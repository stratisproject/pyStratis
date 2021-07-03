from typing import Optional
from pystratis.api import Model


class RPCCommandResponseModel(Model):
    """A RPCCommandResponseModel."""
    value: Optional[dict]
