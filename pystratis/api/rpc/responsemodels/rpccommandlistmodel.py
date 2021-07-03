from typing import Optional
from pystratis.api import Model


class RPCCommandListModel(Model):
    """A RPCCommandListModel."""
    command: Optional[str]
    description: Optional[str]
