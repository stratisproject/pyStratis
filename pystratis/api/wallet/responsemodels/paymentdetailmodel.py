from typing import Optional
from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import Address, Money


class PaymentDetailModel(Model):
    """A PaymentDetailModel."""
    destination_address: Optional[Address] = Field(alias='destinationAddress')
    amount: Optional[Money]
    is_change: Optional[bool] = Field(alias='isChange')
