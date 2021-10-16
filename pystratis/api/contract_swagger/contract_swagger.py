from typing import Union
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.contract_swagger.requestmodels import *
from pystratis.api.contract_swagger.responsemodels import *
from pystratis.core.types import Address


class ContractSwagger(APIRequest, metaclass=EndpointRegister):
    """Implements the connectionmanager api endpoints."""

    route = '/swagger/contracts'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/{{address}}')
    def address(self, address: Union[Address, str], **kwargs) -> OpenAPISchemaModel:
        """Dynamically generates a swagger document for the contract at the given address.

        Args:
            address (str, Address): The smart contract address.
            **kwargs: Extra keyword arguments.

        Returns:
            OpenAPISchemaModel: The swagger/OpenAPI schema for the smart contract.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(address, str):
            address = Address(address=address, network=self._network)
        kwargs['endpoint'] = kwargs['endpoint'].replace('{address}', f'{address}')
        data = self.get(**kwargs)
        data['paths'] = OpenAPIEndpointsModel(data['paths'])
        return OpenAPISchemaModel(**data)

    @endpoint(f'{route}')
    def __call__(self, address: Union[Address, str], **kwargs) -> None:
        """Add the contract address to the Swagger dropdown.

        Args:
            address (Address, str): The smart contract address.
            **kwargs: Extra keyword arguments.

        Returns:
            None

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = str(address)
        self.post(request_model, **kwargs)
