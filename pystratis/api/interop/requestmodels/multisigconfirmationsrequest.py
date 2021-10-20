from pydantic import Field
from pystratis.api import Model
from pystratis.core import DestinationChain
from pystratis.core.types import Address


class MultisigConfirmationsRequest(Model):
    """A pydantic model of a multisigconfirmations request."""
    destination_chain: DestinationChain = Field(alias='destinationChain')
    """The destination chain."""
    transaction_id: int = Field(alias='transactionId')
    """The transaction id."""
