import pytest
from nodes import CirrusNode, CirrusMinerNode
from api.connectionmanager.requestmodels import *
from api.connectionmanager.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_add_node(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode, get_node_endpoint):
    request_model = AddNodeRequest(endpoint=get_node_endpoint(cirrus_syncing_node), command='onetry')
    assert cirrusminer_node.connection_manager.addnode(request_model)

    request_model = AddNodeRequest(endpoint=get_node_endpoint(cirrusminer_node), command='onetry')
    assert cirrus_syncing_node.connection_manager.addnode(request_model)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_peerinfo(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode, get_node_endpoint):
    response = cirrusminer_node.connection_manager.getpeerinfo()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, PeerInfoModel)

    response = cirrus_syncing_node.connection_manager.getpeerinfo()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, PeerInfoModel)
