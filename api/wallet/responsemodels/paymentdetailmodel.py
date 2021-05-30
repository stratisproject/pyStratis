from pydantic import Field
from pybitcoin import Address, Model
from pybitcoin.types import Money


class PaymentDetailModel(Model):
    """A PaymentDetailModel."""
    destination_address: Address = Field(alias='destinationAddress')
    amount: Money
    is_change: bool = Field(alias='isChange')
