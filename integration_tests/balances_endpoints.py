from typing import Union
from nodes import CirrusNode, InterfluxCirrusNode
from api.balances.requestmodels import *
from pybitcoin.types import Money


def check_balances_endpoints(node: Union[CirrusNode, InterfluxCirrusNode]) -> None:
    assert check_over_amount_at_height(node)


def check_over_amount_at_height(node: Union[CirrusNode, InterfluxCirrusNode]) -> bool:
    request_model = OverAmountAtHeightRequest(
        block_height=1,
        amount=Money(5)
    )
    node.balances.over_amount_at_height(request_model)
    return True
