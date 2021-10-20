import pytest
from pytest_mock import MockerFixture
from pystratis.api.externalapi import ExternalAPI
from pystratis.core.networks import StraxMain, CirrusMain
from pystratis.core.types import Money


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_estimate_conversion_gas(mocker: MockerFixture, network):
    data = 79000000000000000
    mocker.patch.object(ExternalAPI, 'get', return_value=data)
    externalapi = ExternalAPI(network=network, baseuri=mocker.MagicMock())

    response = externalapi.estimate_conversion_gas()

    assert response == data
    # noinspection PyUnresolvedReferences
    externalapi.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_estimate_conversion_fee(mocker: MockerFixture, network):
    data = 236.77982178217823
    mocker.patch.object(ExternalAPI, 'get', return_value=data)
    externalapi = ExternalAPI(network=network, baseuri=mocker.MagicMock())

    response = externalapi.estimate_conversion_fee()

    assert response == Money(data)
    # noinspection PyUnresolvedReferences
    externalapi.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_gas_price(mocker: MockerFixture, network):
    data = 100
    mocker.patch.object(ExternalAPI, 'get', return_value=data)
    externalapi = ExternalAPI(network=network, baseuri=mocker.MagicMock())

    response = externalapi.gas_price()

    assert response == data
    # noinspection PyUnresolvedReferences
    externalapi.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_stratis_price(mocker: MockerFixture, network):
    data = 100.00
    mocker.patch.object(ExternalAPI, 'get', return_value=data)
    externalapi = ExternalAPI(network=network, baseuri=mocker.MagicMock())

    response = externalapi.stratis_price()

    assert response == Money(data)
    # noinspection PyUnresolvedReferences
    externalapi.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_stratis_price(mocker: MockerFixture, network):
    data = 5000.00
    mocker.patch.object(ExternalAPI, 'get', return_value=data)
    externalapi = ExternalAPI(network=network, baseuri=mocker.MagicMock())

    response = externalapi.ethereum_price()

    assert response == Money(data)
    # noinspection PyUnresolvedReferences
    externalapi.get.assert_called_once()
