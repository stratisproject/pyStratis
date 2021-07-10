from typing import Optional, List
from pydantic import Field, SecretStr
from pystratis.api import Model
from pystratis.api.global_responsemodels import AddressDescriptor, UtxoDescriptor
from pystratis.core.types import Money, hexstr


# noinspection PyUnresolvedReferences
class OfflineSignRequest(Model):
    """A request model for the wallet/offline-sign-request endpoint.

    Args:
        wallet_password (str): The wallet password.
        wallet_name (str): The wallet name.
        wallet_account (str, optional): The account name. Default='account 0'.
        unsigned_transaction (hexstr): The unsigned transaction hexstr.
        fee (Money): The fee.
        utxos (List[UtxoDescriptor]): A list of utxodescriptors.
        addresses (List[AddressDescriptor]): A list of addresses to send transactions.
    """
    wallet_password: SecretStr = Field(alias='walletPassword')
    wallet_name: str = Field(alias='walletName')
    wallet_account: Optional[str] = Field(default='account 0', alias='walletAccount')
    unsigned_transaction: hexstr = Field(alias='unsignedTransaction')
    fee: Money
    utxos: List[UtxoDescriptor]
    addresses: List[AddressDescriptor]
