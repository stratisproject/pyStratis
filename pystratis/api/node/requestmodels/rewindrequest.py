from pystratis.api import Model


# noinspection PyUnresolvedReferences
class RewindRequest(Model):
    """A request model for the node/rewind endpoint.

    Args:
        height (int): The height to rewind to on node restart.
    """
    height: int
