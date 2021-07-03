from pydantic import BaseModel, Field
from pystratis.core.types import hexstr


class SendTransactionRequest(BaseModel):
    """A request model for multiple api endpoints.

    Args:
        transaction_hex (hexstr): The hexified transaction.
    """
    transaction_hex: hexstr = Field(alias='hex')

    class Config:
        json_encoders = {
            hexstr: lambda v: str(v),
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
