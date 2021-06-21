from typing import List
from api import APIRequest, EndpointRegister, endpoint
from api.diagnostic.requestmodels import *
from api.diagnostic.responsemodels import *


class Diagnostic(APIRequest, metaclass=EndpointRegister):
    route = '/api/diagnostic'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/getconnectedpeersinfo')
    def get_connectedpeers_info(self, **kwargs) -> GetConnectedPeersInfoModel:
        """Get connected peers info.

        Args:
            **kwargs:

        Returns:
            GetConnectedPeersInfoModel

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return GetConnectedPeersInfoModel(**data)

    @endpoint(f'{route}/getstatus')
    def get_status(self, **kwargs) -> GetStatusModel:
        """Get the diagnostic feature status.

        Args:
            **kwargs:

        Returns:
            GetStatusModel

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return GetStatusModel(**data)

    @endpoint(f'{route}/getpeerstatistics')
    def get_peer_statistics(self, request_model: GetPeerStatisticsRequest, **kwargs) -> List[PeerStatisticsModel]:
        """Gets statistics for connected peers.

        Args:
            request_model: A GetPeerStatisticsRequest model.
            **kwargs:

        Returns:
            List[PeerStatisticsModel]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return [PeerStatisticsModel(**x) for x in data]

    @endpoint(f'{route}/startcollectingpeerstatistics')
    def start_collecting_peerstatistics(self, **kwargs) -> str:
        """Start collecting peer statistics.

        Args:
            **kwargs:

        Returns:
            str

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return data

    @endpoint(f'{route}/stopcollectingpeerstatistics')
    def stop_collecting_peerstatistics(self, **kwargs) -> str:
        """Stop collecting peer statistics.

        Args:
            **kwargs:

        Returns:
            str

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return data
