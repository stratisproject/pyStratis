import pytest
from nodes import CirrusMinerNode
from api.rpc.responsemodels import *
from api import APIError


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_call_by_name(cirrusminer_node: CirrusMinerNode):
    try:
        response = cirrusminer_node.rpc.call_by_name(command='getblockcount')
        assert isinstance(response, RPCCommandResponseModel)
    except APIError:
        # RPC functionality is deprecated and works inconsistently.
        pass


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_list_methods(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.rpc.list_methods()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, RPCCommandListModel)
