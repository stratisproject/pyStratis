import pytest
from typing import List
from pystratis.core.types import Address
from pystratis.core.networks import BaseNetwork


@pytest.fixture(scope='package')
def overamountatheightresponse(generate_p2wpkh_address):
    def _overamountatheightresponse(network: BaseNetwork) -> List[Address]:
        return [
            generate_p2wpkh_address(network),
            generate_p2wpkh_address(network),
            generate_p2wpkh_address(network),
            generate_p2wpkh_address(network),
            generate_p2wpkh_address(network),
            generate_p2wpkh_address(network),
            generate_p2wpkh_address(network),
            generate_p2wpkh_address(network),
            generate_p2wpkh_address(network),
            generate_p2wpkh_address(network)
        ]
    return _overamountatheightresponse
