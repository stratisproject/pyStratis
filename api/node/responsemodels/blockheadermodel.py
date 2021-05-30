from pydantic import Field, conint
from pybitcoin import Model
from pybitcoin.types import uint256, hexstr


class BlockHeaderModel(Model):
    """A BlockHeaderModel."""
    version: conint(ge=0)
    merkleroot: hexstr
    nonce: conint(ge=0)
    bits: str
    previous_blockhash: uint256 = Field(alias='previousblockhash')
    time: conint(ge=0)
