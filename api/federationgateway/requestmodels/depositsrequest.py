from pydantic import Field, conint
from pybitcoin import Model


class DepositsRequest(Model):
    """A DepositsRequest."""
    block_height: conint(ge=0) = Field(alias='blockHeight')
