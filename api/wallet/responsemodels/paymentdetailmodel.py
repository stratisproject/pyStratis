from typing import Optional
from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import Address, Money


class PaymentDetailModel(Model):
    """A PaymentDetailModel."""
    destination_address: Optional[Address] = Field(alias='destinationAddress')
    amount: Optional[Money]
    is_change: Optional[bool] = Field(alias='isChange')
