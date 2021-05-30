from typing import List
from pydantic import Field, conint
from pybitcoin import Model, WalletSendTransactionModel


class DistributeUtxoModel(Model):
    """A DistributeUtxoModel."""
    wallet_name: str = Field(alias='WalletName')
    use_unique_address_per_utxo: bool = Field(alias='UseUniqueAddressPerUtxo')
    utxos_count: conint(ge=0) = Field(alias='UtxosCount')
    utxo_per_transaction: conint(ge=0) = Field(alias='UtxoPerTransaction')
    timestamp_difference_between_transactions: conint(ge=0) = Field(alias='TimestampDifferenceBetweenTransactions')
    min_confirmations: conint(ge=0) = Field(alias='MinConfirmations')
    dry_run: bool = Field(alias='DryRun')
    wallet_send_transaction: List[WalletSendTransactionModel] = Field(alias='WalletSendTransaction')
