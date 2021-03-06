import pytest
from pystratis.nodes import StraxNode
from pystratis.api.signalr.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_connection_info(strax_hot_node: StraxNode):
    response = strax_hot_node.signalr.get_connection_info()
    assert isinstance(response, GetConnectionInfoModel)
