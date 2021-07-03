from typing import List, Optional
from pydantic import Field, conint
from pystratis.api import Model
from pystratis.api.global_responsemodels import WalletSendTransactionModel


class DistributeUtxoModel(Model):
    """A DistributeUtxoModel."""
    wallet_name: Optional[str] = Field(alias='walletName')
    use_unique_address_per_utxo: Optional[bool] = Field(alias='useUniqueAddressPerUtxo')
    utxos_count: Optional[conint(ge=0)] = Field(alias='utxosCount')
    utxo_per_transaction: Optional[conint(ge=0)] = Field(alias='utxoPerTransaction')
    timestamp_difference_between_transactions: Optional[conint(ge=0)] = Field(alias='timestampDifferenceBetweenTransactions')
    min_confirmations: Optional[conint(ge=0)] = Field(alias='minConfirmations')
    dry_run: Optional[bool] = Field(alias='dryRun')
    wallet_send_transaction: Optional[List[WalletSendTransactionModel]] = Field(alias='walletSendTransaction')
