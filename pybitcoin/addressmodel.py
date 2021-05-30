from pydantic import BaseModel, Field
from pybitcoin.types import Money


class AddressModel(BaseModel):
    """An AddressModel."""
    address: str
    is_used: bool = Field(alias='isUsed')
    is_change: bool = Field(alias='isChange')
    amount_confirmed: Money = Field(alias='AmountConfirmed')
    amount_unconfirmed: Money = Field(alias='AmountUnconfirmed')

    class Config:
        json_encoders = {
            Money: lambda v: str(v),
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super(AddressModel, self).json(exclude_none=True, by_alias=True)
