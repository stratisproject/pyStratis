from pydantic import conint, Field
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class GenerateRequest(Model):
    """A request model for the mining/generate endpoint.

    Args:
        block_count (conint(ge=0)): The number of blocks to mine.
    """
    block_count: conint(ge=0) = Field(alias='blockCount')
