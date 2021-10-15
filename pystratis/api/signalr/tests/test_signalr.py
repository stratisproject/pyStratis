import pytest
from pytest_mock import MockerFixture
from pystratis.api.signalr import SignalR
from pystratis.api.signalr.responsemodels import *
from pystratis.core.networks import StraxMain, CirrusMain


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_connection_info(mocker: MockerFixture, network):
    data = {
        'signalRUri': 'http://localhost',
        'signalRPort': 17104
    }
    mocker.patch.object(SignalR, 'get', return_value=data)
    signalr = SignalR(network=network, baseuri=mocker.MagicMock())

    response = signalr.get_connection_info()

    assert response == GetConnectionInfoModel(**data)
    # noinspection PyUnresolvedReferences
    signalr.get.assert_called_once()
