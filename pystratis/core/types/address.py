from __future__ import annotations
from typing import Callable
from pystratis.core.networks import BaseNetwork


class Address:
    """A address model. Address is validated by the network."""

    def __init__(self, address: str, network: BaseNetwork):
        self.validate_values(address=address, network=network)
        self.address = address
        self.network = network

    def __repr__(self) -> str:
        return self.address

    def __str__(self) -> str:
        return self.address

    def __eq__(self, other) -> bool:
        return self.address == other

    def json(self) -> str:
        return self.address

    @classmethod
    def __get_validators__(cls) -> Callable:
        yield cls.validate_class

    @classmethod
    def validate_class(cls, value) -> Address:
        cls.validate_values(address=value.address, network=value.network)
        return value

    @staticmethod
    def validate_values(address: str, network: BaseNetwork) -> bool:
        if network.validate_address(address):
            return True
        raise ValueError('Invalid address for given network.')
