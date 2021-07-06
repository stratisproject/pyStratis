from __future__ import annotations
from typing import Union, Callable
from hashlib import sha256
import base58


class Key:
    """Type representing `private key`_.
    A private key is a secret number, known only to the person that generated it.

    Corresponding type from StratisFullNode's implementation can be found here__.

    Args:
        value (bytes, str, Key): data for private key.
        
    Raises:
        ValueError: Attempt to create Key with unsupported `value` type.

    .. _private key: 
        https://en.bitcoin.it/wiki/Private_key

    .. __: 
        https://github.com/stratisproject/StratisFullNode/blob/master/src/NBitcoin/Key.cs#L10
    """
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
        """pydantic model validation"""
        yield cls.validate

    @classmethod
    def _validate_data(cls, v) -> None:
        """pydantic model validation"""
        if not isinstance(v, (str, Key, bytes)):
            raise ValueError('Can only create Key from another Key, hex string or bytes.')
        if isinstance(v, str):
            base58.b58decode(v)

    @classmethod
    def validate(cls, v) -> Key:
        """pydantic model validation"""
        cls._validate_data(v)
        return cls(v)

    def get_bytes(self) -> bytes:
        """Get private key bytes

        Returns:
            bytes: raw private key data
        """
        return self._keybytes

    def __eq__(self, other):
        assert isinstance(other, Key)
        return self._keybytes == other._keybytes

    def __hash__(self) -> int:
        return hash(self._keybytes)

    def __str__(self) -> str:
        return base58.b58encode(self._keybytes).decode('utf-8')

    def generate_wif_key(self) -> str:
        """Convert current key to `Wallet import format`_

        Returns:
            str: WIF compilant key.

        .. _Wallet import format:
            https://en.bitcoin.it/wiki/Wallet_import_format
        """
        extended = b'\x80' + self._keybytes
        checksum = sha256(sha256(extended).digest()).digest()
        return base58.b58encode(extended + checksum[:4]).decode('utf-8')
