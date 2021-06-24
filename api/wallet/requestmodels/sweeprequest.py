from typing import Optional, List
from pydantic import Field
from pybitcoin import Model, Key
from pybitcoin.types import Address


class SweepRequest(Model):
    """A request model for the wallet/sweep endpoint.

    Args:
        private_keys: List[Key] = Field(alias='privateKeys')
        destination_address: Address = Field(alias='destinationAddress')
        broadcast: Optional[bool] = False
    """
    private_keys: List[Key] = Field(alias='privateKeys')
    destination_address: Address = Field(alias='destinationAddress')
    broadcast: Optional[bool] = False
