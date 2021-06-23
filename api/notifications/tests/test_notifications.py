import pytest
from pytest_mock import MockerFixture
from api.notifications import Notifications
from api.notifications.requestmodels import *
from pybitcoin.networks import StraxMain, CirrusMain


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths']]
    for endpoint in paths:
        if Notifications.route + '/' in endpoint:
            assert endpoint in Notifications.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths']]
    for endpoint in paths:
        if Notifications.route + '/' in endpoint:
            assert endpoint in Notifications.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths']]
    for endpoint in paths:
        if Notifications.route + '/' in endpoint:
            assert endpoint in Notifications.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths']]
    for endpoint in paths:
        if Notifications.route + '/' in endpoint:
            assert endpoint in Notifications.endpoints


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_sync(mocker: MockerFixture, network, fakeuri, generate_uint256):
    data = None
    mocker.patch.object(Notifications, 'get', return_value=data)
    notifications = Notifications(network=network, baseuri=fakeuri)

    notifications.sync(sync_from=generate_uint256)

    # noinspection PyUnresolvedReferences
    notifications.get.assert_called_once()
