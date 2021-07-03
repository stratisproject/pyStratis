from typing import Optional, List
from pydantic import Field
from .scriptsig import ScriptSig


class ScriptPubKey(ScriptSig):
    """A ScriptPubKey.

    A ScriptPubKey is a part of transaction's output, and is the second half of a script.

    Args:
        asm (str): The assembly representation of the script.
        hex (str): The hex representation of the script.
        type (str, optional): The type of script. The list of supported types can be found in sources_.
        req_sigs (int, optional): The number of required sigs.
        addresses (List[str], optional): A list of output addresses.

    Note:
        Learn more about `transaction structure`__.

    .. __: https://en.bitcoin.it/wiki/Transaction
    .. _sources: https://github.com/stratisproject/StratisFullNode/blob/master/src/Stratis.Bitcoin/Controllers/Models/TransactionModel.cs#L327
    """
    type: Optional[str]
    req_sigs: Optional[int] = Field(alias='reqSigs')
    addresses: Optional[List[str]]

    class Config:
        allow_population_by_field_name = True
