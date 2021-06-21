from pydantic import BaseModel, Field, conint


class MaturedBlockInfoModel(BaseModel):
    """A MaturedBlockInfoModel."""
    block_hash: str = Field(alias='BlockHash')
    block_height: conint(ge=0) = Field(alias='BlockHeight')
    block_time: conint(ge=0) = Field(alias='BlockTime')

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
