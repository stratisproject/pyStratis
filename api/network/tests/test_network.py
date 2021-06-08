import pytest
from pytest_mock import MockerFixture
from api.network import Network
from api.network.requestmodels import *
from api.network.responsemodels import *
from pybitcoin.networks import StraxMain, CirrusMain


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Network.route + '/' in endpoint:
            assert endpoint in Network.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Network.route + '/' in endpoint:
            assert endpoint in Network.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Network.route + '/' in endpoint:
            assert endpoint in Network.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Network.route + '/' in endpoint:
            assert endpoint in Network.endpoints


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_disconnect(mocker: MockerFixture, network, fakeuri):
    data = None
    mocker.patch.object(Network, 'post', return_value=data)
    network_controller = Network(network=network, baseuri=fakeuri)
    request_model = DisconnectPeerRequest(
        peer_address='http://peeraddress'
    )

    network_controller.disconnect(request_model)

    # noinspection PyUnresolvedReferences
    network_controller.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_setban(mocker: MockerFixture, network, fakeuri):
    data = None
    mocker.patch.object(Network, 'post', return_value=data)
    network_controller = Network(network=network, baseuri=fakeuri)
    request_model = SetBanRequest(
        ban_command='add',
        ban_duration_seconds=60,
        peer_address='http://localhost'
    )

    network_controller.set_ban(request_model)

    # noinspection PyUnresolvedReferences
    network_controller.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getbans(mocker: MockerFixture, network, fakeuri):
    data = [
        {
            'EndPoint': 'http://badpeer0',
            'BanUntil': 'Forever',
            'BanReason': 'Scammer'
        },
        {
            'EndPoint': 'http://badpeer1',
            'BanUntil': 'Forever',
            'BanReason': 'Scammer'
        }
    ]
    mocker.patch.object(Network, 'get', return_value=data)
    network_controller = Network(network=network, baseuri=fakeuri)

    response = network_controller.get_bans()

    assert response == [BannedPeerModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    network_controller.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_clear_banned(mocker: MockerFixture, network, fakeuri):
    data = None
    mocker.patch.object(Network, 'post', return_value=data)
    network_controller = Network(network=network, baseuri=fakeuri)
    request_model = ClearBannedRequest()

    network_controller.clear_banned(request_model)

    # noinspection PyUnresolvedReferences
    network_controller.post.assert_called_once()
