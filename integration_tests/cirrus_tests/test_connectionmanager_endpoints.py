import pytest
from nodes import CirrusMinerNode
from api.connectionmanager.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_add_node(cirrusminer_node: CirrusMinerNode, cirrusminer_syncing_node: CirrusMinerNode, get_node_endpoint):
    assert cirrusminer_node.connection_manager.addnode(
        ipaddr=get_node_endpoint(cirrusminer_syncing_node), command='onetry'
    )


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_peerinfo(cirrusminer_node: CirrusMinerNode, get_node_endpoint):
    response = cirrusminer_node.connection_manager.getpeerinfo()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, PeerInfoModel)
