from typing import Union, List
from decimal import Decimal
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.balances.requestmodels import *
from pystratis.core.types import Address, Money


class Balances(APIRequest, metaclass=EndpointRegister):
    """Implements the balances api endpoints."""

    route = '/api/balances'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/over-amount-at-height')
    def over_amount_at_height(self,
                              block_height: int,
                              amount: Union[Money, int, float, Decimal],
                              **kwargs) -> List[Address]:
        """Returns a list of addresses with balance over specified amount at the given chain height.

        Args:
            block_height (int): The specified chain height.
            amount (Money, int, float, Decimal): The specified amount in coin units.

        Returns:
            List[Address]: A list of addresses meeting the criteria.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = OverAmountAtHeightRequest(block_height=block_height, amount=Money(amount))
        data = self.get(request_model, **kwargs)
        return [Address(address=item, network=self._network) for item in data]
