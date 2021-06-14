import pytest
from api.signalr.responsemodels import *
from nodes import BaseNode


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_connection_info(hot_node: BaseNode):
    response = hot_node.signalr.get_connection_info()
    assert isinstance(response, GetConnectionInfoModel)