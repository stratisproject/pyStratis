from typing import List
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.rpc.requestmodels import *
from pystratis.api.rpc.responsemodels import *


class RPC(APIRequest, metaclass=EndpointRegister):
    """Implements the rpc api endpoints."""

    route = '/api/rpc'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/callbyname')
    def call_by_name(self, command: str, **kwargs) -> RPCCommandResponseModel:
        """Calls the specified RPC command.

        Args:
            command (str): The complete RPC command.
            **kwargs: Extra keyword arguments. 

        Returns:
            The RPCCommandResponse: The command output.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = CallByNameRequest(command=command)
        data = self.post(request_model, **kwargs)
        return RPCCommandResponseModel(**data)

    @endpoint(f'{route}/listmethods')
    def list_methods(self, **kwargs) -> List[RPCCommandListModel]:
        """List available RPC call methods on this node.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            List[RPCCommandListModel]: A list of valid RPC commands.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return [RPCCommandListModel(**x) for x in data]
