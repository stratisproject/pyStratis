from typing import List, Optional
from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import Address, uint256, hexstr
from .logmodel import LogModel


class ReceiptModel(Model):
    """A pydantic model of a smart contact receipt."""
    transaction_hash: uint256 = Field(alias='transactionHash')
    """The transaction hash."""
    block_hash: uint256 = Field(alias='blockHash')
    """The hash of the block containing the transaction."""
    post_state: Optional[uint256] = Field(alias='postState')
    """The smart contact state after execution."""
    gas_used: Optional[int] = Field(alias='gasUsed')
    """The amount of gas used."""
    from_address: Optional[Address] = Field(alias='from')
    """Sending address, if applicable."""
    to_address: Optional[Address] = Field(alias='to')
    """Receiving address, if applicable."""
    new_contract_address: Optional[Address] = Field(alias='newContractAddress')
    """A new contract address, if creation transaction."""
    success: bool
    """True if transaction successful."""
    return_value: Optional[str] = Field(alias='returnValue')
    """Transaction return value, if applicable."""
    bloom: Optional[hexstr]
    """The bloom filter."""
    error: Optional[str]
    """Error message, if present."""
    logs: Optional[List[LogModel]]
    """Smart contact log model data, if present."""
