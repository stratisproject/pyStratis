from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import uint256


# noinspection PyUnresolvedReferences
class ReceiptRequest(Model):
    """A request model for the smartcontracts/receipt endpoint.

    Args:
        tx_hash (uint256): The transaction hash of the smart contract receipt.
    """
    tx_hash: uint256 = Field(alias='txHash')
