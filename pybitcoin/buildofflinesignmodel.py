from typing import List
from pydantic import BaseModel, Field
from pybitcoin.types import Money
from .utxodescriptor import UtxoDescriptor
from .addressdescriptor import AddressDescriptor


class BuildOfflineSignModel(BaseModel):
    """A BuildOfflineSignModel."""
    wallet_name: str = Field(alias='walletName')
    wallet_account: str = Field(alias='walletAccount')
    unsigned_transaction: str = Field(alias='unsignedTransaction')
    fee: Money
    utxos: List[UtxoDescriptor]
    addresses: List[AddressDescriptor]

    class Config:
        json_encoders = {
            Money: lambda v: str(v),
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super(BuildOfflineSignModel, self).json(exclude_none=True, by_alias=True)
