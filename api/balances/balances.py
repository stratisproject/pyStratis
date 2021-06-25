from typing import Union, List
from decimal import Decimal
from api import APIRequest, EndpointRegister, endpoint
from api.balances.requestmodels import *
from pybitcoin.types import Address, Money


class Balances(APIRequest, metaclass=EndpointRegister):
    """Implements the stratis balances api endpoints"""
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
            amount (Money | int | float | Decimal): The specified amount in coin units.

        Returns:
            List[Address]

        Raises:
            APIError
        """
        request_model = OverAmountAtHeightRequest(block_height=block_height, amount=Money(amount))
        data = self.get(request_model, **kwargs)
        return [Address(address=item, network=self._network) for item in data]
