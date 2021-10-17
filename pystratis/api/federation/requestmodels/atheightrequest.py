from pydantic import Field
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class AtHeightRequest(Model):
    """A request model for the federation/get-mining-pubkey-at-height endpoint.

    Args:
        block_height (int): The height to query.

    """
    block_height: int = Field(alias='blockHeight')
