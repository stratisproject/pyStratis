from pydantic import Field
from pystratis.core.types import Money
from pystratis.api import Model
from .scriptpubkey import ScriptPubKey


class VOut(Model):
    """Represents transaction's output.

    Note:
        Learn more about `transaction output structure and scriptPubKey`__.

    .. __: https://en.bitcoin.it/wiki/Transaction#Output
    """
    value: Money
    """The value of a transaction's output."""
    n: int
    """The index of the output."""
    script_pubkey: ScriptPubKey = Field(alias='scriptPubKey')
    """The output's scriptPubKey."""
