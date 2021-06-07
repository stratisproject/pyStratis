from typing import List, Optional
from pydantic import Field
from pybitcoin import Address, Model
from pybitcoin.types import Money, uint256
from .logmodel import LogModel


class ReceiptModel(Model):
    """A ReceiptModel."""
    transaction_hash: Optional[uint256] = Field(alias='TransactionHash')
    block_hash: Optional[uint256] = Field(alias='BlockHash')
    post_state: Optional[str] = Field(alias='PostState')
    gas_used: Optional[Money] = Field(alias='GasUsed')
    from_address: Optional[Address] = Field(alias='From')
    to_address: Optional[Address] = Field(alias='To')
    new_contract_address: Optional[Address] = Field(alias='NetContractAddress')
    success: Optional[bool] = Field(alias='Success')
    return_value: Optional[str] = Field(alias='ReturnValue')
    bloom: Optional[str] = Field(alias='Bloom')
    error: Optional[str] = Field(alias='Error')
    logs: Optional[List[LogModel]] = Field(alias='Logs')
