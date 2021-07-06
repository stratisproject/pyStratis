from typing import List, ForwardRef
from enum import IntEnum
from pydantic import BaseModel, SecretStr
from pystratis.core.types import *
from pystratis.core import Key, ExtKey, PubKey, ExtPubKey, SmartContractParameter
# These must be implemented as ForwardRef to prevent circular imports
Recipient = ForwardRef('Recipient')
Outpoint = ForwardRef('Outpoint')
AddressDescriptor = ForwardRef('AddressDescriptor')
UtxoDescriptor = ForwardRef('UtxoDescriptor')
WalletSecret = ForwardRef('WalletSecret')
MultisigSecret = ForwardRef('MultisigSecret')


class Model(BaseModel):
    """A Model template."""
    class Config:
        json_encoders = {
            Address: lambda v: v.json(),
            bool: lambda v: str(v).lower(),
            bytes: lambda v: v.hex(),
            IntEnum: lambda v: v.value,
            SecretStr: lambda v: v.get_secret_value(),
            Money: lambda v: v.to_coin_unit(),
            hexstr: lambda v: str(v),
            ExtPubKey: lambda v: str(v),
            PubKey: lambda v: str(v),
            int32: lambda v: str(v),
            uint32: lambda v: str(v),
            int64: lambda v: str(v),
            uint64: lambda v: str(v),
            uint128: lambda v: str(v),
            uint160: lambda v: str(v),
            uint256: lambda v: str(v),
            Recipient: lambda v: v.json(),
            Outpoint: lambda v: v.json(),
            SmartContractParameter: lambda v: str(v),
            Key: lambda v: str(v),
            ExtKey: lambda v: str(v),
            List[str]: lambda v: ','.join(v),
            List[uint256]: lambda v: [str(x) for x in v],
            List[AddressDescriptor]: lambda v: [x.json() for x in v],
            List[MultisigSecret]: lambda v: [x.json() for x in v],
            List[Recipient]: lambda v: [x.json() for x in v],
            List[Outpoint]: lambda v: [x.json() for x in v],
            List[SmartContractParameter]: lambda v: [str(x) for x in v],
            List[UtxoDescriptor]: lambda v: [x.json() for x in v],
            List[WalletSecret]: lambda v: [x.json() for x in v]
        }
        allow_population_by_field_name = True
        use_enum_values = True
        extra = 'forbid'
    
    def json(self, *args, **kwargs) -> str:
        self.update_forward_refs()
        return super().json(exclude_none=True, by_alias=True)
