from pydantic import Field
from pystratis.api import Model
from pystratis.core import DestinationChain
from pystratis.core.types import Address


class MultisigTransactionRequest(Model):
    """A pydantic model of a multisigtransaction request."""
    destination_chain: DestinationChain = Field(alias='destinationChain')
    """The destination chain."""
    transaction_id: int = Field(alias='transactionId')
    """The transaction id."""
    raw: bool
    """Indicates whether to partially decode the transaction or leave it in raw hex format."""
