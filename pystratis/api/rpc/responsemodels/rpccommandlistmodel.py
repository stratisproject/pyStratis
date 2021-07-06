from pystratis.api import Model


class RPCCommandListModel(Model):
    """A pydantic model for a RPC command."""
    command: str
    """The RPC command."""
    description: str
    """The command description."""
