from typing import List
from api import APIRequest, EndpointRegister, endpoint
from api.balances.requestmodels import *
from pybitcoin.types import Address


class Balances(APIRequest, metaclass=EndpointRegister):
    """Implements the stratis balances api endpoints"""
    route = '/api/balances'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/over-amount-at-height')
    def over_amount_at_height(self, request_model: OverAmountAtHeightRequest, **kwargs) -> List[Address]:
        """Returns a list of addresses with balance over specified amount at the chain height.

        Args:
            request_model: OverAmountAtHeightRequest model

        Returns:
            List[Address]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return [Address(address=item, network=self._network) for item in data]
