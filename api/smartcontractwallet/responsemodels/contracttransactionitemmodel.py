from typing import Optional
from pydantic import Field, conint
from pybitcoin import Model, ContractTransactionItemType
from pybitcoin.types import Address, Money, uint256


class ContractTransactionItemModel(Model):
    """A ContractTransactionItemModel."""
    block_height: Optional[conint(ge=0)] = Field(alias='blockHeight')
    item_type: Optional[ContractTransactionItemType] = Field(alias='type')
    hash: Optional[uint256]
    to_address: Optional[Address] = Field(alias='to')
    amount: Optional[Money]
    transaction_fee: Optional[Money] = Field(alias='transactionFee')
    gas_fee: Optional[Money] = Field(alias='gasFee')
