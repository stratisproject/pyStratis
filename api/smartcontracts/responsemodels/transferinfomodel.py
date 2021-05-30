from pydantic import Field
from pybitcoin import Model, Address
from pybitcoin.types import Money


class TransferInfoModel(Model):
    """A TransferInfoModel."""
    from_address: Address = Field(alias='From')
    to_address: Address = Field(alias='To')
    value: Money = Field(alias='Value')
