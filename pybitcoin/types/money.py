from __future__ import annotations
from typing import Callable, Union
from functools import total_ordering
from decimal import Decimal, InvalidOperation


@total_ordering
class Money:
    """Represents Money."""
    def __init__(self, value):
        self._validate_value(value)
        value = self._fix_comma_separated_str(value)
        if isinstance(value, (float, Decimal, int, str)):
            self._value = round(Decimal(value), 8)
        if isinstance(value, Money):
            self._value = Decimal(value.value)

    @property
    def value(self) -> Decimal:
        return self._value

    @value.setter
    def value(self, value: Decimal) -> None:
        self._validate_value(value)
        self._value = value

    @classmethod
    def __get_validators__(cls) -> Callable:
        yield cls.validate

    @classmethod
    def from_satoshi_units(cls, value: int) -> Money:
        value = Decimal(value) / Decimal(1e8)
        return cls(value)

    @classmethod
    def validate(cls, value) -> Money:
        cls._validate_value(value)
        return cls(value)

    @classmethod
    def _validate_value(cls, v) -> None:
        if not isinstance(v, (int, str, Decimal, float, Money)):
            raise ValueError(f'Value can only be converted from int, str, Decimal, float, and Money.')

        if isinstance(v, Money):
            if v.value < 0:
                raise ValueError('Must be positive.')

        if isinstance(v, (int, float, Decimal, str)):
            try:
                v = cls._fix_comma_separated_str(v)
                v = Decimal(v)
                if v < 0:
                    raise ValueError('Must be positive.')
            except InvalidOperation:
                raise ValueError(f'Cannot convert {v} to Money.')

    def to_coin_unit(self) -> str:
        # noinspection PyTypeChecker
        return '{:.8f}'.format(self.value)

    @classmethod
    def _fix_comma_separated_str(cls, value):
        if isinstance(value, str):
            return value.replace(',', '.')
        return value

    def __eq__(self, other) -> bool:
        if isinstance(other, Money):
            return self.value == other.value
        if isinstance(other, (int, float, Decimal)):
            try:
                return self.value == Decimal(str(other))
            except InvalidOperation:
                raise ValueError(f'Error comparing Money with {other}')
        return False

    def __lt__(self, other) -> bool:
        if isinstance(other, Money):
            return self.value < other.value
        if isinstance(other, (int, float, Decimal)):
            try:
                return self.value < Decimal(str(other))
            except InvalidOperation:
                raise ValueError(f'Error comparing Money with {other}')
        return False

    def __gt__(self, other) -> bool:
        if isinstance(other, Money):
            return self.value > other.value
        if isinstance(other, (int, float, Decimal)):
            try:
                return self.value > Decimal(other)
            except InvalidOperation:
                raise ValueError(f'Error comparing Money with {other}')
        return False

    def __add__(self, other) -> Money:
        if isinstance(other, Money):
            return Money(self.value + other.value)
        if isinstance(other, (int, float, Decimal)):
            return Money(self.value + other)
        raise NotImplementedError(f'Addition between Money and {type(other)} is not defined.')

    def __truediv__(self, other) -> Union[Decimal, Money]:
        if isinstance(other, Money):
            return Decimal(self.value / other.value)
        if isinstance(other, (int, float, Decimal)):
            return Money(self.value / other)
        raise NotImplementedError(f'Division between Money and {type(other)} is not defined.')

    def __floordiv__(self, other) -> Union[int, Money]:
        if isinstance(other, Money):
            return int(self.value // other.value)
        if isinstance(other, (int, float, Decimal)):
            return Money(self.value // other)
        raise NotImplementedError(f'Division between Money and {type(other)} is not defined.')

    def __mul__(self, other) -> Money:
        if isinstance(other, (int, float, Decimal)):
            return Money(self.value * other)
        raise NotImplementedError(f'Multiplication between Money and {type(other)} is not defined.')

    def __hash__(self) -> int:
        return int(self.value * Decimal(1e8))

    def __repr__(self) -> str:
        return f'Money({self.value})'

    def __str__(self) -> str:
        return str(self.value)

    def __int__(self) -> int:
        return int(self.value * Decimal(1e8))
