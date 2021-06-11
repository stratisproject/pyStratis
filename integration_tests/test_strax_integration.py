import pytest
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
from pybitcoin.types import Money
from pybitcoin import LogRule
from api.wallet.requestmodels import SpendableTransactionsRequest


@pytest.mark.integration_tests
def test_strax_integration(
        generate_p2pkh_address,
        strax_start_regtest_node,
        send_a_transaction,
        node_creates_a_wallet,
        node_mines_some_blocks_and_syncs,
        get_node_address_with_balance,
        get_node_unused_address,
        random_addresses,
        get_node_endpoint,
        stop_regtest_node) -> None:
    git_checkout_current_node_version(api.__version__)

    # Start two nodes on the same regtest network.
    mining_node = strax_start_regtest_node(port=12345)
    receiving_node = strax_start_regtest_node(port=12366)
    offline_node = strax_start_regtest_node(port=12388)

    # Confirm endpoints implemented.
    assert mining_node.check_all_endpoints_implemented()

    # Connect to node b
    check_connection_manager_endpoints(mining_node, receiving_node)

    # Set up wallets for the two nodes. Wallets need to be setup before mining.
    assert node_creates_a_wallet(mining_node)
    assert node_creates_a_wallet(receiving_node)

    # Mine 15 blocks (maturity 10)
    assert node_mines_some_blocks_and_syncs(mining_node=mining_node, syncing_node=receiving_node, num_blocks_to_mine=15)

    # Get some addresses
    mining_address = get_node_address_with_balance(mining_node)
    receiving_address = get_node_unused_address(receiving_node)

    # Send a transaction to create some activity.
    assert send_a_transaction(
        node=mining_node, sending_address=mining_address,
        receiving_address=receiving_address, amount=Money(100000000)
    )

    # Check mempool after transaction added and before mined in a block.
    check_mempool_endpoints(node=mining_node)

    # Mine 15 more blocks
    assert node_mines_some_blocks_and_syncs(mining_node=mining_node, syncing_node=receiving_node, num_blocks_to_mine=15)

    # Send some back to the mining address
    assert send_a_transaction(
        node=receiving_node, sending_address=receiving_address,
        receiving_address=mining_address, amount=Money(50000000)
    )

    # Check mempool after transaction added and before mined in a block.
    check_mempool_endpoints(node=mining_node)

    # Mine 15 more blocks
    assert node_mines_some_blocks_and_syncs(mining_node=mining_node, syncing_node=receiving_node, num_blocks_to_mine=15)

    # Get current tip height, tip hash, and a list of spendable endpoints.
    tip_height = mining_node.blockstore.get_block_count()
    tip_blockhash = mining_node.consensus.get_best_blockhash()
    request_model = SpendableTransactionsRequest(wallet_name='Test', account_name='account 0', min_confirmations=10)
    spendable_transactions = mining_node.wallet.spendable_transactions(request_model)
    spendable_transactions = [x for x in spendable_transactions.transactions]

    check_addressbook_endpoints(node=mining_node, addresses=random_addresses(network=mining_node.blockchainnetwork))

    check_blockstore_endpoints(
        node=mining_node, height=tip_height, block_hash=tip_blockhash,
        addresses=random_addresses(network=mining_node.blockchainnetwork),
    )
    try:
        check_coldstaking_endpoints(
            hot_node=mining_node,
            cold_node=offline_node,
            mining_address=mining_address,
            node_creates_a_wallet=node_creates_a_wallet,
            send_a_transaction=send_a_transaction,
            node_mines_some_blocks_and_syncs=node_mines_some_blocks_and_syncs
        )
    except api.APIError as e:
        print(e.message)
    offline_node.node.stop()
    check_consensus_endpoints(node=mining_node, height=tip_height)
    check_dashboard_endpoints(node=mining_node)
    check_diagnostic_endpoints(node=mining_node)
    check_node_endpoints(
        node=mining_node, block_hash=tip_blockhash, spendable_transactions=spendable_transactions,
        address_string=generate_p2pkh_address(mining_node.blockchainnetwork),
        log_rules=[LogRule(rule_name='Stratis.*', log_level='Debug')]
    )
    check_rpc_endpoints(node=mining_node)
    check_signalr_endpoints(node=mining_node)
    check_staking_endpoints(node=mining_node)
    # check_wallet_endpoints(node=mining_node)

    # Stop mining and disconnect from other node last.
    check_mining_endpoints(node=mining_node, num_blocks_to_mine=1)
    check_network_endpoints(node=mining_node, peer_address=get_node_endpoint(receiving_node))

    stop_regtest_node(mining_node)
    stop_regtest_node(receiving_node)
