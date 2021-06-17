import pytest
from api.signalr.responsemodels import *
from nodes import CirrusMinerNode


@pytest.mark.skip(reason='Endpoint not active for cirrus network with devmode active.')
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_connection_info(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.signalr.get_connection_info()
    assert isinstance(response, GetConnectionInfoModel)
