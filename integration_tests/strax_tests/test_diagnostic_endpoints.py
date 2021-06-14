import pytest
from nodes import StraxNode
from api.diagnostic.requestmodels import *
from api.diagnostic.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_connected_peers_info(hot_node: StraxNode):
    response = hot_node.diagnostic.get_connectedpeers_info()
    assert isinstance(response, GetConnectedPeersInfoModel)
    for item in response.peers_by_peer_id:
        assert isinstance(item, ConnectedPeerInfoModel)
    for item in response.connected_peers:
        assert isinstance(item, ConnectedPeerInfoModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_status(hot_node: StraxNode):
    response = hot_node.diagnostic.get_status()
    assert isinstance(response, GetStatusModel)
    assert response.peer_statistics in ['Enabled', 'Disabled']


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_peer_statistics(hot_node: StraxNode):
    request_model = GetPeerStatisticsRequest(connected_only=True)
    response = hot_node.diagnostic.get_peer_statistics(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, PeerStatisticsModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_start_collecting_peer_statistics(hot_node: StraxNode):
    response = hot_node.diagnostic.start_collecting_peerstatistics()
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_stop_collecting_peer_statistics(hot_node: StraxNode):
    response = hot_node.diagnostic.stop_collecting_peerstatistics()
    assert isinstance(response, str)
