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
        get_federation_compressed_pubkey,
        interflux_wait_n_blocks_and_sync,
        transfer_funds_to_test,
        check_at_or_above_given_block_height,
        git_checkout_current_node_version):
    git_checkout_current_node_version(api.__version__)

    # Start two masternodes nodes on the same regtest network.
    # Configs
    redeem_script = f'2 {get_federation_compressed_pubkey(0)} {get_federation_compressed_pubkey(1)} {get_federation_compressed_pubkey(2)} 3 OP_CHECKMULTISIG'
    interflux_strax_extra_cmd_ops_node_mining = ['-mainchain', f'-federationkeys={get_federation_compressed_pubkey(0)},{get_federation_compressed_pubkey(2)}',
                                                 f'-publickey={get_federation_compressed_pubkey(0)}', '-mindepositconfirmations=1', '-federationips=0.0.0.0,0.0.0.1',
                                                 f'-counterchainapiport={interflux_cirrusminer_node.blockchainnetwork.API_PORT}', f'-redeemscript={redeem_script}']
    interflux_strax_extra_cmd_ops_node_syncing = ['-mainchain', f'-federationkeys={get_federation_compressed_pubkey(0)},{get_federation_compressed_pubkey(2)}',
                                                  f'-publickey={get_federation_compressed_pubkey(2)}', '-mindepositconfirmations=1', '-federationips=0.0.0.0,0.0.0.1',
                                                  f'-counterchainapiport={interflux_cirrusminer_syncing_node.blockchainnetwork.API_PORT}',  f'-redeemscript={redeem_script}']
    interflux_cirrusminer_extra_cmd_ops_node_mining = ['-sidechain', '-devmode=miner', '-mincoinmaturity=1', '-mindepositconfirmations=1', '-bantime=1',
                                                       f'-counterchainapiport={interflux_strax_node.blockchainnetwork.API_PORT}',  f'-redeemscript={redeem_script}']
    interflux_cirrusminer_extra_cmd_ops_node_syncing = ['-sidechain', '-devmode=miner', '-mincoinmaturity=1', '-mindepositconfirmations=1', '-bantime=1',
                                                        f'-whitelist=127.0.0.1:{interflux_cirrusminer_node.blockchainnetwork.DEFAULT_PORT}',
                                                        f'-counterchainapiport={interflux_strax_syncing_node.blockchainnetwork.API_PORT}',  f'-redeemscript={redeem_script}']
    start_interflux_strax_regtest_node(interflux_strax_node, extra_cmd_ops=interflux_strax_extra_cmd_ops_node_mining)
    assert node_creates_a_wallet(interflux_strax_node)
    node_mines_some_blocks_and_syncs(interflux_strax_node, None, 10)
    start_interflux_cirrus_regtest_node(interflux_cirrusminer_node, extra_cmd_ops=interflux_cirrusminer_extra_cmd_ops_node_mining, private_key=get_federation_private_key(2))
    assert node_creates_a_wallet(interflux_cirrusminer_node)

    # Delay starting 2nd masternode to give first a head start.
    while True:
        if check_at_or_above_given_block_height(interflux_strax_node, 5):
            break

    start_interflux_strax_regtest_node(interflux_strax_syncing_node, extra_cmd_ops=interflux_strax_extra_cmd_ops_node_syncing)
    start_interflux_cirrus_regtest_node(interflux_cirrusminer_node, extra_cmd_ops=interflux_cirrusminer_extra_cmd_ops_node_syncing, private_key=get_federation_private_key(2))

    # Check all endpoints
    assert interflux_strax_node.check_all_endpoints_implemented()
    assert interflux_cirrusminer_node.check_all_endpoints_implemented()

    # Set up wallets for the second masternodes.
    assert node_creates_a_wallet(interflux_strax_syncing_node)
    assert node_creates_a_wallet(interflux_cirrusminer_syncing_node)

    # Connect respective networks for each node.
    assert connect_two_nodes(interflux_strax_node, interflux_strax_syncing_node)
    assert connect_two_nodes(interflux_cirrusminer_node, interflux_cirrusminer_syncing_node)
    interflux_wait_n_blocks_and_sync(2)

    # Transfer the cirrusdev funds to the first node's wallet, balance the funds, and remove cirrusdev wallet from each.
    transfer_funds_to_test(interflux_cirrusminer_node)
    interflux_wait_n_blocks_and_sync(2)
    transfer_funds_to_test(interflux_cirrusminer_syncing_node)
    interflux_wait_n_blocks_and_sync(2)
