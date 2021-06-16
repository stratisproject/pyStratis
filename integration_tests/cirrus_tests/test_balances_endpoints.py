import pytest
from nodes import CirrusNode, CirrusMinerNode
from api.balances.requestmodels import *
from pybitcoin.types import Money, Address


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_over_amount_at_height(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = OverAmountAtHeightRequest(
        block_height=1,
        amount=Money(5)
    )
    response = cirrusminer_node.balances.over_amount_at_height(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, Address)

    response = cirrus_syncing_node.balances.over_amount_at_height(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, Address)
