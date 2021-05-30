from typing import Optional, List
from pydantic import Field
from .scriptsig import ScriptSig


class ScriptPubKey(ScriptSig):
    """A ScriptPubKey."""
    type: Optional[str]
    req_sigs: Optional[int] = Field(alias='reqSigs')
    addresses: Optional[List[str]]

    class Config:
        allow_population_by_field_name = True
