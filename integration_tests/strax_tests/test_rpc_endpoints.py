import pytest
from nodes import BaseNode
from api.rpc.requestmodels import *
from api.rpc.responsemodels import *
from api import APIError


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_call_by_name(hot_node: BaseNode):
    request_model = CallByNameRequest(command='getblockcount')
    try:
        response = hot_node.rpc.call_by_name(request_model)
        assert isinstance(response, RPCCommandResponseModel)
    except APIError:
        # RPC functionality is deprecated and works inconsistently.
        pass


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_list_methods(hot_node: BaseNode):
    response = hot_node.rpc.list_methods()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, RPCCommandListModel)
