from api import APIRequest, EndpointRegister, endpoint
from api.staking.requestmodels import *
from api.staking.responsemodels import *


class Staking(APIRequest, metaclass=EndpointRegister):
    route = '/api/staking'

    def __init__(self, **kwargs):
        super(Staking, self).__init__(**kwargs)

    @endpoint(f'{route}/getstakinginfo')
    def get_staking_info(self, **kwargs) -> GetStakingInfoModel:
        """Gets current staking information.

        Args:
            **kwargs:

        Returns:
            GetStakingInfoModel

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return GetStakingInfoModel(**data)

    @endpoint(f'{route}/startstaking')
    def start_staking(self, request_model: StartStakingRequest, **kwargs) -> None:
        """Start staking

        Args:
            request_model: StartStakingRequest model
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/startmultistaking')
    def start_multistaking(self, request_model: StartMultiStakingRequest, **kwargs) -> None:
        """Start staking for multiple wallets simultaneously

        Args:
            request_model: StartMultiStakingRequest model
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        self.get(request_model, **kwargs)

    @endpoint(f'{route}/stopstaking')
    def stop_staking(self, request_model: StopStakingRequest = StopStakingRequest(), **kwargs) -> None:
        """Stop staking.

        Args:
            request_model: StopStakingRequest model
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        self.get(request_model, **kwargs)
