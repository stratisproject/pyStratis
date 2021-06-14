import pytest
import time
from nodes import BaseNode
from api.connectionmanager.requestmodels import *
from api.connectionmanager.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_add_node(hot_node: BaseNode, syncing_node: BaseNode, get_node_endpoint):
    request_model = AddNodeRequest(endpoint=get_node_endpoint(syncing_node), command='add')
    assert hot_node.connection_manager.addnode(request_model)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_peerinfo(hot_node: BaseNode, syncing_node: BaseNode, get_node_endpoint):
    while True:
        response = hot_node.connection_manager.getpeerinfo()
        assert isinstance(response, list)
        if len(response) == 1:
            assert isinstance(response[0], PeerInfoModel)
            assert response[0].addr == get_node_endpoint(syncing_node)
            break
        time.sleep(5)
