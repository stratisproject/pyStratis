from typing import List
from api import APIRequest, EndpointRegister, endpoint
from api.connectionmanager.requestmodels import *
from api.connectionmanager.responsemodels import *


class ConnectionManager(APIRequest, metaclass=EndpointRegister):
    route = '/api/connectionmanager'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/addnode')
    def addnode(self, request_model: AddNodeRequest, **kwargs) -> bool:
        """

        Args:
            request_model:
            **kwargs:

        Returns:
            bool

        Raises:
            APIError
        """
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
