import pytest
import time
from nodes import StraxNode
from api.diagnostic.requestmodels import *
from api.diagnostic.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_connected_peers_info(strax_hot_node: StraxNode):
    response = strax_hot_node.diagnostic.get_connectedpeers_info()
    assert isinstance(response, GetConnectedPeersInfoModel)
    for item in response.peers_by_peer_id:
        assert isinstance(item, ConnectedPeerInfoModel)
    for item in response.connected_peers:
        assert isinstance(item, ConnectedPeerInfoModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_status(strax_hot_node: StraxNode):
    response = strax_hot_node.diagnostic.get_status()
    assert isinstance(response, GetStatusModel)
    assert response.peer_statistics in ['Enabled', 'Disabled']


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_peer_statistics(strax_hot_node: StraxNode):
    strax_hot_node.diagnostic.start_collecting_peerstatistics()
    # collect some stats
    time.sleep(20)
    request_model = GetPeerStatisticsRequest(connected_only=True)
    response = strax_hot_node.diagnostic.get_peer_statistics(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, PeerStatisticsModel)
    strax_hot_node.diagnostic.stop_collecting_peerstatistics()


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_start_collecting_peer_statistics(strax_hot_node: StraxNode):
    response = strax_hot_node.diagnostic.start_collecting_peerstatistics()
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_stop_collecting_peer_statistics(strax_hot_node: StraxNode):
    response = strax_hot_node.diagnostic.stop_collecting_peerstatistics()
    assert isinstance(response, str)
