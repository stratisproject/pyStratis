from nodes import BaseNode, StraxNode
import api
from git_checkout_current_node_version import git_checkout_current_node_version
from addressbook_endpoints import check_addressbook_endpoints
from blockstore_endpoints import check_blockstore_endpoints
from coldstaking_endpoints import check_coldstaking_endpoints
from consensus_endpoints import check_consensus_endpoints
from dashboard_endpoints import check_dashboard_endpoints
from diagnostic_endpoints import check_diagnostic_endpoints
from connectionmanager_endpoints import check_connection_manager_endpoints
from mempool_endpoints import check_mempool_endpoints
from mining_endpoints import check_mining_endpoints
from network_endpoints import check_network_endpoints
from node_endpoints import check_node_endpoints
from rpc_endpoints import check_rpc_endpoints
from signalr_endpoints import check_signalr_endpoints
from staking_endpoints import check_staking_endpoints
from wallet_endpoints import check_wallet_endpoints


def test_strax_integration(
        generate_p2pkh_address,
        strax_start_regtest_node,
        stop_regtest_node) -> None:
    git_checkout_current_node_version(api.__version__)

    # Start two nodes on the same regtest network.
    node_a = strax_start_regtest_node(port=12345)
    node_b = strax_start_regtest_node(port=12366)

    # Confirm endpoints implemented.
    assert node_a.check_all_endpoints_implemented()

    # Connect to node b
    check_connection_manager_endpoints(node_a, node_b)

    # Set up wallets for the two nodes
    assert node_creates_a_wallet(node_a)
    assert node_creates_a_wallet(node_b)

    # Mine a block
    assert node_mines_some_blocks(node_a, count=1)

    random_addresses = [
        generate_p2pkh_address(network=node_a.blockchainnetwork),
        generate_p2pkh_address(network=node_a.blockchainnetwork),
        generate_p2pkh_address(network=node_a.blockchainnetwork),
        generate_p2pkh_address(network=node_a.blockchainnetwork),
        generate_p2pkh_address(network=node_a.blockchainnetwork)
    ]
    tip_blockhash = node_a.consensus.get_best_blockhash

    check_addressbook_endpoints(node=node_a, addresses=random_addresses)

    check_blockstore_endpoints(node=node_a, addresses=random_addresses, height=1, block_hash=tip_blockhash)
    check_coldstaking_endpoints(node=node_a)
    check_consensus_endpoints(node=node_a)
    check_dashboard_endpoints(node=node_a)
    check_diagnostic_endpoints(node=node_a)
    check_mempool_endpoints(node=node_a)
    check_mining_endpoints(node=node_a)
    check_network_endpoints(node=node_a)
    check_node_endpoints(node=node_a)
    check_rpc_endpoints(node=node_a)
    check_signalr_endpoints(node=node_a)
    check_staking_endpoints(node=node_a)
    check_wallet_endpoints(node=node_a)

    # TODO

    stop_regtest_node(node_a)
    stop_regtest_node(node_b)


def node_mines_some_blocks(node: StraxNode, count: int = 1) -> bool:
    from api.mining.requestmodels import GenerateRequest
    node.mining.generate(GenerateRequest(block_count=count))
    return node_stops_mining(node)


def node_stops_mining(node: StraxNode) -> bool:
    node.mining.stop_mining()
    return True


def node_creates_a_wallet(node: BaseNode) -> bool:
    from api.wallet.requestmodels import CreateRequest
    mnemonic = node.wallet.create(CreateRequest(name='Test', password='password', passphrase='passphrase'))
    return len(mnemonic) == 12
