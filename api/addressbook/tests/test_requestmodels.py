import pytest
import json
from api.addressbook.requestmodels import *
from pybitcoin.types import Address
from pybitcoin.networks import StraxMain, CirrusMain


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_addrequest(network, generate_p2pkh_address):
    data = {
        'address': generate_p2pkh_address(network=network),
        'label': 'Test'
    }
    request_model = AddRequest(
        address=Address(address=data['address'], network=network),
        label='Test'
    )
    assert json.dumps(data) == request_model.json()


def test_removerequest():
    data = {
        'label': 'Test'
    }
    request_model = RemoveRequest(
        label='Test'
    )
    assert json.dumps(data) == request_model.json()


def test_getrequest():
    data = {
        'skip': 2,
        'take': 3
    }
    request_model = GetRequest(
        skip=2,
        take=3
    )
    assert json.dumps(data) == request_model.json()
