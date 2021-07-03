from pydantic import Field, conint
from pystratis.api import Model


class DepositsRequest(Model):
    """A request model for the federationgateway/deposits endpoint.

    Args:
        block_height (conint(ge=0)): The block height at which to obtain deposits.
    """
    block_height: conint(ge=0) = Field(alias='blockHeight')
