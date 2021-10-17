from typing import List
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.core.types import Money


class ExternalAPI(APIRequest, metaclass=EndpointRegister):
    """Implements the federation api endpoints."""

    route = '/api/externalapi'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/estimateconversiongas')
    def estimate_conversion_gas(self, **kwargs) -> int:
        """Returns an estimate of conversion gas fees.

        Args:
            **kwargs: Extra keyword arguments.

        Returns:
            int: The conversion gas fee estimate.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        if isinstance(data, float):
            data = int(data)
        return data

    @endpoint(f'{route}/estimateconversionfee')
    def estimate_conversion_fee(self, **kwargs) -> Money:
        """Returns an estimate of conversion fees.

        Args:
            **kwargs: Extra keyword arguments.

        Returns:
            Money: The conversion fee estimate in Strax

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return Money(data)

    @endpoint(f'{route}/gasprice')
    def gas_price(self, **kwargs) -> int:
        """Returns the current ETH gas price.

        Args:
            **kwargs: Extra keyword arguments.

        Returns:
            int: The ETH gas price.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return data

    @endpoint(f'{route}/ethereumprice')
    def ethereum_price(self, **kwargs) -> Money:
        """Returns the current ETH price in USD.

        Args:
            **kwargs: Extra keyword arguments.

        Returns:
            Money: The current ETH/USD price.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return Money(data)

    @endpoint(f'{route}/stratisprice')
    def stratis_price(self, **kwargs) -> Money:
        """Returns the current STRAX price in USD.

        Args:
            **kwargs: Extra keyword arguments.

        Returns:
            Money: The current STRAX/USD price.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return Money(data)
