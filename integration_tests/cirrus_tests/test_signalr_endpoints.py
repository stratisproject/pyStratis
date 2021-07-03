import pytest
from pystratis.nodes import CirrusNode
from pystratis.api.signalr.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_connection_info(cirrus_node: CirrusNode):
    response = cirrus_node.signalr.get_connection_info()
    assert isinstance(response, GetConnectionInfoModel)
