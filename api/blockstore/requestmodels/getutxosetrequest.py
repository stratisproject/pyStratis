from pydantic import Field
from pybitcoin import Model


class GetUTXOSetRequest(Model):
    """A GetUTXOSetRequest."""
    at_block_height: int = Field(alias='atBlockHeight')
