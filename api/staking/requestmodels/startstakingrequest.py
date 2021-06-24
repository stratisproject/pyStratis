from pydantic import SecretStr
from pybitcoin import Model


class StartStakingRequest(Model):
    """A request model for the staking/startstaking endpoint.

    Args:
        name (str): The wallet name.
        password (str): The wallet password.
    """
    name: str
    password: SecretStr
