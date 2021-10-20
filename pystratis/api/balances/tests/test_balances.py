import pytest
from pytest_mock import MockerFixture
from pystratis.api.balances import Balances
from pystratis.core.types import Address
from pystratis.core.networks import CirrusMain


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_overamountatheight(mocker: MockerFixture, network, overamountatheightresponse):
    data = overamountatheightresponse(network)
    mocker.patch.object(Balances, 'get', return_value=data)
    balances = Balances(network=network, baseuri=mocker.MagicMock())

    response = balances.over_amount_at_height(block_height=10, amount=10)

    assert len(response) == len(data)
    for i in range(len(response)):
        assert isinstance(response[i], Address)
        assert response[i] == data[i]
    # noinspection PyUnresolvedReferences
    balances.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_overamountatheight_none(mocker: MockerFixture, network):
    data = []
    mocker.patch.object(Balances, 'get', return_value=data)
    balances = Balances(network=network, baseuri=mocker.MagicMock())

    response = balances.over_amount_at_height(block_height=10, amount=10)

    assert len(response) == len(data)
    for i in range(len(response)):
        assert isinstance(response[i], Address)
        assert response[i] == data[i]
    # noinspection PyUnresolvedReferences
    balances.get.assert_called_once()
