import json
from typing import List, Union
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.rpc.requestmodels import *
from pystratis.api.rpc.responsemodels import *


class RPC(APIRequest, metaclass=EndpointRegister):
    """Implements the rpc api endpoints."""

    route = '/api/rpc'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/callbyname')
    def call_by_name(self, command: str, parameters: dict = None, **kwargs) -> Union[int, str, dict]:
        """Calls the specified RPC command.

        Args:
            command (str): The complete RPC command.
            parameters (dict, optional): Command parameters
            **kwargs: Extra keyword arguments. 

        Returns:
            Union[int, str, dict]: The command output.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = CallByNameRequest(method_name=command)
        request_model = request_model.dict(by_alias=True)
        if parameters is not None:
            request_model.update(parameters)
        data = self.post(request_model, **kwargs)
        if isinstance(data, int):
            return data
        elif isinstance(data, str):
            try:
                return json.loads(data)
            except json.decoder.JSONDecodeError:
                return data
        else:
            return data

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
