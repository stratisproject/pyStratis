from pydantic import Field
from pybitcoin import Model


class AccountAddressesRequest(Model):
    """An AccountAddressesRequest model."""
    wallet_name: str = Field(alias='walletName')
