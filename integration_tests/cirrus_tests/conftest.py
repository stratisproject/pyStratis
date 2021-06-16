import pytest
import api
from binascii import unhexlify
from hashlib import sha256
from pybitcoin.types import Money
from nodes import CirrusMinerNode, CirrusNode
import time
STRAX_HOT_NODE_PORT = 12370
STRAX_SYNCING_NODE_PORT = 12380
CIRRUSMINER_NODE_PORT = 13370
CIRRUS_SYNCING_NODE_PORT = 13380


@pytest.fixture(scope='session', autouse=True)
def initialize_nodes(
        start_cirrusminer_regtest_node,
        start_cirrus_regtest_node,
        cirrusminer_node,
        cirrus_syncing_node,
        node_creates_a_wallet,
        send_a_transaction,
        get_node_address_with_balance,
        get_node_unused_address,
        connect_two_nodes,
        sync_two_nodes,
        generate_privatekey,
        wait_x_blocks_and_sync,
        check_at_or_above_given_block_height,
        git_checkout_current_node_version):
    git_checkout_current_node_version(api.__version__)

    federation_mnemonics = [
        'ensure feel swift crucial bridge charge cloud tell hobby twenty people mandate',
        'quiz sunset vote alley draw turkey hill scrap lumber game differ fiction',
        'fat chalk grant major hair possible adjust talent magnet lobster retreat siren'
    ]

    # Start two cirrus nodes on the same regtest network.
    cirrus_extra_cmd_ops_node_mining = ['-sidechain', '-mincoinmaturity=1', '-mindepositconfirmations=1', '-bantime=1', '-dbtype=rocksdb',
                                        f'-whitelist=127.0.0.1:{cirrus_syncing_node.blockchainnetwork.DEFAULT_PORT}']
    cirrus_extra_cmd_ops_node_syncing = ['-mincoinmaturity=1', '-mindepositconfirmations=1', '-bantime=1',
                                         f'-whitelist=127.0.0.1:{cirrusminer_node.blockchainnetwork.DEFAULT_PORT}']
    start_cirrusminer_regtest_node(cirrusminer_node, extra_cmd_ops=cirrus_extra_cmd_ops_node_mining, copy_private_key=True)
    start_cirrus_regtest_node(cirrus_syncing_node, extra_cmd_ops=cirrus_extra_cmd_ops_node_syncing)

    # Confirm endpoints implemented.
    assert cirrusminer_node.check_all_endpoints_implemented()
    assert cirrus_syncing_node.check_all_endpoints_implemented()

    # Set up wallets for the two nodes. Wallets need to be setup before mining or joining federation
    assert node_creates_a_wallet(cirrusminer_node)
    assert node_creates_a_wallet(cirrus_syncing_node)

    # Connect hot and syncing nodes
    assert connect_two_nodes(cirrusminer_node, cirrus_syncing_node)

    # Get some addresses
    mining_address = get_node_address_with_balance(cirrusminer_node)
    receiving_address = get_node_unused_address(cirrus_syncing_node)

    wait_x_blocks_and_sync(1)

    # Send a transaction to create some activity.
    assert send_a_transaction(
        node=cirrusminer_node, sending_address=mining_address, wallet_name='Test',
        receiving_address=receiving_address, amount_to_send=Money(5000), min_confirmations=1
    )
    wait_x_blocks_and_sync(1)


@pytest.fixture(scope='session')
def wait_x_blocks_and_sync(cirrusminer_node: CirrusMinerNode,
                           cirrus_syncing_node: CirrusNode,
                           connect_two_nodes,
                           check_at_or_above_given_block_height):
    def _wait_x_blocks_and_sync(num_blocks: int):
        cirrusminer_node.network.clear_banned()
        cirrus_syncing_node.network.clear_banned()
        connect_two_nodes(cirrusminer_node, cirrus_syncing_node)
        current_height = cirrusminer_node.blockstore.get_block_count()
        target = current_height + num_blocks
        while True:
            if check_at_or_above_given_block_height(cirrusminer_node, target) and check_at_or_above_given_block_height(cirrus_syncing_node, target):
                break
            time.sleep(1)
    return _wait_x_blocks_and_sync
