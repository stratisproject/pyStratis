from typing import Optional
from pydantic import Field, conint
from pybitcoin import Address, Model, ContractTransactionItemType
from pybitcoin.types import Money, uint256


class ContractTransactionItemModel(Model):
    """A ContractTransactionItemModel."""
    block_height: Optional[conint(ge=0)] = Field(alias='BlockHeight')
    item_type: ContractTransactionItemType = Field(alias='Type')
    hash: uint256 = Field(alias='Hash')
    to_address: Address = Field(alias='To')
    amount: Money = Field(alias='Amount')
    transaction_fee: Money = Field(alias='TransactionFee')
    gas_fee: Money = Field(alias='GasFee')
