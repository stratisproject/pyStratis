from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import Address


class VerifyMessageRequest(Model):
    """A request model used for the /wallet/verifymessage endpoint.

    Args:
        signature (str): The signature is to be verified.
        external_address (Address): The address of the signer.
        message (str): The message that was signed.
    """
    signature: str
    external_address: Address = Field(alias='externalAddress')
    message: str
