from typing import Optional
from pydantic import Field, SecretStr, conint
from pybitcoin import Model


class EnableFederationRequest(Model):
    """A EnableFederationRequest."""
    mnemonic: str
    password: SecretStr
    passphrase: Optional[SecretStr]
    timeout_seconds: conint(ge=0) = Field(alias='timeoutSeconds')
