from typing import Optional, List
from pydantic import Field, SecretStr
from pybitcoin import AddressDescriptor, Model, UtxoDescriptor
from pybitcoin.types import Money


class OfflineSignRequest(Model):
    """A request model for the wallet/offline-sign-request endpoint.

    Args:
        wallet_password: SecretStr = Field(alias='walletPassword')
        wallet_name: str = Field(alias='walletName')
        wallet_account: Optional[str] = Field(default='account 0', alias='walletAccount')
        unsigned_transaction: Optional[str] = Field(alias='unsignedTransaction')
        fee: Money
        utxos: List[UtxoDescriptor]
        addresses: List[AddressDescriptor]
    """
    wallet_password: SecretStr = Field(alias='walletPassword')
    wallet_name: str = Field(alias='walletName')
    wallet_account: Optional[str] = Field(default='account 0', alias='walletAccount')
    unsigned_transaction: Optional[str] = Field(alias='unsignedTransaction')
    fee: Money
    utxos: List[UtxoDescriptor]
    addresses: List[AddressDescriptor]
