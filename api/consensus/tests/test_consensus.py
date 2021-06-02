import pytest
from pytest_mock import MockerFixture
from api.consensus import Consensus
from api.consensus.requestmodels import *
from api.consensus.responsemodels import *
from pybitcoin.networks import StraxMain, CirrusMain


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Consensus.route + '/' in endpoint:
            assert endpoint in Consensus.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Consensus.route + '/' in endpoint:
            assert endpoint in Consensus.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Consensus.route + '/' in endpoint:
            assert endpoint in Consensus.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Consensus.route + '/' in endpoint:
            assert endpoint in Consensus.endpoints


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_deployment_flags(mocker: MockerFixture, network, fakeuri):
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
    consensus = Consensus(network=network, baseuri=fakeuri)

    response = consensus.deployment_flags()

    assert response == [DeploymentFlagsModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    consensus.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_best_block_hash(mocker: MockerFixture, network, fakeuri, generate_uint256):
    data = generate_uint256
    mocker.patch.object(Consensus, 'get', return_value=data)
    consensus = Consensus(network=network, baseuri=fakeuri)

    response = consensus.get_best_blockhash()

    assert response
    # noinspection PyUnresolvedReferences
    consensus.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_block_hash(mocker: MockerFixture, network, fakeuri, generate_uint256):
    data = generate_uint256
    mocker.patch.object(Consensus, 'get', return_value=data)
    consensus = Consensus(network=network, baseuri=fakeuri)
    request_model = GetBlockHashRequest(
        height=10
    )

    response = consensus.get_blockhash(request_model)

    assert response
    # noinspection PyUnresolvedReferences
    consensus.get.assert_called_once()
