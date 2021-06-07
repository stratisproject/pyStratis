from typing import List, Optional
from pydantic import Field, conint
from pybitcoin import Model, WalletSendTransactionModel


class DistributeUtxoModel(Model):
    """A DistributeUtxoModel."""
    wallet_name: Optional[str] = Field(alias='WalletName')
    use_unique_address_per_utxo: Optional[bool] = Field(alias='UseUniqueAddressPerUtxo')
    utxos_count: Optional[conint(ge=0)] = Field(alias='UtxosCount')
    utxo_per_transaction: Optional[conint(ge=0)] = Field(alias='UtxoPerTransaction')
    timestamp_difference_between_transactions: Optional[conint(ge=0)] = Field(alias='TimestampDifferenceBetweenTransactions')
    min_confirmations: Optional[conint(ge=0)] = Field(alias='MinConfirmations')
    dry_run: Optional[bool] = Field(alias='DryRun')
    wallet_send_transaction: Optional[List[WalletSendTransactionModel]] = Field(alias='WalletSendTransaction')
