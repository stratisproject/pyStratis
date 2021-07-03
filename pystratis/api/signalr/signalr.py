from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.signalr.responsemodels import *


class SignalR(APIRequest, metaclass=EndpointRegister):
    route = '/api/signalr'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/getconnectioninfo')
    def get_connection_info(self, **kwargs) -> GetConnectionInfoModel:
        """Returns the signalr connection info.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            GetConnectionInfoModel

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return GetConnectionInfoModel(**data)
