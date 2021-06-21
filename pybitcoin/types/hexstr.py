from __future__ import annotations
from typing import Callable
from binascii import hexlify


# noinspection PyPep8Naming
class hexstr(str):
    """Represents an hex string."""

    def __new__(cls, content, *args, **kwargs):
        cls._validate_data(content)
        return super(hexstr, cls).__new__(cls, content)

    @classmethod
    def __get_validators__(cls) -> Callable:
        yield cls.validate

    @classmethod
    def _validate_data(cls, v) -> None:
        if not isinstance(v, str):
            raise ValueError('Invalid hex.')

        # Will raise ValueError if not a hex string
        int(v, 16)

    @classmethod
    def validate(cls, v) -> hexstr:
        cls._validate_data(v)
        return cls(v)

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        return super().__repr__().replace("'", '')

    def to_bytes(self) -> bytes:
        return hexlify(self)
