import pytest
import time
from pystratis import api


@pytest.fixture(scope='package', autouse=True)
def initialize_nodes(
        start_interflux_strax_regtest_node,
        start_interflux_cirrus_regtest_node,
        start_strax_regtest_node,
        strax_hot_node,
        start_cirrus_regtest_node,
        cirrus_node,
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
        get_federation_mnemonic,
        transfer_funds_to_test,
        check_at_or_above_given_block_height,
        generate_privatekey,
        git_checkout_current_node_version):
    git_checkout_current_node_version(api.__version__)

    # Start two masternodes nodes on the same regtest network.
    # Configs
    # redeem_script = '0347f6ba6232037a68ce2b8ac988c07c071eee1e7edd0e6bb9b3dbda22772ad96a OP_FEDERATION OP_CHECKMULTISIG'
    redeem_script = f'2 {get_federation_compressed_pubkey(index=0)} {get_federation_compressed_pubkey(index=1)} {get_federation_compressed_pubkey(index=3)} 3 OP_CHECKMULTISIG'
    interflux_strax_extra_cmd_ops_node_0 = ['-mainchain', f'-publickey={get_federation_compressed_pubkey(index=0)}', '-federationips=127.0.0.1', '-mine=1',
                                            f'-counterchainapiport={interflux_cirrusminer_node.blockchainnetwork.API_PORT}', f'-redeemscript={redeem_script}']
    interflux_cirrusminer_extra_cmd_ops_node_0 = ['-sidechain', f'-publickey={get_federation_compressed_pubkey(index=0)}', '-federationips=127.0.0.1',
                                                  f'-counterchainapiport={interflux_strax_node.blockchainnetwork.API_PORT}', f'-redeemscript={redeem_script}']
    interflux_strax_extra_cmd_ops_node_1 = ['-mainchain', f'-publickey={get_federation_compressed_pubkey(index=1)}', '-federationips=127.0.0.1', '-mine=1',
                                            f'-counterchainapiport={interflux_cirrusminer_node.blockchainnetwork.API_PORT}', f'-redeemscript={redeem_script}']
    interflux_cirrusminer_extra_cmd_ops_node_1 = ['-sidechain', f'-publickey={get_federation_compressed_pubkey(index=1)}', '-federationips=127.0.0.1',
                                                  f'-counterchainapiport={interflux_strax_node.blockchainnetwork.API_PORT}', f'-redeemscript={redeem_script}']
    # Strax mining node
    start_strax_regtest_node(strax_hot_node)
    # 2 Gateway nodes
    start_interflux_strax_regtest_node(interflux_strax_node, extra_cmd_ops=interflux_strax_extra_cmd_ops_node_0)
    start_interflux_cirrus_regtest_node(interflux_cirrusminer_node, extra_cmd_ops=interflux_cirrusminer_extra_cmd_ops_node_0, private_key=get_federation_private_key(0))
    start_interflux_strax_regtest_node(interflux_strax_syncing_node, extra_cmd_ops=interflux_strax_extra_cmd_ops_node_1)
    start_interflux_cirrus_regtest_node(interflux_cirrusminer_syncing_node, extra_cmd_ops=interflux_cirrusminer_extra_cmd_ops_node_1, private_key=get_federation_private_key(1))
    # Cirrus node
    start_cirrus_regtest_node(cirrus_node, extra_cmd_ops=[])

    # Give a little time to startup.
    time.sleep(10)

    # Check all endpoints exist
    assert strax_hot_node.check_all_endpoints_implemented()
    assert interflux_strax_node.check_all_endpoints_implemented()
    assert interflux_strax_syncing_node.check_all_endpoints_implemented()
    assert interflux_cirrusminer_node.check_all_endpoints_implemented()
    assert interflux_cirrusminer_syncing_node.check_all_endpoints_implemented()
    assert cirrus_node.check_all_endpoints_implemented()

    # Create wallets
    assert node_creates_a_wallet(interflux_strax_node)
    assert node_creates_a_wallet(interflux_cirrusminer_node)
    assert node_creates_a_wallet(strax_hot_node)
    assert node_creates_a_wallet(cirrus_node)

    # Enable the federation, connect the nodes.
    assert connect_two_nodes(strax_hot_node, interflux_strax_node)
    assert connect_two_nodes(interflux_cirrusminer_node, cirrus_node)
    interflux_strax_node.federation_wallet.enable_federation(mnemonic=get_federation_mnemonic(0), password='password', timeout_seconds=60)
    interflux_cirrusminer_node.federation_wallet.enable_federation(mnemonic=get_federation_mnemonic(0), password='password', timeout_seconds=60)
    interflux_strax_syncing_node.federation_wallet.enable_federation(mnemonic=get_federation_mnemonic(1), password='password', timeout_seconds=60)
    interflux_cirrusminer_syncing_node.federation_wallet.enable_federation(mnemonic=get_federation_mnemonic(1), password='password', timeout_seconds=60)

    yield

    # Teardown
    assert strax_hot_node.stop_node()
    assert cirrus_node.stop_node()
    assert interflux_strax_node.stop_node()
    assert interflux_strax_syncing_node.stop_node()
    assert interflux_cirrusminer_node.stop_node()
    assert interflux_cirrusminer_syncing_node.stop_node()
