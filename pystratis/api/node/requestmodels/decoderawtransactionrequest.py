from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import hexstr


# noinspection PyUnresolvedReferences
class DecodeRawTransactionRequest(Model):
    """A request model for the node/decoderawtransaction endpoint.

    Args:
        raw_hex (hexstr): The transaction hexstring.
    """
    raw_hex: hexstr = Field(alias='rawHex')
