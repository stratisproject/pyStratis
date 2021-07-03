import pytest
from pystratis.core.types import Money
from pystratis import api


@pytest.fixture(scope='package', autouse=True)
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
    # Start two nodes on the same regtest network, another offline node.
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

    # Mine 5 blocks
    assert node_mines_some_blocks_and_syncs(mining_node=strax_hot_node, syncing_node=strax_syncing_node, num_blocks_to_mine=15)

    # Get some addresses
    mining_address = get_node_address_with_balance(strax_hot_node)
    receiving_address = get_node_unused_address(strax_syncing_node)

    # Send a transaction to create some activity.
    assert send_a_transaction(node=strax_hot_node, sending_address=mining_address, receiving_address=receiving_address, amount_to_send=Money(1000))

    # Mine more blocks
    assert node_mines_some_blocks_and_syncs(mining_node=strax_hot_node, syncing_node=strax_syncing_node, num_blocks_to_mine=15)

    # Send some back to the mining address
    assert send_a_transaction(node=strax_syncing_node, sending_address=receiving_address, receiving_address=mining_address, amount_to_send=Money(5))

    # Mine more blocks
    assert node_mines_some_blocks_and_syncs(mining_node=strax_hot_node, syncing_node=strax_syncing_node, num_blocks_to_mine=15)

    yield

    # Teardown
    assert strax_hot_node.stop_node()
    assert strax_syncing_node.stop_node()
    assert strax_offline_node.stop_node()
