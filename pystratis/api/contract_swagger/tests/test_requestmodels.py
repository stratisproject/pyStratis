import pytest
from pystratis.api.contract_swagger.requestmodels import *
from pystratis.core.networks import CirrusMain
from pystratis.core.types import Address
import json


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_contractrequest(network, generate_p2pkh_address):
    data = {
        'address': generate_p2pkh_address(network=network)
    }
    request_model = ContractRequest(
        address=Address(address=data['address'], network=network)
    )
    assert json.dumps(data) == request_model.json()
