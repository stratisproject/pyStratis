from pydantic import Field
from pybitcoin import Model, Address
from pybitcoin.types import Money


class AddressBalanceModel(Model):
    """An AddressBalanceModel."""
    address: Address = Field(alias='Address')
    sum: Money = Field(alias='Sum')
