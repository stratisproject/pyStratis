import pytest
from typing import Union
from pystratis.api import APIError
from pystratis.nodes import StraxNode, CirrusNode
from pystratis.core.types import uint256
from pystratis.api.blockstore.responsemodels import BlockTransactionDetailsModel


@pytest.mark.mainnet_test
@pytest.mark.integration_test
def test_walk_strax_main():
    """Retrieves every 10th block on StraxMain, confirms blockheader model, and confirms block model transactions match decoded transactions.

    Requires running node on StraxMain.
    """
    node = StraxNode()
    check_basic_api_functions(node)
    current_block_height = node.blockstore.get_block_count()
    for i in range(1, current_block_height, 10):
        check_block_and_transactions(node=node, height=i)


@pytest.mark.mainnet_test
@pytest.mark.integration_test
def test_walk_cirrus_main():
    """Retrieves every 10th block on CirrusMain, confirms blockheader model, and confirms block model transactions match decoded transactions.

    Requires running node on CirrusMain.
    """
    node = CirrusNode()
    check_basic_api_functions(node)
    current_block_height = node.blockstore.get_block_count()
    for i in range(1, current_block_height, 10):
        check_block_and_transactions(node=node, height=i)


def check_basic_api_functions(node: Union[StraxNode, CirrusNode]):
    """Calls API endpoints and checks response models for the specified functions."""
    assert isinstance(node, StraxNode) or isinstance(node, CirrusNode)
    node.node.status()
    node.node.async_loops()
    node.node.log_rules()
    node.connection_manager.getpeerinfo()
    node.consensus.deployment_flags()
    try:
        node.diagnostic.get_connectedpeers_info()
    except APIError:
        # Thrown if diagnostic route is not active on the current node.
        pass
    try:
        node.signalr.get_connection_info()
    except APIError:
        # Thrown if signalr route is not active on the current node.
        pass


def check_block_and_transactions(node: Union[StraxNode, CirrusNode], height: int):
    """Validates that the API can process each block and associated transactions."""
    assert isinstance(node, StraxNode) or isinstance(node, CirrusNode)
    block_hash_at_height: uint256 = node.consensus.get_blockhash(height=height)

    # Check block header retreival.
    node.node.get_blockheader(block_hash=block_hash_at_height)

    # Get the associated block model.
    block: BlockTransactionDetailsModel = node.blockstore.block(block_hash=block_hash_at_height)

    # Limit to 3 txids in txout_proof request to avoid 414 error.
    node.node.get_txout_proof(txids=[x.txid for x in block.transactions][:3], block_hash=block_hash_at_height)

    for j, trx in enumerate(block.transactions):
        raw_transaction = node.node.decode_raw_transaction(raw_hex=trx.hex)
        assert block.transactions[j] == raw_transaction
