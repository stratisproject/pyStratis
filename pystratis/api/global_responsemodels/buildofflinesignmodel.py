from typing import List
from pydantic import Field
from pystratis.core.types import Money, hexstr
from pystratis.api import Model
from .utxodescriptor import UtxoDescriptor
from .addressdescriptor import AddressDescriptor


class BuildOfflineSignModel(Model):
    """A pydantic model for a built offline sign request."""
    wallet_name: str = Field(alias='walletName')
    """The wallet name."""
    wallet_account: str = Field(alias='walletAccount')
    """The wallet account."""
    unsigned_transaction: hexstr = Field(alias='unsignedTransaction')
    """The unsigned transaction hex."""
    fee: Money
    """The transaction fee."""
    utxos: List[UtxoDescriptor]
    """The utxos included in the transaction."""
    addresses: List[AddressDescriptor]
    """The addresses and amounts receiving outputs."""
