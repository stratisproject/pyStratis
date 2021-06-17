import pytest
import api
from api.wallet.requestmodels import BalanceRequest, RemoveWalletRequest
from pybitcoin.types import Money
from nodes import CirrusMinerNode, BaseNode
import time


@pytest.fixture(scope='session', autouse=True)
def initialize_nodes(
        start_cirrusminer_regtest_node,
        start_cirrus_regtest_node,
        cirrusminer_node,
        cirrusminer_syncing_node,
        cirrus_node,
        node_creates_a_wallet,
        send_a_transaction,
        get_node_address_with_balance,
        get_node_unused_address,
        connect_two_nodes,
        sync_two_nodes,
        generate_privatekey,
        wait_x_blocks_and_sync,
        transfer_funds_to_test,
        balance_funds_across_nodes,
        check_at_or_above_given_block_height,
        git_checkout_current_node_version):
    git_checkout_current_node_version(api.__version__)

    # Start two cirrus nodes on the same regtest network.
    cirrusminer_extra_cmd_ops_node_mining = ['-devmode=miner', '-mincoinmaturity=1', '-mindepositconfirmations=1', '-bantime=1']
    cirrusminer_extra_cmd_ops_node_syncing = ['-devmode=miner', '-mincoinmaturity=1', '-mindepositconfirmations=1', '-bantime=1',
                                              f'-whitelist=127.0.0.1:{cirrusminer_node.blockchainnetwork.DEFAULT_PORT}']
    cirrus_extra_cmd_ops_node_syncing = ['-mincoinmaturity=1', '-mindepositconfirmations=1', '-bantime=1',
                                         f'-whitelist=127.0.0.1:{cirrusminer_node.blockchainnetwork.DEFAULT_PORT}']
    start_cirrusminer_regtest_node(cirrusminer_node, extra_cmd_ops=cirrusminer_extra_cmd_ops_node_mining, copy_private_key=True)

    # Delay starting 2nd node to give first a head start.
    while True:
        if check_at_or_above_given_block_height(cirrusminer_node, 3):
            break

    start_cirrusminer_regtest_node(cirrusminer_syncing_node, extra_cmd_ops=cirrusminer_extra_cmd_ops_node_syncing, copy_private_key=True, key_index=2)
    start_cirrus_regtest_node(cirrus_node, extra_cmd_ops=cirrus_extra_cmd_ops_node_syncing)

    # Check all endpoints
    assert cirrusminer_node.check_all_endpoints_implemented()
    assert cirrusminer_syncing_node.check_all_endpoints_implemented()
    assert cirrus_node.check_all_endpoints_implemented()

    # Set up wallets for the two nodes. Wallets need to be setup before mining or joining federation
    assert node_creates_a_wallet(cirrusminer_node)
    assert node_creates_a_wallet(cirrusminer_syncing_node)
    assert node_creates_a_wallet(cirrus_node)

    # Connect federation nodes
    assert connect_two_nodes(cirrusminer_node, cirrusminer_syncing_node)
    assert connect_two_nodes(cirrusminer_node, cirrus_node)
    wait_x_blocks_and_sync(2)

    # Transfer the cirrusdev funds to the first node's wallet, balance the funds, and remove cirrusdev wallet from each.
    transfer_funds_to_test(cirrusminer_node)
    wait_x_blocks_and_sync(2)
    transfer_funds_to_test(cirrusminer_syncing_node)
    wait_x_blocks_and_sync(2)
    balance_funds_across_nodes(cirrusminer_node, cirrusminer_syncing_node)
    wait_x_blocks_and_sync(2)


@pytest.fixture(scope='session')
def wait_x_blocks_and_sync(cirrusminer_node: CirrusMinerNode,
                           cirrusminer_syncing_node: CirrusMinerNode,
                           check_at_or_above_given_block_height):
    def _wait_x_blocks_and_sync(num_blocks: int):
        current_height = cirrusminer_node.blockstore.get_block_count()
        target = current_height + num_blocks
        while True:
            if check_at_or_above_given_block_height(cirrusminer_node, target) and check_at_or_above_given_block_height(cirrusminer_syncing_node, target):
                break
            time.sleep(1)
    return _wait_x_blocks_and_sync


@pytest.fixture(scope='session')
def transfer_funds_to_test(send_a_transaction, get_node_address_with_balance, get_node_unused_address):
    def _transfer_funds_to_test_wallet(node: BaseNode):
        node_cirrusdev_balance = node.wallet.balance(BalanceRequest(wallet_name='cirrusdev'))
        node_test_balance = node.wallet.balance(BalanceRequest(wallet_name='Test'))

        if node_cirrusdev_balance.balances[0].spendable_amount < 1 and node_test_balance.balances[0].spendable_amount == 0:
            return

        if node_cirrusdev_balance.balances[0].spendable_amount > node_test_balance.balances[0].spendable_amount:
            cirrusdev_address = get_node_address_with_balance(node, wallet_name='cirrusdev')
            test_address = get_node_unused_address(node)

            assert send_a_transaction(
                node=node, sending_address=cirrusdev_address, wallet_name='cirrusdev',
                receiving_address=test_address, amount_to_send=Money(1000000), min_confirmations=2
            )
        node.wallet.remove_wallet(RemoveWalletRequest(wallet_name='cirrusdev'))
    return _transfer_funds_to_test_wallet


@pytest.fixture(scope='session')
def balance_funds_across_nodes(send_a_transaction, get_node_address_with_balance, get_node_unused_address):
    def _balance_funds_across_nodes(a: BaseNode, b: BaseNode):
        a_balance = a.wallet.balance(BalanceRequest(wallet_name='Test'))
        b_balance = b.wallet.balance(BalanceRequest(wallet_name='Test'))

        if a_balance.balances[0].amount_confirmed > b_balance.balances[0].amount_confirmed:
            sending_address = get_node_address_with_balance(a)
            receiving_address = get_node_unused_address(b)
            sending_node = a
        else:
            sending_address = get_node_address_with_balance(b)
            receiving_address = get_node_unused_address(a)
            sending_node = b

        assert send_a_transaction(
            node=sending_node, sending_address=sending_address, wallet_name='Test',
            receiving_address=receiving_address, amount_to_send=Money(500000), min_confirmations=2
        )
    return _balance_funds_across_nodes
