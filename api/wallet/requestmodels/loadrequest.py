from pydantic import SecretStr, Field
from pybitcoin import Model


class LoadRequest(Model):
    """A LoadRequest."""
    name: str = Field(alias='name')
    password: SecretStr
