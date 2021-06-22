import pytest
import api


@pytest.fixture(scope='module', autouse=True)
def initialize_nodes(
        start_interflux_strax_regtest_node,
        start_interflux_cirrus_regtest_node,
        interflux_strax_node,
        interflux_strax_syncing_node,
        interflux_cirrusminer_node,
        interflux_cirrusminer_syncing_node,
        node_creates_a_wallet,
        send_a_transaction,
        get_node_address_with_balance,
        get_node_unused_address,
        node_mines_some_blocks_and_syncs,
        connect_two_nodes,
        sync_two_nodes,
        get_federation_private_key,
        interflux_wait_n_blocks_and_sync,
        transfer_funds_to_test,
        balance_funds_across_nodes,
        fund_smartcontract_address,
        check_at_or_above_given_block_height,
        make_some_transactions_by_splitting,
        git_checkout_current_node_version):
    git_checkout_current_node_version(api.__version__)

    # Start two cirrus nodes on the same regtest network.
    cirrusminer_extra_cmd_ops_node_mining = ['-devmode=miner', '-mincoinmaturity=1', '-mindepositconfirmations=1', '-bantime=1']
    cirrusminer_extra_cmd_ops_node_syncing = ['-devmode=miner', '-mincoinmaturity=1', '-mindepositconfirmations=1', '-bantime=1',
                                              f'-whitelist=127.0.0.1:{interflux_cirrusminer_node.blockchainnetwork.DEFAULT_PORT}']
    start_interflux_strax_regtest_node(interflux_strax_node)
    node_mines_some_blocks_and_syncs(interflux_strax_node, None, 10)
    start_interflux_cirrus_regtest_node(interflux_cirrusminer_node, extra_cmd_ops=cirrusminer_extra_cmd_ops_node_mining, private_key=get_federation_private_key(2))

    # Delay starting 2nd node to give first a head start.
    while True:
        if check_at_or_above_given_block_height(interflux_strax_node, 5):
            break

    start_interflux_strax_regtest_node(interflux_strax_syncing_node)
    start_interflux_cirrus_regtest_node(interflux_cirrusminer_node, extra_cmd_ops=cirrusminer_extra_cmd_ops_node_syncing, private_key=get_federation_private_key(2))

    # Check all endpoints
    assert interflux_strax_node.check_all_endpoints_implemented()
    assert interflux_cirrusminer_node.check_all_endpoints_implemented()

    # Set up wallets for the two nodes. Wallets need to be setup before mining or joining federation
    assert node_creates_a_wallet(interflux_strax_node)
    assert node_creates_a_wallet(interflux_strax_syncing_node)
    assert node_creates_a_wallet(interflux_cirrusminer_node)
    assert node_creates_a_wallet(interflux_cirrusminer_syncing_node)

    # Connect federation nodes
    assert connect_two_nodes(interflux_strax_node, interflux_strax_syncing_node)
    assert connect_two_nodes(interflux_cirrusminer_node, interflux_cirrusminer_syncing_node)
    interflux_wait_n_blocks_and_sync(2)

    # Transfer the cirrusdev funds to the first node's wallet, balance the funds, and remove cirrusdev wallet from each.
    transfer_funds_to_test(interflux_cirrusminer_node)
    interflux_wait_n_blocks_and_sync(2)
    transfer_funds_to_test(interflux_cirrusminer_syncing_node)
    interflux_wait_n_blocks_and_sync(2)
    balance_funds_across_nodes(interflux_cirrusminer_node, interflux_cirrusminer_syncing_node)
    interflux_wait_n_blocks_and_sync(2)
    fund_smartcontract_address(interflux_cirrusminer_node)
    interflux_wait_n_blocks_and_sync(2)
    fund_smartcontract_address(interflux_cirrusminer_syncing_node)
    interflux_wait_n_blocks_and_sync(2)
    make_some_transactions_by_splitting(interflux_cirrusminer_node)
    interflux_wait_n_blocks_and_sync(2)
    make_some_transactions_by_splitting(interflux_cirrusminer_syncing_node)
    interflux_wait_n_blocks_and_sync(2)
