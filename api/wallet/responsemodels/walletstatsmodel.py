from typing import List
from pydantic import Field, conint
from pybitcoin import Model
from .utxoamountmodel import UtxoAmountModel
from .utxopertransactionmodel import UtxoPerTransactionModel
from .utxoperblockmodel import UtxoPerBlockModel


class WalletStatsModel(Model):
    """A WalletStatsModel."""
    wallet_name: str = Field(alias='WalletName')
    total_utxo_count: conint(ge=0) = Field(alias='TotalUtxoCount')
    unique_transaction_count: conint(ge=0) = Field(alias='UniqueTransactionCount')
    unique_block_count: conint(ge=0) = Field(alias='UniqueBlockCount')
    finalized_transactions: conint(ge=0) = Field(alias='CountOfTransactionsWithAtLeastMaxReorgConfirmations')
    utxo_amounts: List[UtxoAmountModel] = Field(alias='UtxoAmounts')
    utxo_per_transaction: List[UtxoPerTransactionModel] = Field(alias='UtxoPerTransaction')
    utxo_per_block: List[UtxoPerBlockModel] = Field(alias='UtxoPerBlock')
