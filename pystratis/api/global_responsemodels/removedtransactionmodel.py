from pydantic import Field
from pystratis.core.types import uint256
from datetime import datetime
from pystratis.api import Model


class RemovedTransactionModel(Model):
    """A RemovedTransactionModel."""
    transaction_id: uint256 = Field(alias='transactionId')
    creation_time: datetime = Field(alias='creationTime')
