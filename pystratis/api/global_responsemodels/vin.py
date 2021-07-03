from typing import Optional
from pydantic import Field, conint
from pystratis.api import Model
from .scriptsig import ScriptSig


class VIn(Model):
    """Represents transaction's input.
    
    Args:
        coinbase (str, optional): The scriptSig if this was a coinbase transaction.
        txid (str, optional): The transaction's ID.
        vout (int, optional): The index of the output.
        script_sig (ScriptSig, optional): The ScriptSig.
        sequence (int): The transaction's sequence number.

    Note:
        Learn more about `transaction input structure`__.

    .. __: https://en.bitcoin.it/wiki/Transaction#Input
    """
    coinbase: Optional[str]
    txid: Optional[str]
    vout: Optional[conint(ge=0)]
    script_sig: Optional[ScriptSig] = Field(alias='scriptSig')
    sequence: conint(ge=0)
