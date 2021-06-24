from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import hexstr


class DecodeRawTransactionRequest(Model):
    """A request model for the node/decoderawtransaction endpoint.

    Args:
        raw_hex (hexstr): The transaction hexstring.
    """
    raw_hex: hexstr = Field(alias='rawHex')
