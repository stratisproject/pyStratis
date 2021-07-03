from typing import Optional, Union
from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import Address, Money


class TransactionOutputModel(Model):
    """A TransactionOutputModel."""
    address: Optional[Union[int, Address]]
    amount: Optional[Money]
    op_return_data: Optional[str] = Field(alias='opReturnData')
