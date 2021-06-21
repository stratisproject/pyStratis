from typing import List
from pydantic import BaseModel, Field
from pybitcoin.types import Address, Money, hexstr, uint256
from .utxodescriptor import UtxoDescriptor
from .addressdescriptor import AddressDescriptor


class BuildOfflineSignModel(BaseModel):
    """A BuildOfflineSignModel."""
    wallet_name: str = Field(alias='walletName')
    wallet_account: str = Field(alias='walletAccount')
    unsigned_transaction: hexstr = Field(alias='unsignedTransaction')
    fee: Money
    utxos: List[UtxoDescriptor]
    addresses: List[AddressDescriptor]

    class Config:
        json_encoders = {
            Address: lambda v: str(v),
            Money: lambda v: v.to_coin_unit(),
            hexstr: lambda v: str(v),
            uint256: lambda v: str(v),
            List[AddressDescriptor]: lambda v: [x.json() for x in v],
            List[UtxoDescriptor]: lambda v: [x.json() for x in v]
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
