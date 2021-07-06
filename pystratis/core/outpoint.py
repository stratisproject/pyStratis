from typing import Optional
from pydantic import BaseModel, Field, conint
from pystratis.core.types import uint256


class Outpoint(BaseModel):
    """A pydantic model representing an outpoint."""
    transaction_id: Optional[uint256] = Field(alias='transactionId')
    """The transaction hash of the unspent output."""
    index: conint(ge=0)
    """The index of the outpoint. Must be >= 0."""

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(by_alias=True, exclude_none=True)
