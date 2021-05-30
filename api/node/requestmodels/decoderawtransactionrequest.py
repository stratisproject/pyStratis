from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import hexstr


class DecodeRawTransactionRequest(Model):
    """A DecodeRawTransactionRequest."""
    raw_hex: hexstr = Field(alias='rawHex')
