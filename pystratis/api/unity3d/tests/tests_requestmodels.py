import pytest
import json
from pystratis.api.unity3d.requestmodels import *
from pystratis.core.types import Address
from pystratis.core.networks import CirrusMain


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_addressrequest(network, generate_p2pkh_address):
    data = {
        'address': generate_p2pkh_address(network=network)
    }
    request_model = AddressRequest(
        address=Address(address=data['address'], network=network)
    )
    assert json.dumps(data) == request_model.json()
