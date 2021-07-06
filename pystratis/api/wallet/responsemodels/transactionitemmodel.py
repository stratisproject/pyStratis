from typing import List, Optional
from datetime import datetime
from pydantic import Field
from pystratis.api import Model
from pystratis.core import TransactionItemType
from pystratis.core.types import Address, Money, uint256
from .paymentdetailmodel import PaymentDetailModel


class TransactionItemModel(Model):
    """A pydantic model for a transaction item."""
    transaction_type: TransactionItemType = Field(alias='type')
    """The transaction type."""
    to_address: Address = Field(alias='toAddress')
    """The address receiving the transaction."""
    transaction_id: uint256 = Field(alias='id')
    """The transaction hash."""
    amount: Money
    """The transaction value."""
    payments: Optional[List[PaymentDetailModel]]
    """A list of payment detail models."""
    fee: Optional[Money]
    """The transaction fee."""
    confirmed_in_block: int = Field(alias='confirmedInBlock')
    """The block n height where transaction was confirmed."""
    timestamp: datetime
    """The transaction timestamp."""
    tx_output_time: datetime = Field(alias='txOutputTime')
    """The transaction output time."""
    tx_output_index: int = Field(alias='txOutputIndex')
    """The transaction output index."""
    block_index: Optional[int] = Field(alias='blockIndex')
    """The block index."""
