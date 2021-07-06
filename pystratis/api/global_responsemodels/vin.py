from typing import Optional
from pydantic import Field
from pystratis.api import Model
from .scriptsig import ScriptSig


class VIn(Model):
    """Represents transaction's input.

    Note:
        Learn more about `transaction input structure`__.

    .. __: https://en.bitcoin.it/wiki/Transaction#Input
    """
    coinbase: Optional[str]
    """Three scriptSig off this was a coinbase transaction."""
    txid: Optional[str]
    """The transaction hash."""
    vout: Optional[int]
    """The index of the output."""
    script_sig: Optional[ScriptSig] = Field(alias='scriptSig')
    """The scriptSig."""
    sequence: int
    """The transaction's sequence number."""
