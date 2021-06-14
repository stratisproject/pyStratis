from typing import List
from api import APIRequest, EndpointRegister, endpoint
from pybitcoin.types import uint256


class Mempool(APIRequest, metaclass=EndpointRegister):
    route = '/api/mempool'

    def __init__(self, **kwargs):
        super(Mempool, self).__init__(**kwargs)

    @endpoint(f'{route}/getrawmempool')
    def get_raw_mempool(self, **kwargs) -> List[uint256]:
        """Gets a list of transaction hashes in the mempool.

        Args:
            **kwargs:

        Returns:
            List[uint256]

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return [uint256(x) for x in data]
