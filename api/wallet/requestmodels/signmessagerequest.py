from pydantic import SecretStr, Field
from pybitcoin import Address, Model


class SignMessageRequest(Model):
    """A SignMessageRequest."""
    wallet_name: str = Field(alias='walletName')
    password: SecretStr
    external_address: Address = Field(alias='externalAddress')
    message: str
