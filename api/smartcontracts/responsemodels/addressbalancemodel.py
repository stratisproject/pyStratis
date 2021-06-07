from typing import Optional
from pydantic import Field
from pybitcoin import Model, Address
from pybitcoin.types import Money


class AddressBalanceModel(Model):
    """An AddressBalanceModel."""
    address: Optional[Address] = Field(alias='Address')
    sum: Optional[Money] = Field(alias='Sum')
