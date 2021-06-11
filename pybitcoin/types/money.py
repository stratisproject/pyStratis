from __future__ import annotations
from typing import Callable, Union
from functools import total_ordering
from decimal import Decimal


@total_ordering
class Money:
    """Represents Money."""
    def __init__(self, value):
        if isinstance(value, float) or isinstance(value, Decimal):
            value = self._float_to_satoshi(value)
        if isinstance(value, Money):
            value = value.value
        self._validate_value(value)
        self._value = value

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        self._validate_value(value)
        self._value = value

    @classmethod
    def __get_validators__(cls) -> Callable:
        yield cls.validate

    @classmethod
    def validate(cls, v) -> Money:
        cls._validate_value(v)
        return cls(v)

    @classmethod
    def _validate_value(cls, v) -> None:
        # Assume floats are given in reference to 1e8 satoshis.
        if isinstance(v, Money):
            v = v.value

        if isinstance(v, str):
            # Try to validate a string in base 10.
            try:
                v = int(v)
            except ValueError:
                pass
            # Try to validate a float string.
            try:
                v = float(v)
            except ValueError:
                pass

        if isinstance(v, float) or isinstance(v, Decimal):
            v = cls._float_to_satoshi(v)

        # Money must be positive.
        if isinstance(v, int) and v < 0:
            raise ValueError('Must be positive.')

        # Final catch-all
        if not isinstance(v, int):
            raise ValueError(f'Invalid Money({v}).')

    @classmethod
    def _float_to_satoshi(cls, value: Union[float, Decimal]) -> int:
        return int(Decimal(value) * Decimal(1e8))

    def to_coin_unit(self) -> str:
        # noinspection PyTypeChecker
        return '{:.8f}'.format(Decimal(self.value) / Decimal(1e8))

    def __eq__(self, other) -> bool:
        if isinstance(other, Money):
            return self.value == other.value
        if isinstance(other, int):
            return self.value == other
        return False

    def __lt__(self, other) -> bool:
        if isinstance(other, Money):
            return self.value < other.value
        if isinstance(other, int):
            return self.value < other
        return False

    def __gt__(self, other) -> bool:
        if isinstance(other, Money):
            return self.value > other.value
        if isinstance(other, int):
            return self.value > other
        return False

    def __hash__(self) -> int:
        return self.value

    def __repr__(self) -> str:
        return f'Money({self.value})'

    def __str__(self) -> str:
        return str(self.value)

    def __int__(self) -> int:
        return int(self.value)
