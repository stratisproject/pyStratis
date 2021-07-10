from typing import Optional
from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import uint256


# noinspection PyUnresolvedReferences
class BlockRequest(Model):
    """A request model for the blockstore block endpoint.

    Args:
        hash (uint256): The hash of the required block.
        show_transaction_details (bool, optional): A flag that indicates whether to return each block
            transaction complete with details or simply return transaction hashes. Default=True.
        output_json (bool): Output json or hex block. Default=True.

    """
    block_hash: uint256 = Field(alias='Hash')
    show_transaction_details: Optional[bool] = Field(default=True, alias='ShowTransactionDetails')
    output_json: Optional[bool] = Field(default=True, alias='OutputJson')
