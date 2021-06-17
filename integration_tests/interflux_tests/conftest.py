import pytest
import os
import re
from nodes import InterfluxStraxNode, InterfluxCirrusNode
from pybitcoin.networks import StraxRegTest, CirrusRegTest
STRAX_HOT_NODE_PORT = 12370
STRAX_SYNCING_NODE_PORT = 12380
CIRRUSMINER_NODE_PORT = 13370
CIRRUS_SYNCING_NODE_PORT = 13380


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
def interflux_cirrusminer_syncing_node(interflux_cirrus_regtest_node):
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
