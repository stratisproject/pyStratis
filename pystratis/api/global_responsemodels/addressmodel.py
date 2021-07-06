from pydantic import Field
from pystratis.core.types import Address, Money
from pystratis.api import Model


class AddressModel(Model):
    """A pydantic model representing an address with balance."""
    address: Address
    """The address."""
    is_used: bool = Field(alias='isUsed')
    """If true, the address is used."""
    is_change: bool = Field(alias='isChange')
    """If true, the address is a change address."""
    amount_confirmed: Money = Field(alias='amountConfirmed')
    """The amount confirmed in the address."""
    amount_unconfirmed: Money = Field(alias='amountUnconfirmed')
    """The amount unconfirmed in the address."""
