from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import Address, Money


class TransferInfoModel(Model):
    """A pydantic model of a smart contact transfer."""
    from_address: Address = Field(alias='from')
    """The sending address."""
    to_address: Address = Field(alias='to')
    """The receiving address."""
    value: Money
    """The amount sent."""
