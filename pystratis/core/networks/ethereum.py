from typing import Optional
from pydantic import Field
import re
# noinspection PyPackageRequirements
from sha3 import keccak_256
from .basenetwork import BaseNetwork


# noinspection PyUnresolvedReferences
class Ethereum(BaseNetwork):
    """Default settings for the ethereum network.

    Args:
        DEFAULT_PORT (int, optional): The network communication port. Default=30303.
    """
    name: str = Field(default='Ethereum')
    DEFAULT_PORT: Optional[int] = Field(default=30303)

    def validate_address(self, address: str) -> bool:
        if self._check_ethereum_checksum(address):
            return True
        if self._check_ethereum(address):
            return True
        return False

    @staticmethod
    def _check_ethereum(address: str) -> bool:
        """Validates an ethereum address that is all uppercase or lowercase"""
        # All address are hex encoded with 0x prefix.
        if re.match(r'^(0x)?[0-9a-f]{40}$', address, re.IGNORECASE) is None:
            return False
        # Checks for either an all upper case or all lower case
        if re.match(r'^(0x)?[0-9a-f]{40}$', address) or re.match(r'^(0x)?[0-9A-F]{40}$', address):
            return True
        return False

    @staticmethod
    def _check_ethereum_checksum(address: str) -> bool:
        """Validates an ethereum checksum address"""
        address = address.replace('0x', '')
        address_hash = keccak_256(
            address.encode('ascii').lower()
        ).hexdigest()
        for i in range(40):
            if int(address_hash[i], 16) > 7 and address[i].upper() != address[i]:
                return False
            if int(address_hash[i], 16) <= 7 and address[i].lower() != address[i]:
                return False
        return True
