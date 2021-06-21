from typing import Optional, Union
from pydantic import Field, BaseModel
from pybitcoin.types import Address, Money


class TransactionOutputModel(BaseModel):
    """A TransactionOutputModel."""
    address: Optional[Union[int, Address]]
    amount: Optional[Money]
    op_return_data: Optional[str] = Field(alias='OpReturnData')

    class Config:
        json_encoders = {
            Money: lambda v: v.to_coin_unit(),
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
