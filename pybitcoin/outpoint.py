from pydantic import BaseModel, Field, conint
from pybitcoin.types import uint256


class Outpoint(BaseModel):
    """An Outpoint."""
    transaction_id: uint256 = Field(alias='transactionId')
    index: conint(ge=0)

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(by_alias=True, exclude_none=True)
