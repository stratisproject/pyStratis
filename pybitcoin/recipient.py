from typing import Optional
from pydantic import BaseModel, Field
from pybitcoin.types import Money
from pybitcoin.types.address import Address


class Recipient(BaseModel):
    """A Recipient."""
    destination_address: Optional[Address] = Field(alias='destinationAddress')
    destination_script: Optional[Address] = Field(alias='destinationScript')
    subtraction_fee_from_amount: Optional[bool] = Field(default=True, alias='subtractFeeFromAmount')
    amount: Money

    class Config:
        json_encoders = {
            Money: lambda v: v.to_coin_unit(),
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
