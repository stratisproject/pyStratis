import pytest
from pytest_mock import MockerFixture
from api.diagnostic import Diagnostic
from api.diagnostic.requestmodels import *
from api.diagnostic.responsemodels import *
from pybitcoin.networks import StraxMain, CirrusMain


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Diagnostic.route + '/' in endpoint:
            assert endpoint in Diagnostic.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Diagnostic.route + '/' in endpoint:
            assert endpoint in Diagnostic.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Diagnostic.route + '/' in endpoint:
            assert endpoint in Diagnostic.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Diagnostic.route + '/' in endpoint:
            assert endpoint in Diagnostic.endpoints


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_connected_peers_info(mocker: MockerFixture, network, fakeuri):
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
    diagnostic = Diagnostic(network=network, baseuri=fakeuri)

    response = diagnostic.get_connectedpeers_info()

    assert response == GetConnectedPeersInfoModel(**data)
    # noinspection PyUnresolvedReferences
    diagnostic.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_status(mocker: MockerFixture, network, fakeuri):
    data = {'peerStatistics': 'Enabled'}
    mocker.patch.object(Diagnostic, 'get', return_value=data)
    diagnostic = Diagnostic(network=network, baseuri=fakeuri)

    response = diagnostic.get_status()

    assert response == GetStatusModel(**data)
    # noinspection PyUnresolvedReferences
    diagnostic.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_peer_statistics(mocker: MockerFixture, network, fakeuri):
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
    diagnostic = Diagnostic(network=network, baseuri=fakeuri)
    request_model = GetPeerStatisticsRequest(
        connected_only=True
    )

    response = diagnostic.get_peer_statistics(request_model)

    assert response == [PeerStatisticsModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    diagnostic.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_start_collecting_peer_statistics(mocker: MockerFixture, network, fakeuri):
    data = 'Diagnostic Peer Statistic Collector enabled.'
    mocker.patch.object(Diagnostic, 'get', return_value=data)
    diagnostic = Diagnostic(network=network, baseuri=fakeuri)

    response = diagnostic.start_collecting_peerstatistics()

    assert response == data
    # noinspection PyUnresolvedReferences
    diagnostic.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_stop_collecting_peer_statistics(mocker: MockerFixture, network, fakeuri):
    data = 'Diagnostic Peer Statistic Collector disabled.'
    mocker.patch.object(Diagnostic, 'get', return_value=data)
    diagnostic = Diagnostic(network=network, baseuri=fakeuri)

    response = diagnostic.stop_collecting_peerstatistics()

    assert response == data
    # noinspection PyUnresolvedReferences
    diagnostic.get.assert_called_once()
