from pydantic import SecretStr
from pybitcoin import Model


class StartStakingRequest(Model):
    """A StartStakingRequest."""
    name: str
    password: SecretStr
