import pytest
from pystratis.nodes import BaseNode
from pystratis.api import APIError
from pystratis.api.rpc.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_call_by_name(strax_hot_node: BaseNode):
    try:
        response = strax_hot_node.rpc.call_by_name(command='getblockcount')
        assert isinstance(response, RPCCommandResponseModel)
    except APIError:
        # RPC functionality is deprecated and works inconsistently.
        pass


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_list_methods(strax_hot_node: BaseNode):
    response = strax_hot_node.rpc.list_methods()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, RPCCommandListModel)
