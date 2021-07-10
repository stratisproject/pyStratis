from pydantic import Field
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class GetUTXOSetRequest(Model):
    """A request model for the GetUTXOSetRequest.

    Args:
        at_block_height (int): The specified block height.
    """
    at_block_height: int = Field(alias='atBlockHeight')
