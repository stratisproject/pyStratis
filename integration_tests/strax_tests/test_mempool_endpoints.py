import pytest
from pybitcoin.types import Money, uint256
from nodes import BaseNode


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_raw_mempool(strax_hot_node: BaseNode, strax_syncing_node: BaseNode, send_a_transaction,
                     get_node_address_with_balance, get_node_unused_address):
    mining_address = get_node_address_with_balance(strax_hot_node)
    receiving_address = get_node_unused_address(strax_syncing_node)
    assert send_a_transaction(
        node=strax_hot_node, sending_address=mining_address,
        receiving_address=receiving_address, amount_to_send=Money(1)
    )
    response = strax_hot_node.mempool.get_raw_mempool()
    for item in response:
        assert isinstance(item, uint256)
