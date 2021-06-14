import pytest
import os
import re
import time
from nodes import StraxNode
from pybitcoin.types import Money
from pybitcoin.networks import StraxRegTest
import api
HOT_NODE_PORT = 12370
SYNCING_NODE_PORT = 12380
OFFLINE_NODE_PORT = 12390


@pytest.mark.order(1)
@pytest.fixture(scope='session', autouse=True)
def initialize_nodes(
        start_strax_regtest_node,
        hot_node,
        syncing_node,
        offline_node,
        node_mines_some_blocks_and_syncs,
        node_creates_a_wallet,
        send_a_transaction,
        get_node_address_with_balance,
        get_node_unused_address,
        connect_two_nodes,
        git_checkout_current_node_version) -> None:
    git_checkout_current_node_version(api.__version__)
    # Start two nodes on the same regtest network.
    start_strax_regtest_node(hot_node)
    start_strax_regtest_node(syncing_node)
    start_strax_regtest_node(offline_node)

    # Confirm endpoints implemented.
    assert hot_node.check_all_endpoints_implemented()

    # Connect hot and syncing nodes
    assert connect_two_nodes(hot_node, syncing_node)

    # Set up wallets for the two nodes. Wallets need to be setup before mining.
    assert node_creates_a_wallet(hot_node)
    assert node_creates_a_wallet(syncing_node)

    # Mine 15 blocks (maturity 10)
    assert node_mines_some_blocks_and_syncs(
        mining_node=hot_node, syncing_node=syncing_node, num_blocks_to_mine=15
    )

    # Get some addresses
    mining_address = get_node_address_with_balance(hot_node)
    receiving_address = get_node_unused_address(syncing_node)

    # Send a transaction to create some activity.
    assert send_a_transaction(
        node=hot_node, sending_address=mining_address,
        receiving_address=receiving_address, amount=Money(1)
    )

    # Check mempool after transaction added and before mined in a block.
    assert len(hot_node.mempool.get_raw_mempool()) == 1

    # Mine 15 more blocks
    assert node_mines_some_blocks_and_syncs(
        mining_node=hot_node, syncing_node=syncing_node, num_blocks_to_mine=15
    )

    # Send some back to the mining address
    assert send_a_transaction(
        node=syncing_node, sending_address=receiving_address,
        receiving_address=mining_address, amount=Money(0.5)
    )

    # Check mempool after transaction added and before mined in a block.
    time.sleep(3)
    assert len(hot_node.mempool.get_raw_mempool()) == 1

    # Mine 15 more blocks
    assert node_mines_some_blocks_and_syncs(
        mining_node=hot_node, syncing_node=syncing_node, num_blocks_to_mine=15
    )


@pytest.fixture(scope='session')
def hot_node(strax_regtest_node):
    return strax_regtest_node(port=HOT_NODE_PORT)


@pytest.fixture(scope='session')
def syncing_node(strax_regtest_node):
    return strax_regtest_node(port=SYNCING_NODE_PORT)


@pytest.fixture(scope='session')
def offline_node(strax_regtest_node):
    return strax_regtest_node(port=OFFLINE_NODE_PORT)


@pytest.fixture(scope='session')
def strax_regtest_node(start_regtest_node, request):
    def _strax_regtest_node(port: int) -> StraxNode:
        node = StraxNode(
            ipaddr='http://localhost',
            blockchainnetwork=StraxRegTest(
                API_PORT=port,
                DEFAULT_PORT=port+1,
                SIGNALR_PORT=port+2,
                RPC_PORT=port + 3
            )
        )

        def stop_node():
            node.node.stop()
        request.addfinalizer(stop_node)
        return node
    return _strax_regtest_node


@pytest.fixture(scope='session')
def start_strax_regtest_node(start_regtest_node):
    def _start_strax_regtest_node(node: StraxNode):
        root_dir = re.match(r'(.*)pystratis', os.getcwd())[0]
        source_dir = os.path.join(root_dir, 'integration_tests', 'StratisFullNode', 'src', 'Stratis.StraxD')
        start_regtest_node(node=node, source_dir=source_dir)
    return _start_strax_regtest_node


@pytest.fixture(scope='session')
def node_mines_some_blocks_and_syncs(sync_node_to_height):
    def _node_mines_some_blocks_and_syncs(
            mining_node: StraxNode,
            syncing_node: StraxNode = None,
            num_blocks_to_mine: int = 1) -> bool:
        from api.mining.requestmodels import GenerateRequest
        mining_node.mining.generate(GenerateRequest(block_count=num_blocks_to_mine))
        if syncing_node is None:
            return True
        return sync_node_to_height(mining_node, syncing_node)
    return _node_mines_some_blocks_and_syncs
