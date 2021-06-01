import pytest
from pytest_mock import MockerFixture
from api.balances import Balances
from api.balances.requestmodels import *
from pybitcoin import Address
from pybitcoin.networks import StraxMain, CirrusMain


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Balances.route + '/' in endpoint:
            assert endpoint in Balances.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Balances.route + '/' in endpoint:
            assert endpoint in Balances.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Balances.route + '/' in endpoint:
            assert endpoint in Balances.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Balances.route + '/' in endpoint:
            assert endpoint in Balances.endpoints


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_overamountatheight(mocker: MockerFixture, network, fakeuri, overamountatheightresponse):
    data = overamountatheightresponse(network)
    mocker.patch.object(Balances, 'get', return_value=data)
    balances = Balances(network=network, baseuri=fakeuri)
    request_model = OverAmountAtHeightRequest(block_height=10, amount=10)

    response = balances.over_amount_at_height(request_model)

    assert len(response) == len(data)
    for i in range(len(response)):
        assert isinstance(response[i], Address)
        assert response[i] == data[i]
    # noinspection PyUnresolvedReferences
    balances.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_overamountatheight_none(mocker: MockerFixture, network, fakeuri):
    data = []
    mocker.patch.object(Balances, 'get', return_value=data)
    balances = Balances(network=network, baseuri=fakeuri)
    request_model = OverAmountAtHeightRequest(block_height=10, amount=10)

    response = balances.over_amount_at_height(request_model)

    assert len(response) == len(data)
    for i in range(len(response)):
        assert isinstance(response[i], Address)
        assert response[i] == data[i]
    # noinspection PyUnresolvedReferences
    balances.get.assert_called_once()
