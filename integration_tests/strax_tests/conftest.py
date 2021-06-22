import pytest
from pybitcoin.types import Money
import time
import api


@pytest.fixture(scope='module', autouse=True)
def initialize_nodes(
        start_strax_regtest_node,
        strax_hot_node,
        strax_syncing_node,
        strax_offline_node,
        node_mines_some_blocks_and_syncs,
        node_creates_a_wallet,
        send_a_transaction,
        get_node_address_with_balance,
        get_node_unused_address,
        connect_two_nodes,
        git_checkout_current_node_version):
    git_checkout_current_node_version(api.__version__)
    # Start two nodes on the same regtest network.
    start_strax_regtest_node(strax_hot_node)
    start_strax_regtest_node(strax_syncing_node)
    start_strax_regtest_node(strax_offline_node)

    # Confirm endpoints implemented.
    assert strax_hot_node.check_all_endpoints_implemented()

    # Set up wallets for the two nodes. Wallets need to be setup before mining.
    assert node_creates_a_wallet(strax_hot_node)
    assert node_creates_a_wallet(strax_syncing_node)

    # Connect hot and syncing nodes
    assert connect_two_nodes(strax_hot_node, strax_syncing_node)

    # Mine 15 blocks (maturity 10)
    assert node_mines_some_blocks_and_syncs(
        mining_node=strax_hot_node, syncing_node=strax_syncing_node, num_blocks_to_mine=15
    )

    # Get some addresses
    mining_address = get_node_address_with_balance(strax_hot_node)
    receiving_address = get_node_unused_address(strax_syncing_node)

    # Send a transaction to create some activity.
    assert send_a_transaction(
        node=strax_hot_node, sending_address=mining_address,
        receiving_address=receiving_address, amount_to_send=Money(1)
    )

    # Check mempool after transaction added and before mined in a block.
    time.sleep(3)
    assert len(strax_hot_node.mempool.get_raw_mempool()) == 1

    # Mine 15 more blocks
    assert node_mines_some_blocks_and_syncs(
        mining_node=strax_hot_node, syncing_node=strax_syncing_node, num_blocks_to_mine=15
    )

    # Send some back to the mining address
    assert send_a_transaction(
        node=strax_syncing_node, sending_address=receiving_address,
        receiving_address=mining_address, amount_to_send=Money(0.5)
    )

    # Check mempool after transaction added and before mined in a block.
    time.sleep(3)
    assert len(strax_hot_node.mempool.get_raw_mempool()) == 1

    # Mine 15 more blocks
    assert node_mines_some_blocks_and_syncs(
        mining_node=strax_hot_node, syncing_node=strax_syncing_node, num_blocks_to_mine=15
    )
