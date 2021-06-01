from __future__ import annotations
from typing import Callable
from hashlib import sha256
import base58


class ExtPubKey:
    # noinspection PyTypeChecker
    def __init__(self, extpubkey: str):
        self.version: bytes = None
        self.depth: bytes = None
        self.parent_fingerprint: bytes = None
        self.index: bytes = None
        self.chain_code: bytes = None
        self.key: bytes = None
        self.checksum = None
        self.decode_extpubkey(extpubkey=extpubkey)

    def decode_extpubkey(self, extpubkey: str):
        data = base58.b58decode(extpubkey)
        self.version = data[:4]
        assert len(self.version) == 4
        self.depth = data[4:5]
        assert len(self.depth) == 1
        self.parent_fingerprint = data[5:9]
        assert len(self.parent_fingerprint) == 4
        self.index = data[9:13]
        assert len(self.index) == 4
        self.chain_code = data[13:45]
        assert len(self.chain_code) == 32
        self.key = data[45:78]
        assert len(self.key) == 33

    def get_payload(self) -> bytes:
        return self.version + self.depth + self.parent_fingerprint + self.index + self.chain_code + self.key

    @staticmethod
    def calculate_checksum(payload: bytes) -> bytes:
        return sha256(sha256(payload).digest()).digest()[:4]

    def __str__(self):
        payload = self.get_payload()
        checksum = self.calculate_checksum(payload)
        return base58.b58encode(payload + checksum).decode('ascii')

    @classmethod
    def __get_validators__(cls) -> Callable:
        yield cls.validate_class

    @classmethod
    def validate_class(cls, value) -> ExtPubKey:
        data = base58.b58decode(value)
        payload = data[:78]
        checksum = cls.calculate_checksum(payload)
        if base58.b58encode(payload + checksum).decode('ascii') != value:
            raise ValueError('Invalid extpubkey.')
        return cls(value)
