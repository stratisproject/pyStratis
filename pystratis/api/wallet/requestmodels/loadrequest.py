from pydantic import SecretStr
from pystratis.api import Model


class LoadRequest(Model):
    """A request model for the wallet/load endpoint.

    Args:
        name (str): The wallet name to load.
        password (str): The wallet password.
    """
    name: str
    password: SecretStr
