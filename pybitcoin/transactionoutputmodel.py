from typing import Optional
from pydantic import Field, BaseModel
from pybitcoin.types import Address, Money


class TransactionOutputModel(BaseModel):
    """A TransactionOutputModel."""
    address: Address
    amount: Money
    op_return_data: Optional[str] = Field(alias='OpReturnData')

    class Config:
        json_encoders = {
            Money: lambda v: v.to_coin_unit(),
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super(TransactionOutputModel, self).json(exclude_none=True, by_alias=True)
