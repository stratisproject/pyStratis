from typing import Union, Optional
from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import Address, Money


class TransactionOutputModel(Model):
    """A pydantic model of a transaction output."""
    address: Optional[Union[int, Address]]
    """The address receiving the output."""
    amount: Money
    """The output amount."""
    op_return_data: Optional[str] = Field(alias='opReturnData')
    """The OP_RETURN data, if present."""
