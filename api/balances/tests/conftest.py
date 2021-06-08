import pytest
from typing import List
from pybitcoin.types import Address


@pytest.fixture(scope='function')
def overamountatheightresponse(generate_p2wpkh_address):
    # noinspection PyUnresolvedReferences
    def _overamountatheightresponse(network: 'BaseNetwork') -> List[Address]:
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
