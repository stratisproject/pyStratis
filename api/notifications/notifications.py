from api import APIRequest, EndpointRegister, endpoint
from api.notifications.requestmodels import *


class Notifications(APIRequest, metaclass=EndpointRegister):
    route = '/api/notifications'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/sync')
    def sync(self, request_model: SyncRequest, **kwargs) -> None:
        """Begin synchronizing the chain from the provided block height or block hash.

        Args:
            request_model: SyncRequest model
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        self.get(request_model, **kwargs)
