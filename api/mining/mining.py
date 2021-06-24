from api import APIRequest, EndpointRegister, endpoint
from api.mining.requestmodels import *
from api.mining.responsemodels import *


class Mining(APIRequest, metaclass=EndpointRegister):
    route = '/api/mining'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/generate')
    def generate(self, block_count: int, **kwargs) -> GenerateBlocksModel:
        """Generate blocks by mining.

        Args:
            block_count (int): The number of blocks to mine.
            **kwargs:

        Returns:
            GenerateBlocksModel

        Raises:
            APIError
        """
        request_model = GenerateRequest(block_count=block_count)
        data = self.post(request_model, **kwargs)
        return GenerateBlocksModel(**data)

    @endpoint(f'{route}/stopmining')
    def stop_mining(self, **kwargs) -> None:
        """Stop mining.

        Args:
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        request_model = StopMiningRequest()
        self.post(request_model, **kwargs)
