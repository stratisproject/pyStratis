from typing import Optional
from pydantic import BaseModel, Field
from pybitcoin.types import Money, uint256, hexstr


class BuildTransactionModel(BaseModel):
    """A BuildTransactionModel."""
    fee: Optional[Money] = Field(default=0)
    hex: Optional[hexstr]
    transaction_id: Optional[uint256] = Field(alias='transactionId')

    class Config:
        json_encoders = {
            Money: lambda v: v.to_coin_unit(),
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
