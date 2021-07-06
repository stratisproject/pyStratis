from pystratis.api import Model


class RPCCommandResponseModel(Model):
    """A pydantic model for a RPC response."""
    value: dict
    """The response."""
