from pydantic import Field, BaseModel
from pybitcoin.types import Money


class TransactionOutputModel(BaseModel):
    """A TransactionOutputModel."""
    address: str
    amount: Money
    op_return_data: str = Field(alias='OpReturnData')

    class Config:
        json_encoders = {
            Money: lambda v: str(v),
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super(TransactionOutputModel, self).json(exclude_none=True, by_alias=True)
