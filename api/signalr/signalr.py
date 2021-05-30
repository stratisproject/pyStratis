from api import APIRequest, EndpointRegister, endpoint
from api.signalr.responsemodels import *


class SignalR(APIRequest, metaclass=EndpointRegister):
    route = '/api/signalr'

    def __init__(self, **kwargs):
        super(SignalR, self).__init__(**kwargs)

    @endpoint(f'{route}/getconnectioninfo')
    def get_connection_info(self, **kwargs) -> GetConnectionInfoModel:
        """Returns the signalr connection info.

        Args:
            **kwargs:

        Returns:
            GetConnectionInfoModel

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return GetConnectionInfoModel(**data)
