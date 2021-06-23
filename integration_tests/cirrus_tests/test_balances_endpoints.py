import pytest
from nodes import CirrusMinerNode
from pybitcoin.types import Money, Address


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_over_amount_at_height(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.balances.over_amount_at_height(block_height=10, amount=Money(1))
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, Address)
