from __future__ import annotations
from typing import Union, Callable
from hashlib import sha256
import base58


class Key:
    def __init__(self, value: Union[bytes, str, Key]):
        if isinstance(value, str):
            self._keybytes: bytes = base58.b58decode(value)
        elif isinstance(value, Key):
            self._keybytes: bytes = value.get_bytes()
        elif isinstance(value, bytes):
            self._keybytes = value
        else:
            raise ValueError('Can only create Key from another Key, hex string or bytes')

    @classmethod
    def __get_validators__(cls) -> Callable:
        yield cls.validate

    @classmethod
    def _validate_data(cls, v) -> None:
        if not isinstance(v, (str, Key, bytes)):
            raise ValueError('Can only create Key from another Key, hex string or bytes.')
        if isinstance(v, str):
            base58.b58decode(v)

    @classmethod
    def validate(cls, v) -> Key:
        cls._validate_data(v)
        return cls(v)

    def get_bytes(self) -> bytes:
        return self._keybytes

    def __eq__(self, other):
        assert isinstance(other, Key)
        return self._keybytes == other._keybytes

    def __hash__(self) -> int:
        return hash(self._keybytes)

    def __str__(self) -> str:
        return base58.b58encode(self._keybytes).decode('utf-8')

    def generate_wif_key(self) -> str:
        extended = b'\x80' + self._keybytes
        checksum = sha256(sha256(extended).digest()).digest()
        return base58.b58encode(extended + checksum[:4]).decode('utf-8')
