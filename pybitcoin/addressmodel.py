from pydantic import BaseModel, Field
from pybitcoin.types import Address, Money


class AddressModel(BaseModel):
    """An AddressModel."""
    address: Address
    is_used: bool = Field(alias='isUsed')
    is_change: bool = Field(alias='isChange')
    amount_confirmed: Money = Field(alias='amountConfirmed')
    amount_unconfirmed: Money = Field(alias='amountUnconfirmed')

    class Config:
        json_encoders = {
            Money: lambda v: v.to_coin_unit(),
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
