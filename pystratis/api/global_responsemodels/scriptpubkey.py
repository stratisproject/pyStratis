from typing import List, Optional
from pydantic import Field
from .scriptsig import ScriptSig


class ScriptPubKey(ScriptSig):
    """A ScriptPubKey.

    A ScriptPubKey is a part of transaction's output, and is the second half of a script.

    Note:
        Learn more about `transaction structure`__.

    .. __: https://en.bitcoin.it/wiki/Transaction
    """
    type: str
    """The type of script. The list of supported types can be found in sources_.
    
    .. _sources: https://github.com/stratisproject/StratisFullNode/blob/master/src/Stratis.Bitcoin/Controllers/Models/TransactionModel.cs#L327
    """
    req_sigs: Optional[int] = Field(alias='reqSigs')
    """The number of required signatures."""
    addresses: Optional[List[str]]
    """A list of output addresses."""
