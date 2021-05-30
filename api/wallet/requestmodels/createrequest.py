from typing import Optional
from pydantic import SecretStr
from pybitcoin import Model


class CreateRequest(Model):
    """A CreateRequest."""
    mnemonic: Optional[str]
    password: SecretStr
    passphrase: SecretStr
    name: str
