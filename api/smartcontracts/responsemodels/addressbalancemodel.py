from typing import Optional
from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import Address, Money


class AddressBalanceModel(Model):
    """An AddressBalanceModel."""
    address: Optional[Address] = Field(alias='Address')
    sum: Optional[Money] = Field(alias='Sum')
