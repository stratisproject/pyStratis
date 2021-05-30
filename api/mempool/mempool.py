from typing import List
from api import APIRequest, EndpointRegister, endpoint


class Mempool(APIRequest, metaclass=EndpointRegister):
    route = '/api/mempool'

    def __init__(self, **kwargs):
        super(Mempool, self).__init__(**kwargs)

    @endpoint(f'{route}/getrawmempool')
    def get_raw_mempool(self, **kwargs) -> List[str]:
        """Gets a list of transaction hashes in the mempool.

        Args:
            **kwargs:

        Returns:
            List[str]

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return data
