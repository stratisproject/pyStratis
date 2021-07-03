from typing import List
from pydantic import Field
from pystratis.core.types import Address, Money, hexstr, uint256
from pystratis.api import Model
from .utxodescriptor import UtxoDescriptor
from .addressdescriptor import AddressDescriptor


class BuildOfflineSignModel(Model):
    """A BuildOfflineSignModel."""
    wallet_name: str = Field(alias='walletName')
    wallet_account: str = Field(alias='walletAccount')
    unsigned_transaction: hexstr = Field(alias='unsignedTransaction')
    fee: Money
    utxos: List[UtxoDescriptor]
    addresses: List[AddressDescriptor]
