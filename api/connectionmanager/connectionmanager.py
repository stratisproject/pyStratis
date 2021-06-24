from typing import List
from api import APIRequest, EndpointRegister, endpoint
from api.connectionmanager.requestmodels import *
from api.connectionmanager.responsemodels import *


class ConnectionManager(APIRequest, metaclass=EndpointRegister):
    route = '/api/connectionmanager'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/addnode')
    def addnode(self, endpoint: str, command: str, **kwargs) -> bool:
        """

        Args:
            endpoint (str): The endpoint.
            command (str): Allowed commands [add, remove, onetry]
            **kwargs:

        Returns:
            bool

        Raises:
            APIError
        """
        request_model = AddNodeRequest(endpoint=endpoint, command=command)
        data = self.get(request_model, **kwargs)

        return data

    @endpoint(f'{route}/getpeerinfo')
    def getpeerinfo(self, **kwargs) -> List[PeerInfoModel]:
        """Gets the peer info.

        Args:
            **kwargs:

        Returns:
            List[PeerInfoModel]

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return [PeerInfoModel(**x) for x in data]
