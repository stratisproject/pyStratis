from typing import Optional
from pydantic import Field, SecretStr, conint
from pybitcoin import Model


class EnableFederationRequest(Model):
    """A EnableFederationRequest."""
    mnemonic: Optional[str]
    password: SecretStr
    passphrase: SecretStr
    timeout_seconds: conint(ge=0) = Field(alias='timeoutSeconds')
