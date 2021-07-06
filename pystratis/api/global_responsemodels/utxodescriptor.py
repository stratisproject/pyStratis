from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import Money, uint256


class UtxoDescriptor(Model):
    """A pydantic model of a utxo descriptor."""
    transaction_id: uint256 = Field(alias='transactionId')
    """The transaction hash off the utxo."""
    index: int
    """The index of the utxo in the transaction."""
    script_pubkey: str = Field(alias='scriptPubKey')
    """The scriptpubkey of the utxo."""
    amount: Money
    """The amount in the utxo."""

