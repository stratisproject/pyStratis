import bech32
from hashlib import sha256
import base58check
from typing import Optional
from pydantic import BaseModel, StrictBytes


class BaseNetwork(BaseModel):
    """Describes a network."""
    name: str
    PUBKEY_ADDRESS: Optional[StrictBytes]
    SCRIPT_ADDRESS: Optional[StrictBytes]
    SECRET_KEY: Optional[StrictBytes]
    ENCRYPTED_SECRET_KEY_NO_EC: Optional[StrictBytes]
    ENCRYPTED_SECRET_KEY_EC: Optional[StrictBytes]
    EXT_PUBLIC_KEY: Optional[StrictBytes]
    EXT_SECRET_KEY: Optional[StrictBytes]
    PASSPHRASE_CODE: Optional[StrictBytes]
    CONFIRMATION_CODE: Optional[StrictBytes]
    STEALTH_ADDRESS: Optional[StrictBytes]
    ASSET_ID: Optional[StrictBytes]
    COLORED_ADDRESS: Optional[StrictBytes]
    BECH32_HRP: Optional[str]
    DEFAULT_PORT:  Optional[int]
    RPC_PORT: Optional[int]
    API_PORT: Optional[int]
    SIGNALR_PORT:  Optional[int]

    def validate_address(self, address: str) -> bool:
        """Validates an address on this network."""
        if self._check_bech32_charset(address):
            if self._check_p2wsh(address):
                return True
            if self._check_p2wpkh(address):
                return True
        if self._check_base58_charset(address):
            if self._check_p2sh(address):
                return True
            if self._check_p2pkh(address):
                return True
        return False

    @staticmethod
    def _check_base58_charset(address: str) -> bool:
        # Charset is missing '0', 'O', 'I', and 'l'
        return all([char in '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz' for char in set(address)])

    def _check_bech32_charset(self, address: str):
        prefix_and_separator_size = self._get_segwit_prefix_len() + 1
        stripped_address = address[prefix_and_separator_size:]
        # Charset is missing '1', 'b', 'i', and 'o'
        return all([char in '234567890ABCDEFGHIJKLMNOPQRSTUVWXYZacdefghjklmnpqrstuvwxyz' for char in set(stripped_address)])

    def _get_segwit_prefix_len(self) -> int:
        """Returns the segwit prefix length for the specifed network."""
        return len(self.BECH32_HRP)

    def _check_p2wsh(self, address: str) -> bool:
        """Validates a p2wsh address"""
        segwit_prefix_length = self._get_segwit_prefix_len()
        if address[0:segwit_prefix_length] == self.BECH32_HRP:
            witver, data = bech32.decode(self.BECH32_HRP, address)
            if witver == 0 and len(data) == 32:
                return True
        return False

    def _check_p2sh(self, address: str) -> bool:
        """Validates a p2sh address"""
        version_bytes_len = len(self.SCRIPT_ADDRESS)
        # noinspection PyTypeChecker
        data = base58check.b58decode(address)
        payload, checksum = data[0:-4], data[-4:]
        if payload[:version_bytes_len] == self.SCRIPT_ADDRESS:
            if len(payload) == version_bytes_len + 20:
                payload_digest = sha256(payload).digest()
                payload_digest = sha256(payload_digest).digest()
                if payload_digest[:4] == checksum:
                    return True
        return False

    def _check_p2pkh(self, address: str) -> bool:
        """Validates a p2pkh address"""
        version_bytes_len = len(self.PUBKEY_ADDRESS)
        # noinspection PyTypeChecker
        data = base58check.b58decode(address)
        payload, checksum = data[0:-4], data[-4:]
        if payload[:version_bytes_len] == self.PUBKEY_ADDRESS:
            if len(payload) == version_bytes_len + 20:
                payload_digest = sha256(payload).digest()
                payload_digest = sha256(payload_digest).digest()
                if payload_digest[:4] == checksum:
                    return True
        return False

    def _check_p2wpkh(self, address: str) -> bool:
        """Validates a p2wpkh address"""
        segwit_prefix_length = self._get_segwit_prefix_len()
        if address[0:segwit_prefix_length] == self.BECH32_HRP:
            witver, data = bech32.decode(self.BECH32_HRP, address)
            if witver == 0 and len(data) == 20:
                return True
        return False
