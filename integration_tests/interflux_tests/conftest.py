import pytest
import os
import re
from nodes import InterfluxStraxNode, InterfluxCirrusNode
from pybitcoin.networks import StraxRegTest, CirrusRegTest


@pytest.fixture(scope='session')
def interflux_strax_syncing_node(interflux_strax_regtest_node):
    return interflux_strax_regtest_node(port=12380)


@pytest.fixture(scope='session')
def interflux_strax_offline_node(interflux_strax_regtest_node):
    return interflux_strax_regtest_node(port=12390)


@pytest.fixture(scope='session')
def interflux_cirrusminer_node(interflux_cirrus_regtest_node):
    return interflux_cirrus_regtest_node(port=13370)


@pytest.fixture(scope='session')
def interflux_cirrus_syncing_node(interflux_cirrus_regtest_node):
    return interflux_cirrus_regtest_node(port=13380)


@pytest.fixture(scope='session')
def interflux_strax_regtest_node(start_regtest_node, request):
    def _interflux_strax_regtest_node(port: int) -> InterfluxStraxNode:
        node = InterfluxStraxNode(
            ipaddr='http://localhost',
            blockchainnetwork=StraxRegTest(
                API_PORT=port,
                DEFAULT_PORT=port + 1,
                SIGNALR_PORT=port + 2,
                RPC_PORT=port + 3
            )
        )
        root_dir = re.match(r'(.*)pystratis', os.getcwd())[0]
        source_dir = os.path.join(root_dir, 'integration_tests', 'StratisFullNode', 'src', 'Stratis.CirrusPegD')
        node = start_regtest_node(node=node, source_dir=source_dir)

        def stop_node():
            node.node.stop()

        request.addfinalizer(stop_node)
        return node
    return _interflux_strax_regtest_node


@pytest.fixture(scope='session')
def interflux_cirrus_regtest_node(start_regtest_node, request):
    def _interflux_cirrus_regtest_node(port: int) -> InterfluxCirrusNode:
        node = InterfluxCirrusNode(
            ipaddr='http://localhost',
            blockchainnetwork=CirrusRegTest(
                API_PORT=port,
                DEFAULT_PORT=port + 1,
                SIGNALR_PORT=port + 2,
                RPC_PORT=port + 3
            )
        )
        root_dir = re.match(r'(.*)pystratis', os.getcwd())[0]
        source_dir = os.path.join(root_dir, 'integration_tests', 'StratisFullNode', 'src', 'Stratis.CirrusPegD')
        node = start_regtest_node(node=node, source_dir=source_dir)

        def stop_node():
            node.node.stop()

        request.addfinalizer(stop_node)
        return node
    return _interflux_cirrus_regtest_node



import pytest
import api
from pybitcoin.types import Money
import time
STRAX_HOT_NODE_PORT = 12370
STRAX_SYNCING_NODE_PORT = 12380
CIRRUSMINER_NODE_PORT = 13370
CIRRUS_SYNCING_NODE_PORT = 13380


@pytest.fixture(scope='session', autouse=True)
def initialize_nodes(
        start_strax_regtest_node,
        start_cirrusminer_regtest_node,
        strax_hot_node,
        strax_syncing_node,
        cirrusminer_node,
        cirrus_syncing_node,
        node_creates_a_wallet,
        node_mines_some_blocks_and_syncs,
        send_a_transaction,
        get_node_address_with_balance,
        get_node_unused_address,
        connect_two_nodes,
        git_checkout_current_node_version):
    git_checkout_current_node_version(api.__version__)

    # Start two strax on the same regtest network
    strax_extra_cmd_ops_node_a = []
    strax_extra_cmd_ops_node_b = []
    start_strax_regtest_node(strax_hot_node, extra_cmd_ops=strax_extra_cmd_ops_node_a)
    start_strax_regtest_node(strax_syncing_node, extra_cmd_ops=strax_extra_cmd_ops_node_b)

    # Start two cirrus nodes on the same regtest network.
    cirrus_extra_cmd_ops_node_a = ['-devmode=miner', '-mincoinmaturity=1', '-mindepositconfirmations=1']
    cirrus_extra_cmd_ops_node_b = ['-devmode=default', '-mincoinmaturity=1', '-mindepositconfirmations=1']
    start_cirrusminer_regtest_node(cirrusminer_node, extra_cmd_ops=cirrus_extra_cmd_ops_node_a)
    start_cirrusminer_regtest_node(cirrus_syncing_node, extra_cmd_ops=cirrus_extra_cmd_ops_node_b)

    # Confirm endpoints implemented.
    assert strax_hot_node.check_all_endpoints_implemented()
    assert cirrusminer_node.check_all_endpoints_implemented()

    # Set up wallets for the two nodes. Wallets need to be setup before mining or joining federation
    assert node_creates_a_wallet(strax_hot_node)
    assert node_creates_a_wallet(strax_syncing_node)

    # Connect hot and syncing nodes
    assert connect_two_nodes(strax_hot_node, strax_syncing_node)
    assert connect_two_nodes(cirrusminer_node, cirrus_syncing_node)

    # Mine 15 blocks (maturity 10)
    assert node_mines_some_blocks_and_syncs(
        mining_node=strax_hot_node, syncing_node=strax_syncing_node, num_blocks_to_mine=50
    )

    # Get some addresses
    mining_address = get_node_address_with_balance(strax_hot_node)
    receiving_address = get_node_unused_address(strax_syncing_node)

    # Send a transaction to create some activity.
    assert send_a_transaction(
        node=strax_hot_node, sending_address=mining_address,
        receiving_address=receiving_address, amount_to_send=Money(150000)
    )

    # Check mempool after transaction added and before mined in a block.
    time.sleep(3)
    assert len(strax_hot_node.mempool.get_raw_mempool()) == 1

    # Mine 15 more blocks
    assert node_mines_some_blocks_and_syncs(
        mining_node=strax_hot_node, syncing_node=strax_syncing_node, num_blocks_to_mine=15
    )

    # Mine 15 more blocks
    assert node_mines_some_blocks_and_syncs(
        mining_node=strax_hot_node, syncing_node=strax_syncing_node, num_blocks_to_mine=15
    )
