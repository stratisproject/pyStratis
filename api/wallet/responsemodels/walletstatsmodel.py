from typing import List, Optional
from pydantic import Field, conint
from pybitcoin import Model
from .utxoamountmodel import UtxoAmountModel
from .utxopertransactionmodel import UtxoPerTransactionModel
from .utxoperblockmodel import UtxoPerBlockModel


class WalletStatsModel(Model):
    """A WalletStatsModel."""
    wallet_name: Optional[str] = Field(alias='WalletName')
    total_utxo_count: Optional[conint(ge=0)] = Field(alias='TotalUtxoCount')
    unique_transaction_count: Optional[conint(ge=0)] = Field(alias='UniqueTransactionCount')
    unique_block_count: Optional[conint(ge=0)] = Field(alias='UniqueBlockCount')
    finalized_transactions: Optional[conint(ge=0)] = Field(alias='CountOfTransactionsWithAtLeastMaxReorgConfirmations')
    utxo_amounts: Optional[List[UtxoAmountModel]] = Field(alias='UtxoAmounts')
    utxo_per_transaction: Optional[List[UtxoPerTransactionModel]] = Field(alias='UtxoPerTransaction')
    utxo_per_block: Optional[List[UtxoPerBlockModel]] = Field(alias='UtxoPerBlock')
