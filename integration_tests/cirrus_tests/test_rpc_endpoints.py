import pytest
from nodes import CirrusMinerNode, CirrusNode
from api.rpc.requestmodels import *
from api.rpc.responsemodels import *
from api import APIError


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_call_by_name(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = CallByNameRequest(command='getblockcount')
    try:
        response = cirrusminer_node.rpc.call_by_name(request_model)
        assert isinstance(response, RPCCommandResponseModel)
    except APIError:
        # RPC functionality is deprecated and works inconsistently.
        pass

    try:
        response = cirrus_syncing_node.rpc.call_by_name(request_model)
        assert isinstance(response, RPCCommandResponseModel)
    except APIError:
        # RPC functionality is deprecated and works inconsistently.
        pass


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_list_methods(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    response = cirrusminer_node.rpc.list_methods()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, RPCCommandListModel)

    response = cirrus_syncing_node.rpc.list_methods()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, RPCCommandListModel)
