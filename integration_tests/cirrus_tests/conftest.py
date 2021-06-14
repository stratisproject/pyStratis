import pytest
import os
import re
from nodes import CirrusNode
from pybitcoin.networks import CirrusRegTest


@pytest.fixture(scope='session')
def cirrus_hot_node(cirrus_regtest_node):
    return cirrus_regtest_node(port=13370)


@pytest.fixture(scope='session')
def cirrus_syncing_node(cirrus_regtest_node):
    return cirrus_regtest_node(port=13380)


@pytest.fixture(scope='session')
def cirrus_regtest_node(start_regtest_node, request):
    def _cirrus_regtest_node(port: int) -> CirrusNode:
        node = CirrusNode(
            ipaddr='http://localhost',
            blockchainnetwork=CirrusRegTest(
                API_PORT=port,
                DEFAULT_PORT=port + 1,
                SIGNALR_PORT=port + 2,
                RPC_PORT=port + 3
            )
        )
        root_dir = re.match(r'(.*)pystratis', os.getcwd())[0]
        source_dir = os.path.join(root_dir, 'integration_tests', 'StratisFullNode', 'src', 'Stratis.CirrusD')
        node = start_regtest_node(node=node, source_dir=source_dir)

        def stop_node():
            node.node.stop()

        request.addfinalizer(stop_node)
        return node
    return _cirrus_regtest_node
