import pytest
from pytest_mock import MockerFixture
from api.rpc import RPC
from api.rpc.requestmodels import *
from api.rpc.responsemodels import *
from pybitcoin.networks import StraxMain, CirrusMain


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if RPC.route + '/' in endpoint:
            assert endpoint in RPC.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if RPC.route + '/' in endpoint:
            assert endpoint in RPC.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if RPC.route + '/' in endpoint:
            assert endpoint in RPC.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if RPC.route + '/' in endpoint:
            assert endpoint in RPC.endpoints


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_call_by_name(mocker: MockerFixture, network, fakeuri):
    data = {
        'value': {
            'test': 0
        }
    }
    mocker.patch.object(RPC, 'post', return_value=data)
    rpc = RPC(network=network, baseuri=fakeuri)
    request_model = CallByNameRequest(
        command='rpccommand'
    )

    response = rpc.call_by_name(request_model)

    assert response == RPCCommandResponseModel(**data)
    # noinspection PyUnresolvedReferences
    rpc.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_list_methods(mocker: MockerFixture, network, fakeuri):
    data = [
        {
            'command': 'rpccommend',
            'description': 'description'
        }
    ]
    mocker.patch.object(RPC, 'get', return_value=data)
    rpc = RPC(network=network, baseuri=fakeuri)

    response = rpc.list_methods()

    assert response == [RPCCommandListModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    rpc.get.assert_called_once()
