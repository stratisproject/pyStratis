from typing import List
from api import APIRequest, EndpointRegister, endpoint
from api.federation.responsemodels import *


class Federation(APIRequest, metaclass=EndpointRegister):
    route = '/api/federation'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/reconstruct')
    def reconstruct(self, **kwargs) -> str:
        """Signals the node to rebuild the federation. Will need to restart node when complete.

        Args:
            **kwargs:

        Returns:
            str

        Raises:
            APIError
        """
        data = self.put(**kwargs)
        return data

    @endpoint(f'{route}/members/current')
    def members_current(self, **kwargs) -> FederationMemberDetailedModel:
        """Retrieves the information for the current federation member's voting status and mining estimates.

        Args:
            **kwargs:

        Returns:
            FederationMemberDetailedModel

        Raises:
            APIError
        """
        data = self.get(**kwargs)
        return FederationMemberDetailedModel(**data)

    @endpoint(f'{route}/members')
    def members(self, **kwargs) -> List[FederationMemberModel]:
        """Retrieves a list of active federation members and last active times.

        Args:
            **kwargs:

        Returns:
            List[FederationMemberModel]

        Raises:
            APIError
        """
        data = self.get(**kwargs)
        return [FederationMemberModel(**x) for x in data]
