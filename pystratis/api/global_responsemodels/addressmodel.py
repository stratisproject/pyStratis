from pydantic import Field
from pystratis.core.types import Address, Money
from pystratis.api import Model


class AddressModel(Model):
    """An AddressModel."""
    address: Address
    is_used: bool = Field(alias='isUsed')
    is_change: bool = Field(alias='isChange')
    amount_confirmed: Money = Field(alias='amountConfirmed')
    amount_unconfirmed: Money = Field(alias='amountUnconfirmed')
