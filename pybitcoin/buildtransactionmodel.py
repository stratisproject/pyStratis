from typing import Optional
from pydantic import BaseModel, Field
from pybitcoin.types import Money


class BuildTransactionModel(BaseModel):
    """A BuildTransactionModel."""
    fee: Optional[Money] = Field(default=0)
    hex: str
    transaction_id: str = Field(alias='transactionId')

    class Config:
        json_encoders = {
            Money: lambda v: str(v),
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super(BuildTransactionModel, self).json(exclude_none=True, by_alias=True)
