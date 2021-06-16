import pytest
from api.signalr.responsemodels import *
from nodes import CirrusNode


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_connection_info(cirrus_syncing_node: CirrusNode):
    response = cirrus_syncing_node.signalr.get_connection_info()
    assert isinstance(response, GetConnectionInfoModel)
