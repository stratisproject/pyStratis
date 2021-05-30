import pytest
from typing import List
from pybitcoin import Address


@pytest.fixture(scope='function')
def overamountatheightresponse(create_p2wpkh_address):
    # noinspection PyUnresolvedReferences
    def _overamountatheightresponse(network: 'BaseNetwork') -> List[Address]:
        return [
            create_p2wpkh_address(network),
            create_p2wpkh_address(network),
            create_p2wpkh_address(network),
            create_p2wpkh_address(network),
            create_p2wpkh_address(network),
            create_p2wpkh_address(network),
            create_p2wpkh_address(network),
            create_p2wpkh_address(network),
            create_p2wpkh_address(network),
            create_p2wpkh_address(network)
        ]
    return _overamountatheightresponse
