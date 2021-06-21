from typing import List
from api import APIRequest, EndpointRegister, endpoint
from api.network.requestmodels import *
from api.network.responsemodels import *


class Network(APIRequest, metaclass=EndpointRegister):
    route = '/api/network'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/disconnect')
    def disconnect(self, request_model: DisconnectPeerRequest, **kwargs) -> None:
        """Disconnect from a node.

        Args:
            request_model: The DisconnectPeerRequest model.
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/setban')
    def set_ban(self, request_model: SetBanRequest, **kwargs) -> None:
        """Set a banned node.

        Args:
            request_model: The SetBanRequest model.
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
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
    def clear_banned(self, request_model: ClearBannedRequest = ClearBannedRequest(), **kwargs) -> None:
        """Clear banned node list.

        Args:
            request_model: The ClearBannedRequest model.
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        self.post(request_model, **kwargs)
