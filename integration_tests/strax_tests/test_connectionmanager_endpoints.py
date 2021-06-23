import pytest
from nodes import BaseNode
from api.connectionmanager.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_add_node(strax_hot_node: BaseNode, strax_syncing_node: BaseNode, get_node_endpoint):
    assert strax_hot_node.connection_manager.addnode(endpoint=get_node_endpoint(strax_syncing_node), command='add')


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_peerinfo(strax_hot_node: BaseNode, strax_syncing_node: BaseNode, get_node_endpoint):
    response = strax_hot_node.connection_manager.getpeerinfo()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, PeerInfoModel)
