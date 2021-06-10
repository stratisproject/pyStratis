from typing import Optional
import pytest
import time
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
from pybitcoin.types import Address, Money


@pytest.mark.integration_tests
def test_strax_integration(
        generate_p2pkh_address,
        strax_start_regtest_node,
        random_addresses,
        stop_regtest_node) -> None:
    git_checkout_current_node_version(api.__version__)

    # Start two nodes on the same regtest network.
    mining_node = strax_start_regtest_node(port=12345)
    receiving_node = strax_start_regtest_node(port=12366)

    # Confirm endpoints implemented.
    assert mining_node.check_all_endpoints_implemented()

    # Connect to node b
    check_connection_manager_endpoints(mining_node, receiving_node)

    # Set up wallets for the two nodes. Wallets need to be setup before mining.
    assert node_creates_a_wallet(mining_node)
    assert node_creates_a_wallet(receiving_node)

    # Mine 20 blocks (maturity 10)
    assert node_mines_some_blocks_and_syncs(
        mining_node=mining_node,
        syncing_node=receiving_node,
        num_blocks_to_mine=20
    )

    # Get some addresses
    mining_address = get_node_address_with_balance(mining_node)
    receiving_address = get_node_unused_address(receiving_node)

    # Send a transaction to create some activity.
    assert send_a_transaction(
        node=mining_node,
        sending_address=mining_address,
        receiving_address=receiving_address,
        amount=Money(1000000)
    )

    # Mine 20 more blocks
    assert node_mines_some_blocks_and_syncs(
        mining_node=mining_node,
        syncing_node=receiving_node,
        num_blocks_to_mine=20
    )

    # Send some back to the mining address
    assert send_a_transaction(
        node=receiving_node,
        sending_address=receiving_address,
        receiving_address=mining_address,
        amount=Money(500000)
    )

    # Mine 15 more blocks
    assert node_mines_some_blocks_and_syncs(
        mining_node=mining_node,
        syncing_node=receiving_node,
        num_blocks_to_mine=15
    )

    tip_blockhash = mining_node.consensus.get_best_blockhash()

    check_addressbook_endpoints(
        node=mining_node,
        addresses=random_addresses(network=mining_node.blockchainnetwork)
    )

    check_blockstore_endpoints(
        node=mining_node,
        addresses=random_addresses(network=mining_node.blockchainnetwork),
        height=1,
        block_hash=tip_blockhash
    )

    check_coldstaking_endpoints(node=mining_node)
    check_consensus_endpoints(node=mining_node)
    check_dashboard_endpoints(node=mining_node)
    check_diagnostic_endpoints(node=mining_node)
    check_mempool_endpoints(node=mining_node)
    check_mining_endpoints(node=mining_node, num_blocks_to_mine=1)
    check_network_endpoints(node=mining_node)
    check_node_endpoints(node=mining_node)
    check_rpc_endpoints(node=mining_node)
    check_signalr_endpoints(node=mining_node)
    check_staking_endpoints(node=mining_node)
    check_wallet_endpoints(node=mining_node)

    stop_regtest_node(mining_node)
    stop_regtest_node(receiving_node)


def node_mines_some_blocks_and_syncs(
        mining_node: StraxNode,
        syncing_node: StraxNode,
        num_blocks_to_mine: int = 1) -> bool:
    from api.mining.requestmodels import GenerateRequest
    previous_height = mining_node.blockstore.get_block_count()
    mining_node.mining.generate(GenerateRequest(block_count=num_blocks_to_mine))
    sync_node_to_height(syncing_node, previous_height + num_blocks_to_mine)
    return True


def sync_node_to_height(node: BaseNode, height: int) -> bool:
    while node.blockstore.get_block_count() < height:
        time.sleep(5)
    return True


def node_creates_a_wallet(node: BaseNode) -> bool:
    from api.wallet.requestmodels import CreateRequest
    mnemonic = node.wallet.create(CreateRequest(name='Test', password='password', passphrase='passphrase'))
    return len(mnemonic) == 12


def get_node_address_with_balance(node: BaseNode) -> Optional[Address]:
    from api.wallet.requestmodels import BalanceRequest
    request_model = BalanceRequest(
        wallet_name='Test',
        account_name='account 0',
        include_balance_by_address=True
    )
    balances = node.wallet.balance(request_model)
    used_addresses = [x.address for x in balances.balances[0].addresses if x.is_used]
    if len(used_addresses) >= 1:
        return used_addresses[0]


def get_node_unused_address(node: BaseNode) -> Address:
    from api.wallet.requestmodels import GetUnusedAddressRequest
    request_model = GetUnusedAddressRequest(
        wallet_name='Test',
        account_name='account 0',
        segwit=False
    )
    return node.wallet.unused_address(request_model)


def send_a_transaction(
        node: BaseNode,
        sending_address: Address,
        receiving_address: Address,
        amount: Money) -> bool:
    from api.wallet.requestmodels import BuildTransactionRequest, SpendableTransactionsRequest
    from pybitcoin import Outpoint, Recipient, SendTransactionRequest
    request_model = SpendableTransactionsRequest(
        wallet_name='Test',
        account_name='account 0',
        min_confirmations=0
    )
    spendable_outpoints = node.wallet.spendable_transactions(request_model)
    request_model = BuildTransactionRequest(
        password='password',
        segwit_change_address=False,
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=str(spendable_outpoints.transactions[0].transaction_id), index=0)],
        recipients=[
            Recipient(
                destination_address=receiving_address,
                subtraction_fee_from_amount=True,
                amount=amount
            )
        ],
        fee_type='low',
        allow_unconfirmed=True,
        shuffle_outputs=True,
        change_address=sending_address
    )

    transaction = node.wallet.build_transaction(request_model)
    request_model = SendTransactionRequest(
        hex=transaction.hex
    )
    node.wallet.send_transaction(request_model)
    return True
