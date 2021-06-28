import pytest
from nodes import BaseNode, StraxNode, CirrusNode
from pybitcoin.types import uint256
from api.node.responsemodels import BlockHeaderModel
from api.blockstore.responsemodels import BlockTransactionDetailsModel


@pytest.mark.mainnet_test
@pytest.mark.integration_test
def test_walk_strax_main():
    """Retrieves every 10th block on StraxMain, confirms blockheader model, and confirms block model transactions match decoded transactions.

    Requires running node on StraxMain.
    """
    node = StraxNode()
    current_block_height = node.blockstore.get_block_count()
    for i in range(1, current_block_height, 10):
        print(f'Checking height {i}')
        block_hash_at_height: uint256 = node.consensus.get_blockhash(height=i)
        node.node.get_blockheader(block_hash=block_hash_at_height)
        block: BlockTransactionDetailsModel = node.blockstore.block(block_hash=block_hash_at_height)
        for j, trx in enumerate(block.transactions):
            raw_transaction = node.node.decode_raw_transaction(raw_hex=trx.hex)
            assert block.transactions[j] == raw_transaction


@pytest.mark.mainnet_test
@pytest.mark.integration_test
def test_walk_cirrus_main():
    """Retrieves every 10th block on CirrusMain, confirms blockheader model, and confirms block model transactions match decoded transactions.

    Requires running node on CirrusMain.
    """
    node = CirrusNode()
    current_block_height = node.blockstore.get_block_count()
    for i in range(1, current_block_height, 10):
        print(f'Checking height {i}')
        block_hash_at_height: uint256 = node.consensus.get_blockhash(height=i)
        node.node.get_blockheader(block_hash=block_hash_at_height)
        block: BlockTransactionDetailsModel = node.blockstore.block(block_hash=block_hash_at_height)
        for j, trx in enumerate(block.transactions):
            raw_transaction = node.node.decode_raw_transaction(raw_hex=trx.hex)
            assert block.transactions[j] == raw_transaction
