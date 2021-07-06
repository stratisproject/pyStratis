from __future__ import annotations
from typing import Union, Callable
import base58
from .key import Key


class ExtKey(Key):
    """Type representing extended private key, as specified in BIP32_.

    Corresponding type from StratisFullNode's implementation can be found here__.

    Args:
        value (bytes, str, Key): data for a private key.
    Raises:
        ValueError: 
            Attempt to create ExtKey with unsupported `value` type.
            Attempt to create with incorrect length.

    .. _BIP32: 
        https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki

    .. __: 
        https://github.com/stratisproject/StratisFullNode/blob/master/src/NBitcoin/BIP32/ExtKey.cs#L12
    """
    def __init__(self, value: Union[bytes, str, Key]):
        super().__init__(value)
        buffer_size = len(self._keybytes)
        if buffer_size != 64:
            raise ValueError(f'Extended key must be 64 bytes long (got {buffer_size} bytes)')

    def generate_private_key_bytes(self) -> bytes:
        """Get private key from this extended private key.

        Returns:
            bytes: private key, represented by the first 32 bytes of extended private key.
        """
        return self._keybytes[:32]

    def generate_chain_code_bytes(self) -> bytes:
        """Get chain code from this extended private key.

        Returns:
            bytes: chain code, represented by the last 32 bytes of extended private key.
        """
        return self._keybytes[32:]

    def generate_private_key_base58(self) -> str:
        """Get Base58-encoded private key from this extended private key.

        Returns:
            str: base58-encoded private key
        """
        return base58.b58encode_check(self.generate_private_key_bytes()).decode('utf-8')

    def generate_private_key(self) -> Key:
        """Get private key from this extended private key.

        Returns:
            Key: private key.
        """
        return Key(self.generate_private_key_bytes())

    @classmethod
    def __get_validators__(cls) -> Callable:
        """pydantic model validation"""
        yield cls.validate

    @classmethod
    def _validate_data(cls, v) -> None:
        """pydantic model validation"""
        if not isinstance(v, (str, ExtKey, bytes)):
            raise ValueError('Can only create ExtKey from another ExtKey, hex string or bytes.')
        if isinstance(v, str):
            if isinstance(v, str):
                base58.b58decode_check(v)

    @classmethod
    def validate(cls, v) -> Key:
        """pydantic model validation"""
        cls._validate_data(v)
        return cls(v)
