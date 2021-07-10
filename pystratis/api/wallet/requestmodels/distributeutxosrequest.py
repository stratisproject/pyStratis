from typing import Optional, List
from pydantic import SecretStr, Field, conint
from pystratis.api import Model
from pystratis.core import Outpoint


# noinspection PyUnresolvedReferences
class DistributeUTXOsRequest(Model):
    """A request model for the wallet/distribute-utxos endpoint.

    Args:
        wallet_name (str): The wallet name.
        account_name (str, optional): The account name. Default='account 0'.
        wallet_password (str): The wallet password.
        use_unique_address_per_utxo (bool, optional): If True, uses a unique address for each utxo. Default=True.
        reuse_addresses (bool, optional): If True, reuses addresses. Default=True.
        use_change_addresses (bool, optional): If True, use change addresses. Default=False.
        utxos_count (conint(ge=0)): The number of utxos to create.
        utxo_per_transaction (conint(ge=0)): The number of utxos per transaction.
        timestamp_difference_between_transactions (conint(ge=0), optional): The number of seconds between transactions. Default=0.
        min_confirmations (conint(ge=0), optional): The minimum number of confirmations to include in transaction. Default=0.
        outpoints (List[Outpoint]): A list of outpoints to include in the transaction.
        dry_run (bool, optional): If True, simulate transaction. Default=True.
    """
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
