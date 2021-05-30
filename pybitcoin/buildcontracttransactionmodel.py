from pydantic import BaseModel, Field
from pybitcoin.types import Money, uint256, hexstr


class BuildContractTransactionModel(BaseModel):
    """A BuildContractTransactionModel."""
    fee: Money
    hex: hexstr
    message: str
    success: bool
    transaction_id: uint256 = Field(alias='transactionId')

    class Config:
        json_encoders = {
            Money: lambda v: str(v),
            uint256: lambda v: str(v),
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super(BuildContractTransactionModel, self).json(exclude_none=True, by_alias=True)
