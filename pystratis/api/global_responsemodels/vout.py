from pydantic import Field, conint
from pystratis.core.types import Money
from pystratis.api import Model
from .scriptpubkey import ScriptPubKey


class VOut(Model):
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
