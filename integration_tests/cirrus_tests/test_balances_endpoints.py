import pytest
from nodes import CirrusNode
from api.balances.requestmodels import *
from pybitcoin.types import Money


@pytest.mark.skip(reason='WIP')
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_over_amount_at_height(cirrus_hot_node: CirrusNode) -> bool:
    request_model = OverAmountAtHeightRequest(
        block_height=1,
        amount=Money(5)
    )
    cirrus_hot_node.balances.over_amount_at_height(request_model)
    return True
