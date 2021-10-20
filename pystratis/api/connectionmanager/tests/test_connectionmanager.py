import pytest
from pytest_mock import MockerFixture
from pystratis.api.connectionmanager import ConnectionManager
from pystratis.api.connectionmanager.responsemodels import *
from pystratis.core.networks import StraxMain, CirrusMain


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_addnode(mocker: MockerFixture, network):
    data = True
    mocker.patch.object(ConnectionManager, 'get', return_value=data)
    connection_manager = ConnectionManager(network=network, baseuri=mocker.MagicMock())

    response = connection_manager.addnode(ipaddr='http://localhost', command='add')

    assert response
    # noinspection PyUnresolvedReferences
    connection_manager.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getpeerinfo(mocker: MockerFixture, network):
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
    connection_manager = ConnectionManager(network=network, baseuri=mocker.MagicMock())

    response = connection_manager.getpeerinfo()

    assert response == [PeerInfoModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    connection_manager.get.assert_called_once()
