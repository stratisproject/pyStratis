from typing import List
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.staking.requestmodels import *
from pystratis.api.staking.responsemodels import *
from pystratis.core import WalletSecret


class Staking(APIRequest, metaclass=EndpointRegister):
    """Implements the staking api endpoints."""

    route = '/api/staking'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/getstakinginfo')
    def get_staking_info(self, **kwargs) -> GetStakingInfoModel:
        """Gets current staking information.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            GetStakingInfoModel: Information about current staking status.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return GetStakingInfoModel(**data)

    @endpoint(f'{route}/startstaking')
    def start_staking(self,
                      name: str,
                      password: str,
                      **kwargs) -> None:
        """Start staking

        Args:
            name (str): The wallet name.
            password (str): The wallet password.
            **kwargs: Extra keyword arguments. 

        Returns:
            None

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = StartStakingRequest(name=name, password=password)
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/startmultistaking')
    def start_multistaking(self,
                           wallet_credentials: List[WalletSecret],
                           **kwargs) -> None:
        """Start staking for multiple wallets simultaneously

        Args:
            wallet_credentials (List[WalletSecret]): A list of wallet credentials to launch staking of multiple wallets with one command.
            **kwargs: Extra keyword arguments. 

        Returns:
            None

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = StartMultiStakingRequest(wallet_credentials=wallet_credentials)
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/stopstaking')
    def stop_staking(self, **kwargs) -> None:
        """Stop staking.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            None

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = StopStakingRequest()
        self.post(request_model, **kwargs)
