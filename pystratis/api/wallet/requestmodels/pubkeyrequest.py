from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import Address


# noinspection PyUnresolvedReferences
class PubKeyRequest(Model):
    """A request model used for /wallet/pubkey endpoint. 

    Args:
        wallet_name (str): The name of the wallet to search for pubkey in.
        external_address (Address): The external address of a wanted pubkey.
    """
    wallet_name: str = Field(alias='walletName')
    external_address: Address = Field(alias='externalAddress')
