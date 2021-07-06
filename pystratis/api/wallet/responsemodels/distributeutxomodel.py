from typing import List, Optional
from pydantic import Field
from pystratis.api import Model
from pystratis.api.global_responsemodels import WalletSendTransactionModel


class DistributeUtxoModel(Model):
    """A pydantic model for the distribute utxo method."""
    wallet_name: str = Field(alias='walletName')
    """The wallet name."""
    use_unique_address_per_utxo: bool = Field(alias='useUniqueAddressPerUtxo')
    """If true, a different address used for each utxo."""
    utxos_count: int = Field(alias='utxosCount')
    """The number of utxos."""
    utxo_per_transaction: int = Field(alias='utxoPerTransaction')
    """The number of utxos per transaction."""
    timestamp_difference_between_transactions: int = Field(alias='timestampDifferenceBetweenTransactions')
    """The number of seconds between transactions."""
    min_confirmations: int = Field(alias='minConfirmations')
    """The minimum number of confirmations to include utxo in transaction."""
    dry_run: bool = Field(alias='dryRun')
    """If true, simulate the transaction."""
    wallet_send_transaction: Optional[List[WalletSendTransactionModel]] = Field(alias='walletSendTransaction')
    """A list of send transactions (if not simulated)."""
