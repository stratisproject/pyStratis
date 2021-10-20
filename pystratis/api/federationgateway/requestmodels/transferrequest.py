from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import uint256


# noinspection PyUnresolvedReferences
class TransferRequest(Model):
    """A request model for the federationgateway/transfer endpoint.

    Args:
        deposit_id (uint256): The deposit id hash.
    """
    deposit_id: uint256 = Field(alias='depositId')
