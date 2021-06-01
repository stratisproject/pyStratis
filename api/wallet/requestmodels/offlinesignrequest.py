from typing import Optional, List
from pydantic import Field, SecretStr
from pybitcoin import AddressDescriptor, Model, UtxoDescriptor


class OfflineSignRequest(Model):
    """A OfflineSignRequest."""
    wallet_password: SecretStr = Field(alias='walletPassword')
    wallet_name: str = Field(alias='walletName')
    wallet_account: Optional[str] = Field(default='account 0', alias='walletAccount')
    unsigned_transaction: Optional[str] = Field(alias='unsignedTransaction')
    fee: str
    utxos: List[UtxoDescriptor]
    addresses: List[AddressDescriptor]
