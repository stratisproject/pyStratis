from typing import Optional
from pystratis.core import Model


class RPCCommandResponseModel(Model):
    """A RPCCommandResponseModel."""
    value: Optional[dict]
