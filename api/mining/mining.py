from api import APIRequest, EndpointRegister, endpoint
from api.mining.requestmodels import *
from api.mining.responsemodels import *


class Mining(APIRequest, metaclass=EndpointRegister):
    route = '/api/mining'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/generate')
    def generate(self, request_model: GenerateRequest, **kwargs) -> GenerateBlocksModel:
        """Generate blocks by mining.

        Args:
            request_model: A GenerateRequest model.
            **kwargs:

        Returns:
            GenerateBlocksModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return GenerateBlocksModel(**data)

    @endpoint(f'{route}/stopmining')
    def stop_mining(self, request_model: StopMiningRequest = StopMiningRequest(), **kwargs) -> None:
        """Stop mining.

        Args:
            request_model: A StopMiningRequest model.
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        self.post(request_model, **kwargs)
