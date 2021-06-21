from typing import Optional
from pydantic import BaseModel, Field, conint
from .scriptsig import ScriptSig


class VIn(BaseModel):
    """A VIn."""
    coinbase: Optional[str]
    txid: Optional[str]
    vout: Optional[conint(ge=0)]
    script_sig: Optional[ScriptSig] = Field(alias='scriptSig')
    sequence: conint(ge=0)

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
