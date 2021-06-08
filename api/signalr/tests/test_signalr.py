import pytest
from pytest_mock import MockerFixture
from api.signalr import SignalR
from api.signalr.responsemodels import *
from pybitcoin.networks import StraxMain, CirrusMain


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if SignalR.route + '/' in endpoint:
            assert endpoint in SignalR.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if SignalR.route + '/' in endpoint:
            assert endpoint in SignalR.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if SignalR.route + '/' in endpoint:
            assert endpoint in SignalR.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if SignalR.route + '/' in endpoint:
            assert endpoint in SignalR.endpoints


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_connection_info(mocker: MockerFixture, network, fakeuri):
    data = {
        'signalRUri': 'http://localhost',
        'signalRPort': 17104
    }
    mocker.patch.object(SignalR, 'get', return_value=data)
    signalr = SignalR(network=network, baseuri=fakeuri)

    response = signalr.get_connection_info()

    assert response == GetConnectionInfoModel(**data)
    # noinspection PyUnresolvedReferences
    signalr.get.assert_called_once()
