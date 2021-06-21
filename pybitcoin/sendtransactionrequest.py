from pydantic import BaseModel
from pybitcoin.types import hexstr


class SendTransactionRequest(BaseModel):
    """A SendTransactionRequest."""
    hex: hexstr

    class Config:
        json_encoders = {
            hexstr: lambda v: str(v),
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
