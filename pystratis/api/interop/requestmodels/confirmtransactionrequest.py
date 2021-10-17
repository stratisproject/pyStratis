from pydantic import Field
from pystratis.api import Model
from pystratis.core import DestinationChain
from pystratis.core.types import Address


class ConfirmTransactionRequest(Model):
    """A pydantic model of a confirm transaction request."""
    destination_chain: DestinationChain = Field(alias='destinationChain')
    """The destination chain."""
    transaction_id: int = Field(alias='transactionId')
    """The transaction id."""
    gas_price: int = Field(alias='gasPrice')
    """The gas price."""
