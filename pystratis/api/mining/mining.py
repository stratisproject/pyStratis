from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.mining.requestmodels import *
from pystratis.api.mining.responsemodels import *


class Mining(APIRequest, metaclass=EndpointRegister):
    """Implements the mining api endpoints."""

    route = '/api/mining'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/generate')
    def generate(self, block_count: int, **kwargs) -> GenerateBlocksModel:
        """Generate blocks by mining.

        Args:
            block_count (int): The number of blocks to mine.
            **kwargs: Extra keyword arguments. 

        Returns:
            GenerateBlocksModel: A list of generated blocks.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = GenerateRequest(block_count=block_count)
        data = self.post(request_model, **kwargs)
        return GenerateBlocksModel(**data)

    @endpoint(f'{route}/stopmining')
    def stop_mining(self, **kwargs) -> None:
        """Stop mining.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            None

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = StopMiningRequest()
        self.post(request_model, **kwargs)
