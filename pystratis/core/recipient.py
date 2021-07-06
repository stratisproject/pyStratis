from typing import Optional
from pydantic import Field, BaseModel
from pystratis.core.types import Money, Address


class Recipient(BaseModel):
    """A pydantic model for a recipient."""
    destination_address: Optional[Address] = Field(alias='destinationAddress')
    """The destination address, if applicable."""
    destination_script: Optional[Address] = Field(alias='destinationScript')
    """The destination script, if applicable."""
    subtraction_fee_from_amount: Optional[bool] = Field(default=True, alias='subtractFeeFromAmount')
    """If true, subtract fee from amount."""
    amount: Money
    """The amount to send to this recipient."""

    class Config:
        json_encoders = {
            Money: lambda v: v.to_coin_unit(),
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
