from pydantic import BaseModel, Field, conint
from pybitcoin.types import Money
from .scriptpubkey import ScriptPubKey


class VOut(BaseModel):
    """A VOut."""
    value: Money
    n: conint(ge=0)
    script_pubkey: ScriptPubKey = Field(alias='scriptPubKey')

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
