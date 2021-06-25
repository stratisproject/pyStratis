from pydantic import BaseModel, Field, conint
from pybitcoin.types import Money
from .scriptpubkey import ScriptPubKey


class VOut(BaseModel):
    """Represents transaction's output.
    
    Args:
        value (Money): The value of transaction's output.
        n (int): The index of the output.
        script_pubkey (ScriptPubKey): The output's scriptpubkey.

    Note:
        Learn more about `transaction output structure and scriptPubKey`__.

    .. __: https://en.bitcoin.it/wiki/Transaction#Output
    """
    value: Money
    n: conint(ge=0)
    script_pubkey: ScriptPubKey = Field(alias='scriptPubKey')

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
