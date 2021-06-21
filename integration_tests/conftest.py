import pytest
import re
import os
import shutil
import subprocess
import time
from typing import List, Optional, Union
from requests.exceptions import ConnectionError
from nodes import StraxNode, CirrusMinerNode, CirrusNode, InterfluxCirrusNode, InterfluxStraxNode, BaseNode
from api.wallet.requestmodels import BuildTransactionRequest, SendTransactionRequest, SpendableTransactionsRequest
from api.wallet.responsemodels import SpendableTransactionModel
from pybitcoin.networks import BaseNetwork, StraxRegTest, CirrusRegTest
from pybitcoin.types import Address, Money
from pybitcoin import Outpoint, Recipient
STRAX_HOT_NODE_PORT = 12370
STRAX_SYNCING_NODE_PORT = 12380
STRAX_OFFLINE_NODE_PORT = 12390
CIRRUSMINER_NODE_PORT = 13370
CIRRUSMINER_SYNCING_NODE_PORT = 13380
CIRRUS_NODE_PORT = 13390


@pytest.fixture(scope='session')
def get_spendable_transactions():
    def _get_spendable_transactions(
            node: BaseNode,
            amount: Money,
            op_return_amount: Money = Money(0.00000001),
            min_confirmations: int = 2,
            wallet_name: str = 'Test') -> List[SpendableTransactionModel]:
        request_model = SpendableTransactionsRequest(wallet_name=wallet_name, account_name='account 0', min_confirmations=min_confirmations)
        spendable_transactions = node.wallet.spendable_transactions(request_model)
        spendable_transactions = [x for x in spendable_transactions.transactions]
        sorted_spendable_transactions = sorted(spendable_transactions, key=lambda x: int(x.amount))
        amount_to_send = amount
        op_return_amount = op_return_amount
        transactions = []
        trxid_amount = Money(0)
        for spendable_transaction in sorted_spendable_transactions:
            transactions.append(spendable_transaction)
            trxid_amount += spendable_transaction.amount
            if trxid_amount >= amount_to_send + op_return_amount:
                break
        if trxid_amount < amount_to_send + op_return_amount:
            raise RuntimeError('Not enough funds in spendable transactions for specified amount.')
        return transactions
    return _get_spendable_transactions


@pytest.fixture(scope='session')
def start_regtest_node(request):
    def _start_regtest_node(
            node: Union[StraxNode, CirrusNode, CirrusMinerNode, InterfluxCirrusNode, InterfluxStraxNode],
            source_dir: str,
            extra_cmd_ops: List[str] = None,
            private_key: bytes = None) -> BaseNode:
        # Kill any running nodes using same ports.
        try:
            node.node.stop()
            time.sleep(10)
        except ConnectionError:
            pass
        root_dir = re.match(r'(.*)pystratis', os.getcwd())[0]
        data_dir = os.path.join(root_dir, 'integration_tests', 'data_dir', f'{node.name}-node-{node.blockchainnetwork.API_PORT}')
        if os.path.exists(data_dir):
            shutil.rmtree(data_dir)
        if private_key is not None:
            os.makedirs(os.path.join(data_dir, 'cirrus', 'CirrusRegTest'), exist_ok=True)
            fed_keyfile_target_path = os.path.join(data_dir, 'cirrus', 'CirrusRegTest', 'federationKey.dat')
            with open(fed_keyfile_target_path, 'w+b') as f:
                f.write(bytearray(private_key))

        root_dir = os.getcwd()
        os.chdir(source_dir)
        cmd_args = [
            'dotnet', 'run', '-regtest', f'-datadir={data_dir}', '-addressindex=1', '-txindex=1', '-server=1',
            f'-apiport={node.blockchainnetwork.API_PORT}', f'-port={node.blockchainnetwork.DEFAULT_PORT}',
            f'-signalrport={node.blockchainnetwork.SIGNALR_PORT}', f'-rpcport={node.blockchainnetwork.RPC_PORT}'
        ]
        if extra_cmd_ops is not None:
            cmd_args += extra_cmd_ops
        subprocess.Popen(cmd_args)
        os.chdir(root_dir)
        # Wait for node to start.
        while True:
            try:
                node.node.status()
                break
            except ConnectionError:
                time.sleep(5)
        print('Node started.')

        def stop_node():
            node.node.stop()

        request.addfinalizer(stop_node)
        return node
    return _start_regtest_node


@pytest.fixture(scope='session')
def random_addresses(generate_p2pkh_address):
    def _random_addresses(network: BaseNetwork) -> List[Address]:
        return [
            Address(address=generate_p2pkh_address(network=network), network=network),
            Address(address=generate_p2pkh_address(network=network), network=network),
            Address(address=generate_p2pkh_address(network=network), network=network),
            Address(address=generate_p2pkh_address(network=network), network=network),
            Address(address=generate_p2pkh_address(network=network), network=network)
        ]
    return _random_addresses


@pytest.fixture(scope='session')
def send_a_transaction(get_spendable_transactions):
    def _send_a_transaction(
            node: BaseNode,
            sending_address: Address,
            receiving_address: Address,
            amount_to_send: Money,
            wallet_name: str = 'Test',
            min_confirmations: int = 10,
            op_return_amount: Money = Money(0)) -> bool:
        spendable_transactions = get_spendable_transactions(
            node=node, amount=amount_to_send, op_return_amount=op_return_amount, wallet_name=wallet_name, min_confirmations=min_confirmations
        )

        request_model = BuildTransactionRequest(
            password='password',
            segwit_change_address=False,
            wallet_name=wallet_name,
            account_name='account 0',
            outpoints=[Outpoint(transaction_id=str(x.transaction_id), index=x.index) for x in spendable_transactions],
            recipients=[Recipient(destination_address=receiving_address, subtraction_fee_from_amount=True, amount=amount_to_send)],
            fee_type='high',
            allow_unconfirmed=True,
            shuffle_outputs=True,
            change_address=sending_address
        )
        transaction = node.wallet.build_transaction(request_model)
        request_model = SendTransactionRequest(
            hex=transaction.hex
        )
        node.wallet.send_transaction(request_model)
        return True
    return _send_a_transaction


@pytest.fixture(scope='session')
def get_node_endpoint():
    def _get_node_endpoint(node: BaseNode) -> str:
        localhost_ip = node.ipaddr.replace('http://localhost', '[::ffff:127.0.0.1]')
        return f'{localhost_ip}:{node.blockchainnetwork.DEFAULT_PORT}'
    return _get_node_endpoint


@pytest.fixture(scope='session')
def sync_two_nodes():
    def _sync_two_nodes(a: BaseNode, b: BaseNode) -> bool:
        while True:
            time.sleep(10)
            if a.consensus.get_best_blockhash() == b.consensus.get_best_blockhash():
                return True
    return _sync_two_nodes


@pytest.fixture(scope='session')
def node_creates_a_wallet():
    def _node_creates_a_wallet(node: BaseNode, wallet_name: str = 'Test') -> bool:
        from api.wallet.requestmodels import CreateRequest
        mnemonic = node.wallet.create(CreateRequest(name=wallet_name, password='password', passphrase='passphrase'))
        return len(mnemonic) == 12
    return _node_creates_a_wallet


@pytest.fixture(scope='session')
def get_node_address_with_balance():
    def _get_node_address_with_balance(node: BaseNode, wallet_name: str = 'Test') -> Optional[Address]:
        from api.wallet.requestmodels import BalanceRequest
        request_model = BalanceRequest(
            wallet_name=wallet_name,
            account_name='account 0',
            include_balance_by_address=True
        )
        balances = node.wallet.balance(request_model)
        used_addresses = [x.address for x in balances.balances[0].addresses if x.is_used]
        if len(used_addresses) >= 1:
            return used_addresses[0]
    return _get_node_address_with_balance


@pytest.fixture(scope='session')
def connect_two_nodes(get_node_endpoint):
    def _connect_two_nodes(a: BaseNode, b: BaseNode):
        from api.connectionmanager.requestmodels import AddNodeRequest
        request_model = AddNodeRequest(endpoint=get_node_endpoint(b), command='add')
        a.connection_manager.addnode(request_model)
        return True
    return _connect_two_nodes


@pytest.fixture(scope='session')
def get_node_unused_address():
    def _get_node_unused_address(node: BaseNode, wallet_name: str = 'Test') -> Address:
        from api.wallet.requestmodels import GetUnusedAddressRequest
        request_model = GetUnusedAddressRequest(
            wallet_name=wallet_name,
            account_name='account 0',
            segwit=False
        )
        return node.wallet.unused_address(request_model)
    return _get_node_unused_address


@pytest.fixture(scope='session')
def git_checkout_current_node_version():
    def _git_checkout_current_node_version(version: str):
        """Checks out the most current version of the StratisFullNode with the specified branch.

        Returns:
            None
        """
        project_uri = 'https://github.com/stratisproject/StratisFullNode.git'
        root_dir = re.match(r'(.*)pystratis', os.getcwd())[0]
        clone_dir = os.path.join(root_dir, 'integration_tests', 'StratisFullNode')

        if not os.path.exists(os.path.join(clone_dir)):
            os.system(f'git clone {project_uri} {clone_dir}')
            os.chdir(clone_dir)
            os.system('git fetch')
            os.system(f'git checkout -b release/{version} origin/release/{version}')
            os.system(f'git pull')
            os.chdir(root_dir)
        else:
            os.chdir(clone_dir)
            os.system('git fetch')
            os.system(f'git checkout release/{version}')
            os.system(f'git pull')
            os.chdir(root_dir)
    return _git_checkout_current_node_version


def strax_regtest_node(port: int) -> StraxNode:
    node = StraxNode(
        ipaddr='http://localhost',
        blockchainnetwork=StraxRegTest(
            API_PORT=port,
            DEFAULT_PORT=port + 1,
            SIGNALR_PORT=port + 2,
            RPC_PORT=port + 3
        )
    )
    return node


@pytest.fixture(scope='session')
def start_strax_regtest_node(start_regtest_node):
    def _start_strax_regtest_node(node: StraxNode, extra_cmd_ops: List = None):
        root_dir = re.match(r'(.*)pystratis', os.getcwd())[0]
        source_dir = os.path.join(root_dir, 'integration_tests', 'StratisFullNode', 'src', 'Stratis.StraxD')
        start_regtest_node(node=node, source_dir=source_dir, extra_cmd_ops=extra_cmd_ops)
    return _start_strax_regtest_node


@pytest.fixture(scope='session')
def node_mines_some_blocks_and_syncs(sync_two_nodes):
    def _node_mines_some_blocks_and_syncs(
            mining_node: StraxNode,
            syncing_node: StraxNode = None,
            num_blocks_to_mine: int = 1) -> bool:
        from api.mining.requestmodels import GenerateRequest
        mining_node.mining.generate(GenerateRequest(block_count=num_blocks_to_mine))
        if syncing_node is None:
            return True
        return sync_two_nodes(mining_node, syncing_node)
    return _node_mines_some_blocks_and_syncs


@pytest.fixture(scope='session')
def strax_hot_node():
    return strax_regtest_node(port=STRAX_HOT_NODE_PORT)


@pytest.fixture(scope='session')
def strax_syncing_node():
    return strax_regtest_node(port=STRAX_SYNCING_NODE_PORT)


@pytest.fixture(scope='session')
def strax_offline_node():
    return strax_regtest_node(port=STRAX_OFFLINE_NODE_PORT)


@pytest.fixture(scope='session')
def cirrusminer_node():
    return cirrusminer_regtest_node(port=CIRRUSMINER_NODE_PORT, devmode=True)


@pytest.fixture(scope='session')
def cirrusminer_syncing_node():
    return cirrusminer_regtest_node(port=CIRRUSMINER_SYNCING_NODE_PORT, devmode=True)


@pytest.fixture(scope='session')
def cirrus_node():
    return cirrus_regtest_node(port=CIRRUS_NODE_PORT)


def cirrusminer_regtest_node(port: int, devmode: bool = True) -> CirrusMinerNode:
    node = CirrusMinerNode(
        ipaddr='http://localhost',
        blockchainnetwork=CirrusRegTest(
            API_PORT=port,
            DEFAULT_PORT=port + 1,
            SIGNALR_PORT=port + 2,
            RPC_PORT=port + 3
        ), devmode=devmode
    )
    return node


def cirrus_regtest_node(port: int) -> CirrusNode:
    node = CirrusNode(
        ipaddr='http://localhost',
        blockchainnetwork=CirrusRegTest(
            API_PORT=port,
            DEFAULT_PORT=port + 1,
            SIGNALR_PORT=port + 2,
            RPC_PORT=port + 3
        )
    )
    return node


@pytest.fixture(scope='session')
def start_cirrusminer_regtest_node(start_regtest_node):
    def _start_cirrusminer_regtest_node(node: CirrusMinerNode, extra_cmd_ops: List[str], private_key: bytes = None):
        root_dir = re.match(r'(.*)pystratis', os.getcwd())[0]
        source_dir = os.path.join(root_dir, 'integration_tests', 'StratisFullNode', 'src', 'Stratis.CirrusMinerD')
        start_regtest_node(node=node, source_dir=source_dir, extra_cmd_ops=extra_cmd_ops, private_key=private_key)
    return _start_cirrusminer_regtest_node


@pytest.fixture(scope='session')
def start_cirrus_regtest_node(start_regtest_node):
    def _start_cirrus_regtest_node(node: CirrusNode, extra_cmd_ops: List[str]):
        root_dir = re.match(r'(.*)pystratis', os.getcwd())[0]
        source_dir = os.path.join(root_dir, 'integration_tests', 'StratisFullNode', 'src', 'Stratis.CirrusD')
        start_regtest_node(node=node, source_dir=source_dir, extra_cmd_ops=extra_cmd_ops)
    return _start_cirrus_regtest_node


@pytest.fixture(scope='session')
def check_at_or_above_given_block_height():
    def _check_at_or_above_given_block_height(node: BaseNode, height: int) -> False:
        return True if node.blockstore.get_block_count() >= height else False
    return _check_at_or_above_given_block_height
