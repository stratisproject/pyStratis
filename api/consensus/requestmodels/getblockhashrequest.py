from pydantic import conint
from pybitcoin import Model


class GetBlockHashRequest(Model):
    """A GetBlockHashRequest."""
    height: conint(ge=0)
