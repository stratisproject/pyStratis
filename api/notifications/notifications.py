from typing import Union
from pybitcoin.types import uint256
from api import APIRequest, EndpointRegister, endpoint
from api.notifications.requestmodels import *


class Notifications(APIRequest, metaclass=EndpointRegister):
    route = '/api/notifications'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/sync')
    def sync(self, sync_from: Union[uint256, str], **kwargs) -> None:
        """Begin synchronizing the chain from the provided block height or block hash.

        Args:
            sync_from (uint256 | str): The block hash to start syncing at.
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        if isinstance(sync_from, str):
            sync_from = uint256(sync_from)
        request_model = SyncRequest(sync_from=sync_from)
        self.get(request_model, **kwargs)
