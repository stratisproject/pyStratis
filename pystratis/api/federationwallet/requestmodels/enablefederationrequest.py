from typing import Optional
from pydantic import Field, SecretStr, conint
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class EnableFederationRequest(Model):
    """A request model for the federationwallet/enable-federation endpoint.

    Args:
        mnemonic (str): The mnemonic.
        password (SecretStr): The password.
        passphrase (SecretStr, optional): The passphrase.
        timeout_seconds (conint(ge=0)): Seconds to timeout.
    """
    mnemonic: str
    password: SecretStr
    passphrase: Optional[SecretStr]
    timeout_seconds: conint(ge=0) = Field(alias='timeoutSeconds')
