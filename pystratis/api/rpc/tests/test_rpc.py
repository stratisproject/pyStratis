import pytest
from pytest_mock import MockerFixture
from pystratis.api.rpc import RPC
from pystratis.api.rpc.responsemodels import *
from pystratis.core.networks import StraxMain, CirrusMain


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_call_by_name(mocker: MockerFixture, network):
    data = 0
    mocker.patch.object(RPC, 'post', return_value=data)
    rpc = RPC(network=network, baseuri=mocker.MagicMock())

    response = rpc.call_by_name(command='getblockcount')

    assert response == data
    # noinspection PyUnresolvedReferences
    rpc.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_list_methods(mocker: MockerFixture, network):
    data = [
        {
            'command': 'rpccommend',
            'description': 'description'
        }
    ]
    mocker.patch.object(RPC, 'get', return_value=data)
    rpc = RPC(network=network, baseuri=mocker.MagicMock())

    response = rpc.list_methods()

    assert response == [RPCCommandListModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    rpc.get.assert_called_once()
