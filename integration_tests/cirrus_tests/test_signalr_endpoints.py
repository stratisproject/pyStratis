import pytest
from api.signalr.responsemodels import *
from nodes import BaseNode


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_connection_info(cirrus_hot_node: BaseNode):
    response = cirrus_hot_node.signalr.get_connection_info()
    assert isinstance(response, GetConnectionInfoModel)
