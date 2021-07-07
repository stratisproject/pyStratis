from typing import Union
from pystratis.api.notifications.requestmodels import *
from pystratis.core.types import uint256
from pystratis.api import APIRequest, EndpointRegister, endpoint


class Notifications(APIRequest, metaclass=EndpointRegister):
    """Implements the notifications api endpoints."""

    route = '/api/notifications'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/sync')
    def sync(self, sync_from: Union[uint256, str], **kwargs) -> None:
        """Begin synchronizing the chain from the provided block height or block hash.

        Args:
            sync_from (uint256, str): The block hash to start syncing at.
            **kwargs: Extra keyword arguments. 

        Returns:
            None

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(sync_from, str):
            sync_from = uint256(sync_from)
        request_model = SyncRequest(sync_from=sync_from)
        self.get(request_model, **kwargs)
