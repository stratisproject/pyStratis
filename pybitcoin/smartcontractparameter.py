from __future__ import annotations
from typing import Any
from pydantic import ValidationError
from pybitcoin import Address
from pybitcoin.types import int32, int64, uint32, uint64, uint128, uint256
from .smartcontractparametertype import SmartContractParameterType


class SmartContractParameter:
    def __init__(self, type: SmartContractParameterType, value: Any):
        self.type = type
        self.value = value

    def __str__(self) -> str:
        if self.type == SmartContractParameterType.Boolean:
            return f'{self.type.value}#{str(self.value).lower()}'
        if self.type == SmartContractParameterType.Byte:
            return f'{self.type.value}#{int.from_bytes(self.value,"big")}'
        if self.type == SmartContractParameterType.Char:
            return f'{self.type.value}#{self.value}'
        if self.type == SmartContractParameterType.String:
            return f'{self.type.value}#{self.value}'
        if self.type == SmartContractParameterType.UInt32:
            return f'{self.type.value}#{self.value}'
        if self.type == SmartContractParameterType.Int32:
            return f'{self.type.value}#{self.value}'
        if self.type == SmartContractParameterType.UInt64:
            return f'{self.type.value}#{self.value}'
        if self.type == SmartContractParameterType.Int64:
            return f'{self.type.value}#{self.value}'
        if self.type == SmartContractParameterType.Address:
            return f'{self.type.value}#{self.value}'
        if self.type == SmartContractParameterType.ByteArray:
            return f'{self.type.value}#{self.value.hex().upper()}'
        if self.type == SmartContractParameterType.UInt128:
            return f'{self.type.value}#{int(self.value)}'
        if self.type == SmartContractParameterType.UInt256:
            return f'{self.type.value}#{int(self.value)}'

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_class

    @classmethod
    def validate_class(cls, instance) -> SmartContractParameter:
        cls.validate_values(type=instance.type, value=instance.value)
        return instance

    @staticmethod
    def validate_values(type: SmartContractParameterType, value: Any) -> bool:
        if type.Boolean and isinstance(value, bool):
            return True
        # noinspection PyTypeChecker
        if type.Byte and isinstance(value, bytes) and len(value) == 1:
            return True
        if type.Char and isinstance(value, str) and len(value) == 1:
            return True
        if type.String:
            if isinstance(value, str):
                return True
            # noinspection PyBroadException
            try:
                str(value)
                return True
            except:
                pass
        if type.UInt32 and isinstance(value, uint32):
            return True
        if type.UInt64 and isinstance(value, uint64):
            return True
        if type.Int32 and isinstance(value, int32):
            return True
        if type.Int64 and isinstance(value, int64):
            return True
        if type.UInt128 and isinstance(value, uint128):
            return True
        if type.UInt256 and isinstance(value, uint256):
            return True
        if type.Address and isinstance(value, Address):
            return True
        if type.ByteArray and isinstance(value, bytearray):
            return True
        raise ValidationError(
            [ValueError(f'Invalid {type.name} parameter.')],
            model=SmartContractParameter,
        )
