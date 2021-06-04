import pytest
from pytest_mock import MockerFixture
from api.connectionmanager import ConnectionManager
from api.connectionmanager.requestmodels import *
from api.connectionmanager.responsemodels import *
from pybitcoin.networks import StraxMain, CirrusMain


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if ConnectionManager.route + '/' in endpoint:
            assert endpoint in ConnectionManager.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if ConnectionManager.route + '/' in endpoint:
            assert endpoint in ConnectionManager.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if ConnectionManager.route + '/' in endpoint:
            assert endpoint in ConnectionManager.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if ConnectionManager.route + '/' in endpoint:
            assert endpoint in ConnectionManager.endpoints


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_addnode(mocker: MockerFixture, network, fakeuri):
    data = True
    mocker.patch.object(ConnectionManager, 'get', return_value=data)
    connection_manager = ConnectionManager(network=network, baseuri=fakeuri)
    request_model = AddNodeRequest(
        endpoint='http://localhost',
        command='add'
    )

    response = connection_manager.addnode(request_model)

    assert response
    # noinspection PyUnresolvedReferences
    connection_manager.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getpeerinfo(mocker: MockerFixture, network, fakeuri):
    data = [
        {
            "id": 0,
            "addr": "[::ffff:x.x.x.x]:17105",
            "addrlocal": "[::ffff:x.x.x.x]:52424",
            "services": "9",
            "relaytxes": False,
            "lastsend": 0,
            "lastrecv": 0,
            "bytessent": 0,
            "bytesrecv": 0,
            "conntime": 0,
            "timeoffset": 0,
            "pingtime": 0,
            "minping": 0,
            "pingwait": 0,
            "version": 70012,
            "subver": "StratisFullNode:1.x.x.x (70012)",
            "inbound": False,
            "addnode": False,
            "startingheight": 378614,
            "banscore": 0,
            "synced_headers": 0,
            "synced_blocks": 0,
            "whitelisted": False,
            "inflight": None,
            "bytessent_per_msg": None,
            "bytesrecv_per_msg": None
        },
        {
            "id": 1,
            "addr": "[::ffff:x.x.x.x]:17105",
            "addrlocal": "[::ffff:x.x.x.x]:33104",
            "services": "9",
            "relaytxes": False,
            "lastsend": 0,
            "lastrecv": 0,
            "bytessent": 0,
            "bytesrecv": 0,
            "conntime": 0,
            "timeoffset": 0,
            "pingtime": 0,
            "minping": 0,
            "pingwait": 0,
            "version": 70012,
            "subver": "StratisFullNode:1.x.x.x (70012)",
            "inbound": False,
            "addnode": False,
            "startingheight": 379357,
            "banscore": 0,
            "synced_headers": 0,
            "synced_blocks": 0,
            "whitelisted": False,
            "inflight": None,
            "bytessent_per_msg": None,
            "bytesrecv_per_msg": None
        }
    ]
    mocker.patch.object(ConnectionManager, 'get', return_value=data)
    connection_manager = ConnectionManager(network=network, baseuri=fakeuri)

    response = connection_manager.getpeerinfo()

    assert response == [PeerInfoModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    connection_manager.get.assert_called_once()
