from pydantic import Field
from pystratis.api import Model
from pystratis.core import DestinationChain
from pystratis.core.types import Money, hexstr


class TransactionResponseModel(Model):
    """A pydantic model of a multisig transaction request."""
    data: hexstr
    """The transaction hexstr."""
    destination: DestinationChain
    """The destination chain."""
    value: Money
    """The amount converted."""
    executed: bool
    """True if the transaction has been processed."""
