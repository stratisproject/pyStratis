import pytest
from pytest_mock import MockerFixture
from pystratis.api.consensus.responsemodels import *
from pystratis.api.consensus import Consensus
from pystratis.core.types import uint256
from pystratis.core.networks import StraxMain, CirrusMain


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_deployment_flags(mocker: MockerFixture, network):
    data = [
        {
            "deploymentName": "csv",
            "deploymentIndex": 0,
            "stateValue": 4,
            "thresholdState": "Active",
            "height": 381708,
            "sinceHeight": 0,
            "confirmationPeriod": 2016,
            "periodStartHeight": 381023,
            "periodEndHeight": 383039,
            "votes": 0,
            "blocks": 684,
            "versions": {
              "20000000": 684
            },
            "threshold": 1916,
            "timeStart": "1969-12-31T00:00:00",
            "timeTimeOut": "2001-09-09T00:00:00"
        },
        {
            "deploymentName": "segwit",
            "deploymentIndex": 1,
            "stateValue": 4,
            "thresholdState": "Active",
            "height": 381708,
            "sinceHeight": 0,
            "confirmationPeriod": 2016,
            "periodStartHeight": 381023,
            "periodEndHeight": 383039,
            "votes": 0,
            "blocks": 684,
            "versions": {
              "20000000": 684
            },
            "threshold": 1916,
            "timeStart": "1969-12-31T00:00:00",
            "timeTimeOut": "2001-09-09T00:00:00"
        },
        {
            "deploymentName": "coldstaking",
            "deploymentIndex": 2,
            "stateValue": 4,
            "thresholdState": "Active",
            "height": 381708,
            "sinceHeight": 0,
            "confirmationPeriod": 2016,
            "periodStartHeight": 381023,
            "periodEndHeight": 383039,
            "votes": 0,
            "blocks": 684,
            "versions": {
              "20000000": 684
            },
            "threshold": 1916,
            "timeStart": "1969-12-31T00:00:00",
            "timeTimeOut": "2001-09-09T00:00:00"
        }
    ]
    mocker.patch.object(Consensus, 'get', return_value=data)
    consensus = Consensus(network=network, baseuri=mocker.MagicMock())

    response = consensus.deployment_flags()

    assert response == [DeploymentFlagsModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    consensus.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_best_block_hash(mocker: MockerFixture, network, generate_uint256):
    data = generate_uint256
    mocker.patch.object(Consensus, 'get', return_value=data)
    consensus = Consensus(network=network, baseuri=mocker.MagicMock())

    response = consensus.get_best_blockhash()

    assert response == uint256(data)
    # noinspection PyUnresolvedReferences
    consensus.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_block_hash(mocker: MockerFixture, network, generate_uint256):
    data = generate_uint256
    mocker.patch.object(Consensus, 'get', return_value=data)
    consensus = Consensus(network=network, baseuri=mocker.MagicMock())

    response = consensus.get_blockhash(height=10)

    assert response == uint256(data)
    # noinspection PyUnresolvedReferences
    consensus.get.assert_called_once()
