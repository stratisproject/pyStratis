from typing import List
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.network.requestmodels import *
from pystratis.api.network.responsemodels import *


class Network(APIRequest, metaclass=EndpointRegister):
    """Implements the network api endpoints."""

    route = '/api/network'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/disconnect')
    def disconnect(self, peer_address: str, **kwargs) -> None:
        """Disconnect from a node.

        Args:
            peer_address (str): The peer endpoint.
            **kwargs: Extra keyword arguments. 

        Returns:
            None

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = DisconnectPeerRequest(peer_address=peer_address)
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/setban')
    def set_ban(self,
                ban_command: str,
                ban_duration_seconds: int,
                peer_address: str,
                **kwargs) -> None:
        """Set a banned node.

        Args:
            ban_command (str): Allowed commands [add, remove].
            ban_duration_seconds (int): The ban duration in seconds.
            peer_address (str): The peer address to ban/unban.
            **kwargs: Extra keyword arguments. 

        Returns:
            None

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = SetBanRequest(ban_command=ban_command, ban_duration_seconds=ban_duration_seconds, peer_address=peer_address)
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/getbans')
    def get_bans(self, **kwargs) -> List[BannedPeerModel]:
        """Get a list of banned peers.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            List[BannedPeerModel]: A list of banned peers with information on duration and reason for ban.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return [BannedPeerModel(**x) for x in data]

    @endpoint(f'{route}/clearbanned')
    def clear_banned(self, **kwargs) -> None:
        """Clear banned node list.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            None

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = ClearBannedRequest()
        self.post(request_model, **kwargs)
