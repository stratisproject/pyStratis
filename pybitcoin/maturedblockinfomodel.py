from pydantic import BaseModel, Field, conint
from datetime import datetime
from pybitcoin.types import uint256


class MaturedBlockInfoModel(BaseModel):
    """A MaturedBlockInfoModel."""
    block_hash: uint256 = Field(alias='blockHash')
    block_height: conint(ge=0) = Field(alias='blockHeight')
    block_time: datetime = Field(alias='blockTime')

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
