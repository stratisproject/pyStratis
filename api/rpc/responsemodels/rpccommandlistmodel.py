from pybitcoin import Model


class RPCCommandListModel(Model):
    """A RPCCommandListModel."""
    command: str
    description: str
