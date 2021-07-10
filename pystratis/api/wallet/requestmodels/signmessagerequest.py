from pydantic import SecretStr, Field
from pystratis.api import Model
from pystratis.core.types import Address


# noinspection PyUnresolvedReferences
class SignMessageRequest(Model):
    """A request model used for /wallet/signmessage endpoint.

    Args:
        wallet_name (str): The name of the wallet to sign message with.
        password (str): The password of the wallet to sign message with.
        external_address (Address): The external address of a private key used to sign message.
        message (str): The message to be signed.
    """
    wallet_name: str = Field(alias='walletName')
    password: SecretStr
    external_address: Address = Field(alias='externalAddress')
    message: str
