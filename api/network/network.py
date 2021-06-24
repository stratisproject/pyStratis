from typing import List
from api import APIRequest, EndpointRegister, endpoint
from api.network.requestmodels import *
from api.network.responsemodels import *


class Network(APIRequest, metaclass=EndpointRegister):
    route = '/api/network'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/disconnect')
    def disconnect(self, peer_address: str, **kwargs) -> None:
        """Disconnect from a node.

        Args:
            peer_address (str): The peer endpoint.
            **kwargs:

        Returns:
            None

        Raises:
            APIError
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
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        request_model = SetBanRequest(ban_command=ban_command, ban_duration_seconds=ban_duration_seconds, peer_address=peer_address)
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/getbans')
    def get_bans(self, **kwargs) -> List[BannedPeerModel]:
        """Get a list of banned peers.

        Args:
            **kwargs:

        Returns:
            List[BannedPeerModel]

        Raises:
            APIError
        """
        data = self.get(**kwargs)
        return [BannedPeerModel(**x) for x in data]

    @endpoint(f'{route}/clearbanned')
    def clear_banned(self, **kwargs) -> None:
        """Clear banned node list.

        Args:
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        request_model = ClearBannedRequest()
        self.post(request_model, **kwargs)
