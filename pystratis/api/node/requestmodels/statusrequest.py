from pystratis.api import Model


# noinspection PyUnresolvedReferences
class StatusRequest(Model):
    """A request model for the node/status endpoint.

    Args:
        publish (bool): If true, publish a full node event with the status.
    """
    publish: bool
