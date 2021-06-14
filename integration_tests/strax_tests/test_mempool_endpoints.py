import pytest
import time
from pybitcoin.types import Money, uint256
from nodes import BaseNode


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_raw_mempool(hot_node: BaseNode, syncing_node: BaseNode, send_a_transaction,
                     get_node_address_with_balance, get_node_unused_address):
    mining_address = get_node_address_with_balance(hot_node)
    receiving_address = get_node_unused_address(syncing_node)
    assert send_a_transaction(
        node=hot_node, sending_address=mining_address,
        receiving_address=receiving_address, amount=Money(1)
    )
    response = hot_node.mempool.get_raw_mempool()
    time.sleep(5)
    assert len(response) == 1
    for item in response:
        assert isinstance(item, uint256)
