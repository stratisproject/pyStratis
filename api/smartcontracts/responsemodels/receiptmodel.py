from typing import List, Optional
from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import Address, uint256, hexstr
from .logmodel import LogModel


class ReceiptModel(Model):
    """A ReceiptModel."""
    transaction_hash: Optional[uint256] = Field(alias='transactionHash')
    block_hash: Optional[uint256] = Field(alias='blockHash')
    post_state: Optional[uint256] = Field(alias='postState')
    gas_used: Optional[int] = Field(alias='gasUsed')
    from_address: Optional[Address] = Field(alias='from')
    to_address: Optional[Address] = Field(alias='to')
    new_contract_address: Optional[Address] = Field(alias='newContractAddress')
    success: Optional[bool]
    return_value: Optional[str] = Field(alias='returnValue')
    bloom: Optional[hexstr]
    error: Optional[str]
    logs: Optional[List[LogModel]]
