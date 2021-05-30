from typing import List
from pydantic import Field
from pybitcoin import Address, Model
from pybitcoin.types import Money, uint256
from .logmodel import LogModel


class ReceiptModel(Model):
    """A ReceiptModel."""
    transaction_hash: uint256 = Field(alias='TransactionHash')
    block_hash: uint256 = Field(alias='BlockHash')
    post_state: str = Field(alias='PostState')
    gas_used: Money = Field(alias='GasUsed')
    from_address: Address = Field(alias='From')
    to_address: Address = Field(alias='To')
    new_contract_address: Address = Field(alias='NetContractAddress')
    success: bool = Field(alias='Success')
    return_value: str = Field(alias='ReturnValue')
    bloom: str = Field(alias='Bloom')
    error: str = Field(alias='Error')
    logs: List[LogModel] = Field(alias='Logs')
