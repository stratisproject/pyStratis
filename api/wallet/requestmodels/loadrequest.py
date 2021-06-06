from pydantic import SecretStr
from pybitcoin import Model


class LoadRequest(Model):
    """A LoadRequest."""
    name: str
    password: SecretStr
