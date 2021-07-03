from typing import Optional
from pydantic import Field
from pystratis.core import Model
from pystratis.core.types import Address, Money


class TransferInfoModel(Model):
    """A TransferInfoModel."""
    from_address: Optional[Address] = Field(alias='from')
    to_address: Optional[Address] = Field(alias='to')
    value: Optional[Money]
