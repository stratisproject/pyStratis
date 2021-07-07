from typing import List
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.core.types import uint256


class Mempool(APIRequest, metaclass=EndpointRegister):
    """Implements the mempool api endpoints."""

    route = '/api/mempool'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/getrawmempool')
    def get_raw_mempool(self, **kwargs) -> List[uint256]:
        """Gets a list of transaction hashes in the mempool.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            List[uint256]: A list of transactions in the mempool.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return [uint256(x) for x in data]
