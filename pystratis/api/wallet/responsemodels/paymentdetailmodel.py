from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import Address, Money


class PaymentDetailModel(Model):
    """A pydantic model for payment details."""
    destination_address: Address = Field(alias='destinationAddress')
    """The destination address."""
    amount: Money
    """The amount sent to this address."""
    is_change: bool = Field(alias='isChange')
    """If true, destination address is a change address."""
