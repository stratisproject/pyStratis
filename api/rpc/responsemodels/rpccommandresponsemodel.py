from typing import Optional
from pybitcoin import Model


class RPCCommandResponseModel(Model):
    """A RPCCommandResponseModel."""
    value: Optional[dict]
