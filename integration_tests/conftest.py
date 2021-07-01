import pytest
import re
import os
import shutil
import subprocess
import time
from typing import List, Optional, Union
from requests.exceptions import ConnectionError
from nodes import StraxNode, CirrusMinerNode, CirrusNode, InterfluxCirrusNode, InterfluxStraxNode, BaseNode
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
INTERFLUX_STRAX_MAIN_NODE_PORT = 14370
INTERFLUX_STRAX_SYNCING_NODE_PORT = 14380
INTERFLUX_CIRRUS_MAIN_NODE_PORT = 15370
INTERFLUX_CIRRUS_SYNCING_NODE_PORT = 15380


def start_regtest_node(
        node: Union[StraxNode, CirrusNode, CirrusMinerNode, InterfluxCirrusNode, InterfluxStraxNode],
        source_dir: str,
        extra_cmd_ops: List[str] = None,
        private_key: bytes = None) -> BaseNode:
    # Kill any running nodes using same ports.
    assert node.stop_node()
    time.sleep(10)
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
    return node


def strax_regtest_node(port: int) -> StraxNode:
    return StraxNode(
        ipaddr='http://localhost',
        blockchainnetwork=StraxRegTest(
            API_PORT=port,
            DEFAULT_PORT=port + 1,
            SIGNALR_PORT=port + 2,
            RPC_PORT=port + 3
        )
    )


def cirrusminer_regtest_node(port: int, devmode: bool = True) -> CirrusMinerNode:
    return CirrusMinerNode(
        ipaddr='http://localhost',
        blockchainnetwork=CirrusRegTest(
            API_PORT=port,
            DEFAULT_PORT=port + 1,
            SIGNALR_PORT=port + 2,
            RPC_PORT=port + 3
        ), devmode=devmode
    )


def cirrus_regtest_node(port: int) -> CirrusNode:
    return CirrusNode(
        ipaddr='http://localhost',
        blockchainnetwork=CirrusRegTest(
            API_PORT=port,
            DEFAULT_PORT=port + 1,
            SIGNALR_PORT=port + 2,
            RPC_PORT=port + 3
        )
    )


def interflux_strax_regtest_node(port: int) -> InterfluxStraxNode:
    return InterfluxStraxNode(
        ipaddr='http://localhost',
        blockchainnetwork=StraxRegTest(
            API_PORT=port,
            DEFAULT_PORT=port + 1,
            SIGNALR_PORT=port + 2,
            RPC_PORT=port + 3
        )
    )


def interflux_cirrus_regtest_node(port: int) -> InterfluxCirrusNode:
    return InterfluxCirrusNode(
        ipaddr='http://localhost',
        blockchainnetwork=CirrusRegTest(
            API_PORT=port,
            DEFAULT_PORT=port + 1,
            SIGNALR_PORT=port + 2,
            RPC_PORT=port + 3
        )
    )


@pytest.fixture(scope='package')
def get_spendable_transactions():
    def _get_spendable_transactions(
            node: BaseNode,
            amount: Money,
            op_return_amount: Money = Money(0.00000001),
            min_confirmations: int = 0,
            wallet_name: str = 'Test') -> List[SpendableTransactionModel]:
        spendable_transactions = node.wallet.spendable_transactions(
            wallet_name=wallet_name, account_name='account 0', min_confirmations=min_confirmations
        )
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


@pytest.fixture(scope='package')
def random_addresses(generate_p2pkh_address):
    def _random_addresses(network: BaseNetwork) -> List[str]:
        return [
            generate_p2pkh_address(network=network),
            generate_p2pkh_address(network=network),
            generate_p2pkh_address(network=network),
            generate_p2pkh_address(network=network),
            generate_p2pkh_address(network=network),
        ]
    return _random_addresses


@pytest.fixture(scope='package')
def send_a_transaction(get_spendable_transactions):
    def _send_a_transaction(
            node: BaseNode,
            sending_address: Address,
            receiving_address: Address,
            amount_to_send: Money,
            wallet_name: str = 'Test',
            min_confirmations: int = 1,
            op_return_amount: Money = Money(0)) -> bool:
        spendable_transactions = get_spendable_transactions(
                    node=node, amount=amount_to_send, op_return_amount=op_return_amount, wallet_name=wallet_name,
                    min_confirmations=min_confirmations
        )
        transaction = node.wallet.build_transaction(
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
        node.wallet.send_transaction(transaction_hex=transaction.hex)
        time.sleep(3)
        return True
    return _send_a_transaction


@pytest.fixture(scope='package')
def get_node_endpoint():
    def _get_node_endpoint(node: BaseNode) -> str:
        localhost_ip = node.ipaddr.replace('http://localhost', '[::ffff:127.0.0.1]')
        return f'{localhost_ip}:{node.blockchainnetwork.DEFAULT_PORT}'
    return _get_node_endpoint


@pytest.fixture(scope='package')
def sync_two_nodes():
    def _sync_two_nodes(a: BaseNode, b: BaseNode) -> bool:
        while True:
            time.sleep(10)
            a_best_blockhash = a.consensus.get_best_blockhash()
            b_best_blockhash = b.consensus.get_best_blockhash()
            if a_best_blockhash == b_best_blockhash:
                return True
    return _sync_two_nodes


@pytest.fixture(scope='package')
def node_creates_a_wallet():
    def _node_creates_a_wallet(node: BaseNode, wallet_name: str = 'Test', mnemonic: str = None) -> bool:
        mnemonic = node.wallet.create(name=wallet_name, mnemonic=mnemonic, password='password', passphrase='passphrase')
        return len(mnemonic) == 12
    return _node_creates_a_wallet


@pytest.fixture(scope='package')
def get_node_address_with_balance():
    def _get_node_address_with_balance(node: BaseNode, wallet_name: str = 'Test') -> Optional[Address]:
        balances = node.wallet.balance(wallet_name=wallet_name, account_name='account 0', include_balance_by_address=True)
        used_addresses = [x.address for x in balances.balances[0].addresses if x.is_used]
        if len(used_addresses) >= 1:
            return used_addresses[0]
    return _get_node_address_with_balance


@pytest.fixture(scope='package')
def connect_two_nodes(get_node_endpoint):
    def _connect_two_nodes(a: BaseNode, b: BaseNode) -> bool:
        a.connection_manager.addnode(ipaddr=get_node_endpoint(b), command='add')
        time.sleep(3)
        return True
    return _connect_two_nodes


@pytest.fixture(scope='package')
def get_node_unused_address():
    def _get_node_unused_address(node: BaseNode, wallet_name: str = 'Test') -> Optional[Address]:
        return node.wallet.unused_address(wallet_name=wallet_name, account_name='account 0', segwit=False)
    return _get_node_unused_address


@pytest.fixture(scope='package')
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


@pytest.fixture(scope='package')
def start_strax_regtest_node():
    def _start_strax_regtest_node(node: StraxNode, extra_cmd_ops: List = None):
        root_dir = re.match(r'(.*)pystratis', os.getcwd())[0]
        source_dir = os.path.join(root_dir, 'integration_tests', 'StratisFullNode', 'src', 'Stratis.StraxD')
        start_regtest_node(node=node, source_dir=source_dir, extra_cmd_ops=extra_cmd_ops)
    return _start_strax_regtest_node


@pytest.fixture(scope='package')
def node_mines_some_blocks_and_syncs(sync_two_nodes):
    def _node_mines_some_blocks_and_syncs(
            mining_node: StraxNode,
            syncing_node: StraxNode = None,
            num_blocks_to_mine: int = 1) -> bool:
        mining_node.mining.generate(block_count=num_blocks_to_mine)
        time.sleep(10)
        if syncing_node is None:
            return True
        return sync_two_nodes(mining_node, syncing_node)
    return _node_mines_some_blocks_and_syncs


@pytest.fixture(scope='package')
def strax_hot_node():
    node = strax_regtest_node(port=STRAX_HOT_NODE_PORT)
    yield node
    assert node.stop_node()


@pytest.fixture(scope='package')
def strax_syncing_node():
    node = strax_regtest_node(port=STRAX_SYNCING_NODE_PORT)
    yield node
    assert node.stop_node()


@pytest.fixture(scope='package')
def strax_offline_node():
    node = strax_regtest_node(port=STRAX_OFFLINE_NODE_PORT)
    yield node
    assert node.stop_node()


@pytest.fixture(scope='package')
def cirrusminer_node():
    node = cirrusminer_regtest_node(port=CIRRUSMINER_NODE_PORT, devmode=True)
    yield node
    assert node.stop_node()


@pytest.fixture(scope='package')
def cirrusminer_syncing_node():
    node = cirrusminer_regtest_node(port=CIRRUSMINER_SYNCING_NODE_PORT, devmode=True)
    yield node
    assert node.stop_node()


@pytest.fixture(scope='package')
def cirrus_node():
    node = cirrus_regtest_node(port=CIRRUS_NODE_PORT)
    yield node
    assert node.stop_node()


@pytest.fixture(scope='package')
def interflux_strax_node():
    node = interflux_strax_regtest_node(port=INTERFLUX_STRAX_MAIN_NODE_PORT)
    yield node
    assert node.stop_node()


@pytest.fixture(scope='package')
def interflux_strax_syncing_node():
    node = interflux_strax_regtest_node(port=INTERFLUX_STRAX_SYNCING_NODE_PORT)
    yield node
    assert node.stop_node()


@pytest.fixture(scope='package')
def interflux_cirrusminer_node():
    node = interflux_cirrus_regtest_node(port=INTERFLUX_CIRRUS_MAIN_NODE_PORT)
    yield node
    assert node.stop_node()


@pytest.fixture(scope='package')
def interflux_cirrusminer_syncing_node():
    node = interflux_cirrus_regtest_node(port=INTERFLUX_CIRRUS_SYNCING_NODE_PORT)
    yield node
    assert node.stop_node()


@pytest.fixture(scope='package')
def start_cirrusminer_regtest_node():
    def _start_cirrusminer_regtest_node(node: CirrusMinerNode, extra_cmd_ops: List[str], private_key: bytes = None):
        root_dir = re.match(r'(.*)pystratis', os.getcwd())[0]
        source_dir = os.path.join(root_dir, 'integration_tests', 'StratisFullNode', 'src', 'Stratis.CirrusMinerD')
        start_regtest_node(node=node, source_dir=source_dir, extra_cmd_ops=extra_cmd_ops, private_key=private_key)
    return _start_cirrusminer_regtest_node


@pytest.fixture(scope='package')
def start_cirrus_regtest_node():
    def _start_cirrus_regtest_node(node: CirrusNode, extra_cmd_ops: List[str]):
        root_dir = re.match(r'(.*)pystratis', os.getcwd())[0]
        source_dir = os.path.join(root_dir, 'integration_tests', 'StratisFullNode', 'src', 'Stratis.CirrusD')
        start_regtest_node(node=node, source_dir=source_dir, extra_cmd_ops=extra_cmd_ops)
    return _start_cirrus_regtest_node


@pytest.fixture(scope='package')
def check_at_or_above_given_block_height():
    def _check_at_or_above_given_block_height(node: BaseNode, height: int) -> False:
        return True if node.blockstore.get_block_count() >= height else False
    return _check_at_or_above_given_block_height


@pytest.fixture(scope='package')
def start_interflux_strax_regtest_node():
    def _start_interflux_strax_regtest_node(node: InterfluxStraxNode, extra_cmd_ops: List = None):
        root_dir = re.match(r'(.*)pystratis', os.getcwd())[0]
        source_dir = os.path.join(root_dir, 'integration_tests', 'StratisFullNode', 'src', 'Stratis.CirrusPegD')
        start_regtest_node(node=node, source_dir=source_dir, extra_cmd_ops=extra_cmd_ops)
    return _start_interflux_strax_regtest_node


@pytest.fixture(scope='package')
def start_interflux_cirrus_regtest_node():
    def _start_interflux_cirrus_regtest_node(node: InterfluxCirrusNode, extra_cmd_ops: List = None, private_key: bytes = None):
        root_dir = re.match(r'(.*)pystratis', os.getcwd())[0]
        source_dir = os.path.join(root_dir, 'integration_tests', 'StratisFullNode', 'src', 'Stratis.CirrusPegD')
        start_regtest_node(node=node, source_dir=source_dir, extra_cmd_ops=extra_cmd_ops, private_key=private_key)
    return _start_interflux_cirrus_regtest_node


@pytest.fixture(scope='package')
def wait_and_clear_mempool(cirrusminer_node: CirrusMinerNode,
                           cirrusminer_syncing_node: CirrusMinerNode,
                           check_at_or_above_given_block_height):
    def _wait_and_clear_mempool(wait: int = 5) -> bool:
        time.sleep(wait)
        while True:
            mempool = cirrusminer_node.mempool.get_raw_mempool()
            if len(mempool) == 0:
                confirmed_height = cirrusminer_node.blockstore.get_block_count()
                break
            time.sleep(5)
        while True:
            above_height = check_at_or_above_given_block_height(cirrusminer_syncing_node, confirmed_height + 2)
            if above_height:
                break
            time.sleep(5)
        return True
    return _wait_and_clear_mempool


@pytest.fixture(scope='package')
def interflux_wait_and_clear_mempool(interflux_cirrusminer_node: InterfluxCirrusNode,
                                     cirrus_node: CirrusNode,
                                     check_at_or_above_given_block_height):
    def _interflux_wait_and_clear_mempool(wait: int = 5):
        time.sleep(wait)
        while True:
            mempool = cirrusminer_node.mempool.get_raw_mempool()
            if len(mempool) == 0:
                confirmed_height = cirrusminer_node.blockstore.get_block_count()
                break
            time.sleep(5)
        while True:
            if check_at_or_above_given_block_height(cirrus_node, confirmed_height + 2):
                break
            time.sleep(5)
    return _interflux_wait_and_clear_mempool


@pytest.fixture(scope='package')
def transfer_funds_to_test(send_a_transaction, get_node_address_with_balance, get_node_unused_address):
    def _transfer_funds_to_test_wallet(node: BaseNode) -> bool:
        node_cirrusdev_balance = node.wallet.balance(wallet_name='cirrusdev')
        node_test_balance = node.wallet.balance(wallet_name='Test')

        if node_cirrusdev_balance.balances[0].spendable_amount < 1 and node_test_balance.balances[0].spendable_amount == 0:
            return True

        if node_cirrusdev_balance.balances[0].spendable_amount > node_test_balance.balances[0].spendable_amount:
            cirrusdev_address = get_node_address_with_balance(node, wallet_name='cirrusdev')
            test_address = get_node_unused_address(node)

            assert send_a_transaction(
                node=node, sending_address=cirrusdev_address, wallet_name='cirrusdev',
                receiving_address=test_address, amount_to_send=Money(1000000), min_confirmations=0
            )
        node.wallet.remove_wallet(wallet_name='cirrusdev')
        return True
    return _transfer_funds_to_test_wallet


@pytest.fixture(scope='package')
def balance_funds_across_nodes(send_a_transaction, get_node_address_with_balance, get_node_unused_address):
    def _balance_funds_across_nodes(a: BaseNode, b: BaseNode) -> bool:
        a_balance = a.wallet.balance(wallet_name='Test')
        b_balance = b.wallet.balance(wallet_name='Test')

        if a_balance.balances[0].spendable_amount > b_balance.balances[0].spendable_amount:
            sending_address = get_node_address_with_balance(a)
            receiving_address = get_node_unused_address(b)
            sending_node = a
            amount = a_balance.balances[0].spendable_amount / 2
        else:
            sending_address = get_node_address_with_balance(b)
            receiving_address = get_node_unused_address(a)
            sending_node = b
            amount = b_balance.balances[0].spendable_amount / 2
        assert send_a_transaction(
            node=sending_node, sending_address=sending_address, wallet_name='Test',
            receiving_address=receiving_address, amount_to_send=amount, min_confirmations=0
        )
        return True
    return _balance_funds_across_nodes
