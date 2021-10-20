from typing import List
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.federation.responsemodels import *
from pystratis.api.federation.requestmodels import *
from pystratis.core import PubKey
from pystratis.core.types import Address


class Federation(APIRequest, metaclass=EndpointRegister):
    """Implements the federation api endpoints."""

    route = '/api/federation'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/reconstruct')
    def reconstruct(self, **kwargs) -> str:
        """Signals the node to rebuild the federation. Will need to restart node when complete.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            str: The node response ot the request.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.put(**kwargs)
        return data

    @endpoint(f'{route}/members/current')
    def members_current(self, **kwargs) -> FederationMemberDetailedModel:
        """Retrieves the information for the current federation member's voting status and mining estimates.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            FederationMemberDetailedModel: Information on the current member.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        if data['miningStats']['miningAddress'] is not None:
            data['miningStats']['miningAddress'] = Address(address=data['miningStats']['miningAddress'], network=self._network)
        data['miningStats'] = MiningStats(**data['miningStats'])
        return FederationMemberDetailedModel(**data)

    @endpoint(f'{route}/members')
    def members(self, **kwargs) -> List[FederationMemberModel]:
        """Retrieves a list of active federation members and last active times.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            List[FederationMemberModel]: Information on each of federation members.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return [FederationMemberModel(**x) for x in data]

    @endpoint(f'{route}/mineratheight')
    def miner_at_height(self, block_height: int, **kwargs) -> PubKey:
        """Gets the federation pubkey that mined the block at the specified height.

        Args:
            block_height: The height to query
            **kwargs:

        Returns:
            PubKey: The pubkey that produced the block at the specified height.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = AtHeightRequest(block_height=block_height)
        data = self.get(request_model, **kwargs)
        return PubKey(data)

    @endpoint(f'{route}/federationatheight')
    def federation_at_height(self, block_height: int, **kwargs) -> List[PubKey]:
        """Gets the federation membership at the specified height.

        Args:
            block_height: The height to query
            **kwargs:

        Returns:
            List[PubKey]: The pubkeys of federation members at the specified height.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = AtHeightRequest(block_height=block_height)
        data = self.get(request_model, **kwargs)
        return [PubKey(x) for x in data]
