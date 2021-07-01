from __future__ import annotations
from typing import Callable, Tuple
from binascii import unhexlify


class PubKey:
    """Type representing public key.
    A public key is the number that corresponds to a private key, 
    but does not need to be kept secret.
    A public key can be calculated from a private key, but not vice versa.

    A public key can be presented in compressed or uncompressed format.

    Note:
        Read more about `public key formats`__.

    .. __: https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch04.asciidoc#public-key-formats
    """
    def __init__(self, value: str):
        value = value.replace('0x', '')
        if value[:2] == '04':
            self.x, self.y = self._check_uncompressed(value)
        if value[:2] in ['02', '03']:
            self.x, self.y = self._check_compressed(value)

    @classmethod
    def _check_uncompressed(cls, value: str) -> Tuple[str, str]:
        """Validates and returns an uncompressed pubkey.
        An uncompressed public key must be 64 bytes long and start with '04' value.

        Returns:
            :rtype: (str, str): The (x,y) parts of a public key.
        """
        uncompressed_bytes = unhexlify(value[2:])
        assert len(uncompressed_bytes) == 64
        return uncompressed_bytes[:32].hex(), uncompressed_bytes[32:].hex()

    @classmethod
    def _check_compressed(cls, value: str) -> Tuple[str, str]:
        """Calculates y from x.
        A compressed public key must start with '02' or '03' value.

        Notes:
            https://bitcointalk.org/index.php?topic=644919.0
        """
        p = int(2 ** 256 - 2 ** 32 - 2 ** 9 - 2 ** 8 - 2 ** 7 - 2 ** 6 - 2 ** 4 - 1)
        y_parity = int(value[:2]) - 2
        x = int(value[2:], 16)
        y_sq = (cls._pow_mod(x, 3, p) + 7) % p
        y = cls._pow_mod(y_sq, (p + 1) // 4, p)
        if y % 2 != y_parity:
            y = -y % p
        x = format(x, '0>64x')
        y = format(y, '0>64x')
        return x, y

    @staticmethod
    def _pow_mod(x: int, y: int, z: int) -> int:
        """Modular exponentiation.
        
        Notes:
            https://bitcointalk.org/index.php?topic=644919.0
        """
        number = 1
        while y:
            if y & 1:
                number = number * x % z
            y >>= 1
            x = x * x % z
        return number

    def uncompressed(self) -> str:
        """Retrieves a uncompressed pubkey."""
        return f'04{self.x}{self.y}'

    def compressed(self) -> str:
        """Retreives a compressed pubkey."""
        prefix = '02' if int(self.y, 16) % 2 == 0 else '03'
        return f'{prefix}{self.x}'

    @classmethod
    def __get_validators__(cls) -> Callable:
        yield cls.validate_class

    @classmethod
    def validate_class(cls, value: str) -> PubKey:
        if isinstance(value, PubKey):
            value = str(value)
        if not isinstance(value, str):
            raise ValueError('PubKey must be a string.')
        prefix = value[:2]
        if len(value) == 66 and prefix not in ['02', '03']:
            raise ValueError('Compressed PubKey must have prefix 02 or 03.')
        if len(value) == 130 and prefix != '04':
            raise ValueError('Uncompressed PubKey must have prefix 04.')
        return cls(value)

    def __str__(self) -> str:
        return self.compressed()

    def __eq__(self, other) -> bool:
        if isinstance(other, PubKey):
            return self.uncompressed() == other.uncompressed()
        return False
