import pytest
from pystratis.nodes import CirrusMinerNode
from pystratis.api import APIError
from pystratis.api.rpc.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_call_by_name(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.rpc.call_by_name(command='getblockcount')
    assert isinstance(response, int)
    parameters = {'height': response}
    response = cirrusminer_node.rpc.call_by_name(command='getblockhash', parameters=parameters)
    assert isinstance(response, str)
    parameters = {'hash': response}
    response = cirrusminer_node.rpc.call_by_name(command='getblockheader', parameters=parameters)
    assert isinstance(response, dict)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_list_methods(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.rpc.list_methods()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, RPCCommandListModel)
