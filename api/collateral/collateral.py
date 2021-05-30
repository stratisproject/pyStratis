from api import APIRequest, EndpointRegister, endpoint
from api.collateral.requestmodels import *
from api.collateral.responsemodels import *


class Collateral(APIRequest, metaclass=EndpointRegister):
    route = '/api/collateral'

    def __init__(self, **kwargs):
        super(Collateral, self).__init__(**kwargs)

    @endpoint(f'{route}/joinfederation')
    def join_federation(self, request_model: JoinFederationRequest, **kwargs) -> JoinFederationResponseModel:
        """Called by a miner wanting to join the federation.

        Args:
            request_model: A joinfederationrequest model.
            **kwargs:

        Returns:
            JoinFederationResponseModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return JoinFederationResponseModel(**data)
