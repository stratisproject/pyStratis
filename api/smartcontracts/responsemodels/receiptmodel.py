from typing import List, Optional
from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import Address, Money, uint256, hexstr
from .logmodel import LogModel


class ReceiptModel(Model):
    """A ReceiptModel."""
    transaction_hash: Optional[uint256] = Field(alias='TransactionHash')
    block_hash: Optional[uint256] = Field(alias='BlockHash')
    post_state: Optional[uint256] = Field(alias='PostState')
    gas_used: Optional[Money] = Field(alias='GasUsed')
    from_address: Optional[Address] = Field(alias='From')
    to_address: Optional[Address] = Field(alias='To')
    new_contract_address: Optional[Address] = Field(alias='NewContractAddress')
    success: Optional[bool] = Field(alias='Success')
    return_value: Optional[str] = Field(alias='ReturnValue')
    bloom: Optional[hexstr] = Field(alias='Bloom')
    error: Optional[str] = Field(alias='Error')
    logs: Optional[List[LogModel]] = Field(alias='Logs')
