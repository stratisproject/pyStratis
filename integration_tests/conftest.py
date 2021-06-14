import pytest
import re
import os
import shutil
import subprocess
import time
from typing import List, Optional, Union
from requests.exceptions import ConnectionError
from nodes import StraxNode, CirrusNode, InterfluxCirrusNode, InterfluxStraxNode, BaseNode
from pybitcoin.networks import BaseNetwork
from pybitcoin.types import Address, Money


@pytest.fixture(scope='session')
def start_regtest_node():
    def _start_regtest_node(
            node: Union[StraxNode, CirrusNode, InterfluxCirrusNode, InterfluxStraxNode],
            source_dir: str,
            extra_cmd_ops: List[str] = None) -> None:
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
def send_a_transaction():
    def _send_a_transaction(
            node: BaseNode,
            sending_address: Address,
            receiving_address: Address,
            amount: Money) -> bool:
        from api.wallet.requestmodels import BuildTransactionRequest, SpendableTransactionsRequest
        from pybitcoin import Outpoint, Recipient, SendTransactionRequest
        request_model = SpendableTransactionsRequest(wallet_name='Test', account_name='account 0', min_confirmations=10)
        spendable_outpoints = node.wallet.spendable_transactions(request_model)
        spendable_outpoints = [x for x in spendable_outpoints.transactions]
        request_model = BuildTransactionRequest(
            password='password',
            segwit_change_address=False,
            wallet_name='Test',
            account_name='account 0',
            outpoints=[Outpoint(
                transaction_id=str(spendable_outpoints[0].transaction_id),
                index=spendable_outpoints[0].index)
            ],
            recipients=[
                Recipient(
                    destination_address=receiving_address,
                    subtraction_fee_from_amount=True,
                    amount=amount
                )
            ],
            fee_type='low',
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
def sync_node_to_height():
    def _sync_node_to_height(a: BaseNode, b: BaseNode) -> bool:
        while True:
            time.sleep(10)
            if a.consensus.get_best_blockhash() == b.consensus.get_best_blockhash():
                return True
    return _sync_node_to_height


@pytest.fixture(scope='session')
def node_creates_a_wallet():
    def _node_creates_a_wallet(node: BaseNode, name: str = 'Test') -> bool:
        from api.wallet.requestmodels import CreateRequest
        mnemonic = node.wallet.create(CreateRequest(name=name, password='password', passphrase='passphrase'))
        return len(mnemonic) == 12
    return _node_creates_a_wallet


@pytest.fixture(scope='session')
def get_node_address_with_balance():
    def _get_node_address_with_balance(node: BaseNode) -> Optional[Address]:
        from api.wallet.requestmodels import BalanceRequest
        request_model = BalanceRequest(
            wallet_name='Test',
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
    def _get_node_unused_address(node: BaseNode) -> Address:
        from api.wallet.requestmodels import GetUnusedAddressRequest
        request_model = GetUnusedAddressRequest(
            wallet_name='Test',
            account_name='account 0',
            segwit=False
        )
        return node.wallet.unused_address(request_model)
    return _get_node_unused_address


@pytest.fixture(scope='session')
def git_checkout_current_node_version():
    def _git_checkout_current_node_version(version: str) -> None:
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
