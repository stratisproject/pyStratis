from typing import Optional
from pydantic import SecretStr, Field
from pybitcoin import Model


class RecoverRequest(Model):
    """A RecoverRequest."""
    mnemonic: str
    password: SecretStr
    passphrase: SecretStr
    name: str
    creation_date: Optional[str] = Field(default=None, alias='creationDate')
