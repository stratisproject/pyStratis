from typing import Callable
from decimal import Decimal


class Money(int):
    """Represents Money."""
    def __new__(cls, content, *args, **kwargs):
        # Assume floats are given in reference to 1e8 satoshis.
        if isinstance(content, float) or isinstance(content, Decimal):
            content = cls._float_to_satoshi(content)
        cls._validate_data(content)
        return super(Money, cls).__new__(cls, content)

    @classmethod
    def __get_validators__(cls) -> Callable:
        yield cls.validate

    @classmethod
    def validate(cls, v) -> 'Money':
        cls._validate_data(v)
        return cls(v)

    @classmethod
    def _validate_data(cls, v) -> None:
        # Assume floats are given in reference to 1e8 satoshis.
        if isinstance(v, float) or isinstance(v, Decimal):
            v = cls._float_to_satoshi(v)

        # Try to validate a string in base 10.
        if isinstance(v, str):
            v = int(v)

        # Money must be positive.
        if isinstance(v, int) and v < 0:
            raise ValueError('Must be positive.')

        # Final catch-all
        if not isinstance(v, int):
            raise ValueError(f'Invalid Money{v}.')

    @classmethod
    def _float_to_satoshi(cls, value) -> int:
        return int(Decimal(value) * Decimal(1e8))

    def __repr__(self):
        return f'Money({super().__repr__()})'

    def __str__(self):
        return super().__repr__()
