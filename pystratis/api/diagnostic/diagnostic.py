from typing import List
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.diagnostic.requestmodels import *
from pystratis.api.diagnostic.responsemodels import *


class Diagnostic(APIRequest, metaclass=EndpointRegister):
    """Implements the diagnostic api endpoints."""

    route = '/api/diagnostic'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/getconnectedpeersinfo')
    def get_connectedpeers_info(self, **kwargs) -> GetConnectedPeersInfoModel:
        """Get connected peers info.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            GetConnectedPeersInfoModel: Information on connected peers.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)

        return GetConnectedPeersInfoModel(**data)

    @endpoint(f'{route}/getstatus')
    def get_status(self, **kwargs) -> GetStatusModel:
        """Get the diagnostic feature status.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            GetStatusModel: The feature status.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return GetStatusModel(**data)

    @endpoint(f'{route}/getpeerstatistics')
    def get_peer_statistics(self, connected_only: bool, **kwargs) -> List[PeerStatisticsModel]:
        """Gets statistics for connected peers.

        Args:
            connected_only (bool): To show data for only connected nodes.
            **kwargs: Extra keyword arguments. 

        Returns:
            List[PeerStatisticsModel]: A list of statistics on the connected peers.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = GetPeerStatisticsRequest(connected_only=connected_only)
        data = self.get(request_model, **kwargs)
        return [PeerStatisticsModel(**x) for x in data]

    @endpoint(f'{route}/startcollectingpeerstatistics')
    def start_collecting_peerstatistics(self, **kwargs) -> str:
        """Start collecting peer statistics.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            str: The status of the feature.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return data

    @endpoint(f'{route}/stopcollectingpeerstatistics')
    def stop_collecting_peerstatistics(self, **kwargs) -> str:
        """Stop collecting peer statistics.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            str: The status of the feature.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return data
