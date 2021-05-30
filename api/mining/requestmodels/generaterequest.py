from pydantic import conint, Field
from pybitcoin import Model


class GenerateRequest(Model):
    """A GenerateRequest."""
    block_count: conint(ge=0) = Field(alias='blockCount')
