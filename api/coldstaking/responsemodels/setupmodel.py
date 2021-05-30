from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import uint256


class SetupModel(Model):
    """A SetupModel."""
    transaction_hex: uint256 = Field(alias='transactionHex')
