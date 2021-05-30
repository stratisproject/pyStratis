from typing import Optional, List
from pydantic import SecretStr, Field, conint
from pybitcoin import Model, Outpoint


class DistributeUTXOsRequest(Model):
    """A DistributeUTXOsRequest."""
    wallet_name: str = Field(alias='walletName')
    account_name: str = Field(default='account 0', alias='accountName')
    wallet_password: SecretStr = Field(alias='walletPassword')
    use_unique_address_per_utxo: Optional[bool] = Field(default=True, alias='useUniqueAddressPerUtxo')
    reuse_addresses: Optional[bool] = Field(default=True, alias='reuseAddresses')
    use_change_addresses: Optional[bool] = Field(default=False, alias='useChangeAddresses')
    utxos_count: conint(ge=0) = Field(alias='utxosCount')
    utxo_per_transaction: conint(ge=0) = Field(alias='utxoPerTransaction')
    timestamp_difference_between_transactions: Optional[conint(ge=0)] = Field(default=0, alias='timestampDifferenceBetweenTransactions')
    min_confirmations: Optional[conint(ge=0)] = Field(default=0, alias='minConfirmations')
    outpoints: List[Outpoint]
    dry_run: Optional[bool] = Field(default=True, alias='dryRun')
