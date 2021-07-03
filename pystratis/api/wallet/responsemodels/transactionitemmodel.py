from typing import List, Optional
from datetime import datetime
from pydantic import Field, conint
from pystratis.api import Model
from pystratis.core import TransactionItemType
from pystratis.core.types import Address, Money, uint256
from .paymentdetailmodel import PaymentDetailModel


class TransactionItemModel(Model):
    """A TransactionItemModel."""
    transaction_type: Optional[TransactionItemType] = Field(alias='type')
    to_address: Optional[Address] = Field(alias='toAddress')
    transaction_id: Optional[uint256] = Field(alias='id')
    amount: Optional[Money]
    payments: Optional[List[PaymentDetailModel]]
    fee: Optional[Money]
    confirmed_in_block: Optional[conint(ge=0)] = Field(alias='confirmedInBlock')
    timestamp: Optional[datetime]
    tx_output_time: Optional[datetime] = Field(alias='txOutputTime')
    tx_output_index: Optional[conint(ge=0)] = Field(alias='txOutputIndex')
    block_index: Optional[conint(ge=0)] = Field(alias='blockIndex')
