import pytest
from pytest_mock import MockerFixture
from pystratis.api.federation.responsemodels import *
from pystratis.api.federation import Federation
from pystratis.core.networks import StraxMain, CirrusMain


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_reconstruct(mocker: MockerFixture, network):
    data = "Reconstruction flag set, please restart the node."
    mocker.patch.object(Federation, 'put', return_value=data)
    federation = Federation(network=network, baseuri=mocker.MagicMock())

    response = federation.reconstruct()

    assert response == data
    # noinspection PyUnresolvedReferences
    federation.put.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_members_current(mocker: MockerFixture, network, generate_compressed_pubkey, get_datetime):
    data = {
        "pollStartBlockHeight": None,
        "pollNumberOfVotesAcquired": None,
        "pollFinishedBlockHeight": None,
        "pollWillFinishInBlocks": None,
        "pollExecutedBlockHeight": None,
        "memberWillStartMiningAtBlockHeight": None,
        "memberWillStartEarningRewardsEstimateHeight": None,
        "pollType": None,
        "rewardEstimatePerBlock": 0.05,
        "pubkey": generate_compressed_pubkey,
        "collateralAmount": 50000,
        "lastActiveTime": get_datetime(5),
        "periodOfInactivity": "00:02:32.9200000"
    }

    mocker.patch.object(Federation, 'get', return_value=data)
    federation = Federation(network=network, baseuri=mocker.MagicMock())

    response = federation.members_current()

    assert response == FederationMemberDetailedModel(**data)
    # noinspection PyUnresolvedReferences
    federation.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_member(mocker: MockerFixture, network, generate_compressed_pubkey, get_datetime):
    data = [
        {
            "pubkey": generate_compressed_pubkey,
            "collateralAmount": 50000,
            "lastActiveTime": get_datetime(5),
            "periodOfInactivity": "00:02:32.9200000"
        },
        {
            "pubkey": generate_compressed_pubkey,
            "collateralAmount": 50000,
            "lastActiveTime": get_datetime(5),
            "periodOfInactivity": "00:02:33.9200000"
        },
        {
            "pubkey": generate_compressed_pubkey,
            "collateralAmount": 50000,
            "lastActiveTime": get_datetime(5),
            "periodOfInactivity": "00:02:34.9200000"
        }
    ]

    mocker.patch.object(Federation, 'get', return_value=data)
    federation = Federation(network=network, baseuri=mocker.MagicMock())

    response = federation.members()

    assert response == [FederationMemberModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    federation.get.assert_called_once()
