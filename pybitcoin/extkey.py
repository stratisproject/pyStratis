from __future__ import annotations
from typing import Union, Callable
import base58
from .key import Key


class ExtKey(Key):
    def __init__(self, value: Union[bytes, str, Key]):
        super().__init__(value)

    def generate_private_key_bytes(self) -> bytes:
        return self._keybytes[:32]

    def generate_private_key_base58(self) -> str:
        return base58.b58encode_check(self.generate_private_key_bytes()).decode('utf-8')

    def generate_private_key(self) -> Key:
        return Key(self.generate_private_key_bytes())

    @classmethod
    def __get_validators__(cls) -> Callable:
        yield cls.validate

    @classmethod
    def _validate_data(cls, v) -> None:
        if not isinstance(v, (str, ExtKey, bytes)):
            raise ValueError('Can only create ExtKey from another ExtKey, hex string or bytes.')
        if isinstance(v, str):
            if isinstance(v, str):
                base58.b58decode_check(v)

    @classmethod
    def validate(cls, v) -> Key:
        cls._validate_data(v)
        return cls(v)
