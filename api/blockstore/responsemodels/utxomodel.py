from pydantic import Field, conint
from pybitcoin import Model
from pybitcoin.types import Money, uint256


class UTXOModel(Model):
    """A UTXOModel."""
    transaction_id: uint256 = Field(alias='txId')
    index: conint(ge=0)
    script_pubkey: str = Field(alias='scriptPubKey')
    value: Money
