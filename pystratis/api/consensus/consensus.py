from typing import List
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.consensus.requestmodels import *
from pystratis.api.consensus.responsemodels import *
from pystratis.core.types import uint256


class Consensus(APIRequest, metaclass=EndpointRegister):
    """Implements the consensus api endpoints."""

    route = '/api/consensus'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/deploymentflags')
    def deployment_flags(self, **kwargs) -> List[DeploymentFlagsModel]:
        """Get the active deployment flags.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            List[DeploymentFlagsModel]: A list of active deployment flags..

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return [DeploymentFlagsModel(**x) for x in data]

    @endpoint(f'{route}/getbestblockhash')
    def get_best_blockhash(self, **kwargs) -> uint256:
        """Gets the best block hash.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            uint256: The block hash.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return uint256(data)

    @endpoint(f'{route}/getblockhash')
    def get_blockhash(self, height: int, **kwargs) -> uint256:
        """Gets the block hash at the specified block

        Args:
            height (int): The requested height for block hash retrieval.
            **kwargs: Extra keyword arguments. 

        Returns:
            uint256: The block hash.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = GetBlockHashRequest(height=height)
        data = self.get(request_model, **kwargs)
        return uint256(data)
