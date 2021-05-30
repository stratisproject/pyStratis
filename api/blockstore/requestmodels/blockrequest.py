from typing import Optional
from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import uint256


class BlockRequest(Model):
    """A BlockRequest."""
    hash: uint256 = Field(alias='Hash')
    show_transaction_details: Optional[bool] = Field(default=True, alias='ShowTransactionDetails')
    output_json: Optional[bool] = Field(default=True, alias='OutputJson')
