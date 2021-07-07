from typing import Union
from pystratis.core.types import Address
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.collateral.responsemodels import *
from pystratis.api.collateral.requestmodels import *


class Collateral(APIRequest, metaclass=EndpointRegister):
    """Implements the collateral api endpoints."""

    route = '/api/collateral'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/joinfederation')
    def join_federation(self,
                        collateral_address: Union[Address, str],
                        collateral_wallet_name: str,
                        collateral_wallet_password: str,
                        wallet_password: str,
                        wallet_name: str,
                        wallet_account: str = 'account 0',
                        **kwargs) -> JoinFederationResponseModel:
        """Called by a miner wanting to join the federation.

        Args:
            collateral_address (Address, str): The collateral address.
            collateral_wallet_name (str): The collateral wallet name.
            collateral_wallet_password (SecretStr): The collateral wallet password.
            wallet_password (SecretStr): The wallet password.
            wallet_name (str): The wallet name.
            wallet_account (str, optional):  The wallet account. Default='account 0'.
            **kwargs: Extra keyword arguments. 

        Returns:
            JoinFederationResponseModel: The response to the join-federation API request.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(collateral_address, str):
            collateral_address = Address(address=collateral_address, network=self._network)
        request_model = JoinFederationRequest(
            collateral_address=collateral_address,
            collateral_wallet_name=collateral_wallet_name,
            collateral_wallet_password=collateral_wallet_password,
            wallet_password=wallet_password,
            wallet_name=wallet_name,
            wallet_account=wallet_account
        )
        data = self.post(request_model, **kwargs)

        return JoinFederationResponseModel(**data)
