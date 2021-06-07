from typing import Optional
from pybitcoin import Model


class RPCCommandListModel(Model):
    """A RPCCommandListModel."""
    command: Optional[str]
    description: Optional[str]
