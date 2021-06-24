from typing import List
from api import APIRequest, EndpointRegister, endpoint
from api.consensus.requestmodels import *
from api.consensus.responsemodels import *
from pybitcoin.types import uint256


class Consensus(APIRequest, metaclass=EndpointRegister):
    route = '/api/consensus'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/deploymentflags')
    def deployment_flags(self, **kwargs) -> List[DeploymentFlagsModel]:
        """Get the active deployment flags.

        Args:
            **kwargs:

        Returns:
            List[DeploymentFlagsModel]

        Raises:
            APIError
        """
        data = self.get(**kwargs)
        return [DeploymentFlagsModel(**x) for x in data]

    @endpoint(f'{route}/getbestblockhash')
    def get_best_blockhash(self, **kwargs) -> uint256:
        """Gets the best block hash.

        Args:
            **kwargs:

        Returns:
            uint256

        Raises:
            APIError
        """
        data = self.get(**kwargs)
        return uint256(data)

    @endpoint(f'{route}/getblockhash')
    def get_blockhash(self, height: int, **kwargs) -> uint256:
        """Gets the block hash at the specified block

        Args:
            height (int): The requested height for block hash retrieval.
            **kwargs:

        Returns:
            uint256

        Raises:
            APIError
        """
        request_model = GetBlockHashRequest(height=height)
        data = self.get(request_model, **kwargs)
        return uint256(data)
