import pytest
import time
from pybitcoin.types import Money, uint256
from nodes import CirrusNode, CirrusMinerNode


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_raw_mempool(cirrusminer_node: CirrusMinerNode,
                     cirrus_syncing_node: CirrusNode,
                     send_a_transaction,
                     wait_x_blocks_and_sync,
                     get_node_address_with_balance,
                     get_node_unused_address):
    wait_x_blocks_and_sync(1)
    mining_address = get_node_address_with_balance(cirrusminer_node)
    receiving_address = get_node_unused_address(cirrus_syncing_node)
    assert send_a_transaction(
        node=cirrusminer_node, sending_address=mining_address,
        receiving_address=receiving_address, amount_to_send=Money(1)
    )
    response = cirrusminer_node.mempool.get_raw_mempool()
    time.sleep(1)
    assert len(response) == 1
    for item in response:
        assert isinstance(item, uint256)

    sending_address = get_node_address_with_balance(cirrus_syncing_node)
    receiving_address = get_node_unused_address(cirrusminer_node)
    assert send_a_transaction(
        node=cirrus_syncing_node, sending_address=sending_address,
        receiving_address=receiving_address, amount_to_send=Money(1)
    )
    response = cirrus_syncing_node.mempool.get_raw_mempool()
    time.sleep(1)
    assert len(response) == 1
    for item in response:
        assert isinstance(item, uint256)
