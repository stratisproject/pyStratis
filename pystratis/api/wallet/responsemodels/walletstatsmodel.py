from typing import List
from pydantic import Field
from pystratis.api import Model
from .utxoamountmodel import UtxoAmountModel
from .utxopertransactionmodel import UtxoPerTransactionModel
from .utxoperblockmodel import UtxoPerBlockModel


class WalletStatsModel(Model):
    """A pydantic model for wallet stats."""
    wallet_name: str = Field(alias='walletName')
    """The wallet name."""
    total_utxo_count: int = Field(alias='totalUtxoCount')
    """The total number of utxos."""
    unique_transaction_count: int = Field(alias='uniqueTransactionCount')
    """The number of unique transactions."""
    unique_block_count: int = Field(alias='uniqueBlockCount')
    """The number of unique blocks containing wallet transactions."""
    finalized_transactions: int = Field(alias='countOfTransactionsWithAtLeastMaxReorgConfirmations')
    """The number of finalized transactions."""
    utxo_amounts: List[UtxoAmountModel] = Field(alias='utxoAmounts')
    """A list of utxo amounts."""
    utxo_per_transaction: List[UtxoPerTransactionModel] = Field(alias='utxoPerTransaction')
    """A list of utxo per transaction."""
    utxo_per_block: List[UtxoPerBlockModel] = Field(alias='utxoPerBlock')
    """A list of utxo per block."""
