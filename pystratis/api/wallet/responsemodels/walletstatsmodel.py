from typing import List, Optional
from pydantic import Field, conint
from pystratis.core import Model
from .utxoamountmodel import UtxoAmountModel
from .utxopertransactionmodel import UtxoPerTransactionModel
from .utxoperblockmodel import UtxoPerBlockModel


class WalletStatsModel(Model):
    """A WalletStatsModel."""
    wallet_name: Optional[str] = Field(alias='walletName')
    total_utxo_count: Optional[conint(ge=0)] = Field(alias='totalUtxoCount')
    unique_transaction_count: Optional[conint(ge=0)] = Field(alias='uniqueTransactionCount')
    unique_block_count: Optional[conint(ge=0)] = Field(alias='uniqueBlockCount')
    finalized_transactions: Optional[conint(ge=0)] = Field(alias='countOfTransactionsWithAtLeastMaxReorgConfirmations')
    utxo_amounts: Optional[List[UtxoAmountModel]] = Field(alias='utxoAmounts')
    utxo_per_transaction: Optional[List[UtxoPerTransactionModel]] = Field(alias='utxoPerTransaction')
    utxo_per_block: Optional[List[UtxoPerBlockModel]] = Field(alias='utxoPerBlock')
