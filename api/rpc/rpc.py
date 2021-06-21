from typing import List
from api import APIRequest, EndpointRegister, endpoint
from api.rpc.requestmodels import *
from api.rpc.responsemodels import *


class RPC(APIRequest, metaclass=EndpointRegister):
    route = '/api/rpc'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/callbyname')
    def call_by_name(self, request_model: CallByNameRequest, **kwargs) -> RPCCommandResponseModel:
        """Calls the specified RPC command.

        Args:
            request_model: CallByNameRequest model
            **kwargs:

        Returns:
            The RPCCommandResponse

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return RPCCommandResponseModel(**data)

    @endpoint(f'{route}/listmethods')
    def list_methods(self, **kwargs) -> List[RPCCommandListModel]:
        """List available RPC call methods on this node.

        Args:
            **kwargs:

        Returns:
            List[RPCCommandListModel]

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return [RPCCommandListModel(**x) for x in data]
