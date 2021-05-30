from typing import List, Optional
from pydantic import Field, conint
from pybitcoin import Address, Model, TransactionItemType
from pybitcoin.types import Money, uint256
from .paymentdetailmodel import PaymentDetailModel


class TransactionItemModel(Model):
    """A TransactionItemModel."""
    transaction_type: TransactionItemType = Field(alias='type')
    to_address: Address = Field(alias='toAddress')
    transaction_id: uint256 = Field(alias='id')
    amount: Money
    payments: List[PaymentDetailModel]
    fee: Money
    confirmed_in_block: Optional[conint(ge=0)] = Field(alias='confirmedInBlock')
    timestamp: str
    tx_output_time: conint(ge=0) = Field(alias='txOutputTime')
    tx_output_index: conint(ge=0) = Field(alias='txOutputIndex')
    block_index: Optional[conint(ge=0)] = Field(alias='blockIndex')
