from typing import Optional, List
from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import Address


class SweepRequest(Model):
    """A SweepRequest."""
    private_keys: List[str] = Field(alias='privateKeys')
    destination_address: Address = Field(alias='destinationAddress')
    broadcast: Optional[bool] = False
