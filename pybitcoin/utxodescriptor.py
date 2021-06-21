from typing import Optional
from pydantic import BaseModel, Field, conint
from pybitcoin.types import Money, uint256


class UtxoDescriptor(BaseModel):
    """A UtxoDescriptor."""
    transaction_id: Optional[uint256] = Field(alias='transactionId')
    index: Optional[conint(ge=0)]
    script_pubkey: Optional[str] = Field(alias='scriptPubKey')
    amount: Money

    class Config:
        json_encoders = {
            Money: lambda v: v.to_coin_unit(),
            uint256: lambda v: str(v)
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
