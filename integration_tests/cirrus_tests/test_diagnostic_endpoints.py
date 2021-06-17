import pytest
from nodes import CirrusMinerNode
from api.diagnostic.requestmodels import *
from api.diagnostic.responsemodels import *


@pytest.mark.skip(reason='Endpoint not active for cirrus network with devmode active.')
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_connected_peers_info(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.diagnostic.get_connectedpeers_info()
    assert isinstance(response, GetConnectedPeersInfoModel)
    for item in response.peers_by_peer_id:
        assert isinstance(item, ConnectedPeerInfoModel)
    for item in response.connected_peers:
        assert isinstance(item, ConnectedPeerInfoModel)


@pytest.mark.skip(reason='Endpoint not active for cirrus network with devmode active.')
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_status(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.diagnostic.get_status()
    assert isinstance(response, GetStatusModel)
    assert response.peer_statistics in ['Enabled', 'Disabled']


@pytest.mark.skip(reason='Endpoint not active for cirrus network with devmode active.')
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_peer_statistics(cirrusminer_node: CirrusMinerNode):
    request_model = GetPeerStatisticsRequest(connected_only=True)
    response = cirrusminer_node.diagnostic.get_peer_statistics(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, PeerStatisticsModel)


@pytest.mark.skip(reason='Endpoint not active for cirrus network with devmode active.')
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_start_collecting_peer_statistics(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.diagnostic.start_collecting_peerstatistics()
    assert isinstance(response, str)


@pytest.mark.skip(reason='Endpoint not active for cirrus network with devmode active.')
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_stop_collecting_peer_statistics(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.diagnostic.stop_collecting_peerstatistics()
    assert isinstance(response, str)
