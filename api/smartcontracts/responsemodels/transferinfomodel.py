from typing import Optional
from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import Address, Money


class TransferInfoModel(Model):
    """A TransferInfoModel."""
    from_address: Optional[Address] = Field(alias='from')
    to_address: Optional[Address] = Field(alias='to')
    value: Optional[Money]
