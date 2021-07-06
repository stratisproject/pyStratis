from pydantic import Field
from pystratis.core.types import uint256
from datetime import datetime
from pystratis.api import Model


class RemovedTransactionModel(Model):
    """A pydantic model for a removed transaction."""
    transaction_id: uint256 = Field(alias='transactionId')
    """The removed transaction hash."""
    creation_time: datetime = Field(alias='creationTime')
    """The creation time of the removed transaction."""
