import pytest
from pytest_mock import MockerFixture
from pystratis.api.diagnostic import Diagnostic
from pystratis.api.diagnostic.responsemodels import *
from pystratis.core.networks import StraxMain, CirrusMain


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_connected_peers_info(mocker: MockerFixture, network):
    data = {
        'peersByPeerId': [
            {
                'isConnected': True,
                'disconnectReason': None,
                'state': 1,
                'endPoint': '[::ffff:x.x.x.x]:17105'
            }
        ],
        'connectedPeers': [
            {
                'isConnected': True,
                'disconnectReason': None,
                'state': 1,
                'endPoint': '[::ffff:x.x.x.x]:17105'
            }
        ],
        'connectedPeersNotInPeersByPeerId': [
            {
                'isConnected': True,
                'disconnectReason': None,
                'state': 1,
                'endPoint': '[::ffff:x.x.x.x]:17105'
            }

        ]
    }
    mocker.patch.object(Diagnostic, 'get', return_value=data)
    diagnostic = Diagnostic(network=network, baseuri=mocker.MagicMock())

    response = diagnostic.get_connectedpeers_info()

    assert response == GetConnectedPeersInfoModel(**data)
    # noinspection PyUnresolvedReferences
    diagnostic.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_status(mocker: MockerFixture, network):
    data = {'peerStatistics': 'Enabled'}
    mocker.patch.object(Diagnostic, 'get', return_value=data)
    diagnostic = Diagnostic(network=network, baseuri=mocker.MagicMock())

    response = diagnostic.get_status()

    assert response == GetStatusModel(**data)
    # noinspection PyUnresolvedReferences
    diagnostic.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_peer_statistics(mocker: MockerFixture, network):
    data = [
        {
            'peerEndPoint': '[::ffff:x.x.x.x]:17105',
            'connected': True,
            'inbound': True,
            'bytesSent': 0,
            'bytesReceived': 0,
            'receivedMessages': 0,
            'sentMessages': 0,
            'latestEvents': []
        },
        {
            'peerEndPoint': '[::ffff:x.x.x.x]:17105',
            'connected': True,
            'inbound': True,
            'bytesSent': 0,
            'bytesReceived': 0,
            'receivedMessages': 0,
            'sentMessages': 0,
            'latestEvents': []
        }
    ]
    mocker.patch.object(Diagnostic, 'get', return_value=data)
    diagnostic = Diagnostic(network=network, baseuri=mocker.MagicMock())

    response = diagnostic.get_peer_statistics(connected_only=True)

    assert response == [PeerStatisticsModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    diagnostic.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_start_collecting_peer_statistics(mocker: MockerFixture, network):
    data = 'Diagnostic Peer Statistic Collector enabled.'
    mocker.patch.object(Diagnostic, 'get', return_value=data)
    diagnostic = Diagnostic(network=network, baseuri=mocker.MagicMock())

    response = diagnostic.start_collecting_peerstatistics()

    assert response == data
    # noinspection PyUnresolvedReferences
    diagnostic.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_stop_collecting_peer_statistics(mocker: MockerFixture, network):
    data = 'Diagnostic Peer Statistic Collector disabled.'
    mocker.patch.object(Diagnostic, 'get', return_value=data)
    diagnostic = Diagnostic(network=network, baseuri=mocker.MagicMock())

    response = diagnostic.stop_collecting_peerstatistics()

    assert response == data
    # noinspection PyUnresolvedReferences
    diagnostic.get.assert_called_once()
