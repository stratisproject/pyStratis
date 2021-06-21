from __future__ import annotations
from functools import total_ordering
from typing import Callable, Union
from .hexstr import hexstr


# noinspection PyPep8Naming
@total_ordering
class customint:
    """Represents a custom int."""
    _num_bits: int = None
    _minvalue: int = None
    _maxvalue: int = None

    def __init__(self, value, num_bits=None, minvalue=None, maxvalue=None):
        self.update(num_bits=num_bits, minvalue=minvalue, maxvalue=maxvalue)
        self.value = value

    @classmethod
    def update(cls, num_bits, minvalue, maxvalue):
        cls._num_bits = num_bits
        cls._minvalue = minvalue
        cls._maxvalue = maxvalue

    @property
    def value(self) -> int:
        return self._value

    # noinspection PyUnresolvedReferences
    @value.setter
    def value(self, value: int) -> None:
        self._value = self.validate_value(value)

    @classmethod
    def __get_validators__(cls) -> Callable:
        yield cls.validate_class

    def __hash__(self) -> int:
        return hash(self._value)

    # noinspection PyTypeChecker
    def __hex__(self) -> str:
        conversion = self.value & (2 ** self._num_bits - 1)
        fixed_width = self._num_bits // 4
        padchar = '0' if self.value > 0 else 'f'
        format_spec = f'{padchar}>{fixed_width}x'
        return format(conversion, format_spec)

    def to_hex(self) -> str:
        return self.__hex__()

    @classmethod
    def hex_to_int(cls, v: Union[str, hexstr]) -> int:
        # For unsigned ints
        if cls._minvalue == 0:
            return int(v, 16)
        # For signed ints
        sign_mask = 1 << (len(v.replace('0x', '')) * 4 - 1)
        value_mask = sign_mask - 1
        value_int = int(v, 16)
        new_value = -(value_int & sign_mask) | (value_int & value_mask)
        return new_value

    @classmethod
    def validate_class(cls, value) -> customint:
        cls.validate_allowed_types(value)
        try:
            value = int(value)
        except ValueError:
            value = cls._convert_hexstr_to_int(value)
        _check_value_out_of_range(value=value, minvalue=cls._minvalue, maxvalue=cls._maxvalue)
        return cls(value)

    def validate_value(self, value) -> int:
        self.validate_allowed_types(value)
        try:
            value = int(value)
        except ValueError:
            value = self._convert_hexstr_to_int(value)
        _check_value_out_of_range(value=value, minvalue=self._minvalue, maxvalue=self._maxvalue)
        return int(value)

    @classmethod
    def validate_allowed_types(cls, value) -> None:
        if isinstance(value, bool) or not isinstance(value, (str, int, hexstr, customint)):
            raise ValueError('Invalid type. Must be str, int, or customint subclass.')

    @classmethod
    def _convert_hexstr_to_int(cls, value: Union[str, int, hexstr]) -> int:
        return cls.hex_to_int(value) if isinstance(value, (hexstr, str)) else value

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.value})'

    def __str__(self) -> str:
        return self.to_hex()

    def __int__(self) -> int:
        return int(self.value)

    def __eq__(self, other) -> bool:
        if isinstance(other, customint):
            return self.value == other.value
        if isinstance(other, int):
            return self.value == other
        return False

    def __lt__(self, other) -> bool:
        if isinstance(other, customint):
            return self.value < other.value
        if isinstance(other, int):
            return self.value < other
        return False

    def __gt__(self, other) -> bool:
        if isinstance(other, customint):
            return self.value > other.value
        if isinstance(other, int):
            return self.value > other
        return False

    # noinspection PyTypeChecker
    def __len__(self) -> int:
        return len(self.value)


def _check_underflow(minvalue: int, value: int) -> bool:
    return value < minvalue


def _check_overflow(maxvalue: int, value: int) -> bool:
    return value > maxvalue


def _check_value_out_of_range(value: int, minvalue: int, maxvalue: int) -> None:
    if _check_underflow(minvalue=minvalue, value=value):
        raise ValueError(f'Underflow error: value less than {minvalue}.')
    if _check_overflow(maxvalue=maxvalue, value=value):
        raise ValueError(f'Overflow error: value greater than {maxvalue}.')
