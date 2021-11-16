import pytest
from pytest_mock import MockerFixture
from pystratis.api.voting import Voting
from pystratis.api.voting.requestmodels import *
from pystratis.api.voting.responsemodels import *
from pystratis.core.networks import CirrusMain
from pystratis.api.global_responsemodels import PollViewModel


def test_missing_one_poll_request_item_is_ok(generate_compressed_pubkey):
    PollsRequest(
            vote_type=VoteKey.KickFederationMember
        )
    PollsRequest(
        pubkey_of_member_being_voted_on=generate_compressed_pubkey
    )


def test_missing_one_poll_request_item_is_raises_exception():
    with pytest.raises(ValueError):
        PollsRequest()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_executed_polls(mocker: MockerFixture, network, generate_uint256, generate_compressed_pubkey, generate_p2pkh_address):
    kicked_pubkey = generate_compressed_pubkey
    kicked_address = generate_p2pkh_address
    data = [
        {
            'IsPending': False,
            'IsExecuted': True,
            'Id': 1,
            'PollVotedInFavorBlockDataHash': generate_uint256,
            'PollVotedInFavorBlockDataHeight': 1414151,
            'PollStartFavorBlockDataHash': generate_uint256,
            'PollStartFavorBlockDataHeight': 1414141,
            'PollExecutedBlockDataHash': generate_uint256,
            'PollExecutedBlockDataHeight': 1414161,
            'PubKeysHexVotedInFavor': [
                generate_compressed_pubkey,
                generate_compressed_pubkey,
                generate_compressed_pubkey,
                generate_compressed_pubkey,
                generate_compressed_pubkey
            ],
            'VotingDataString': f"Action:'{VoteKey.KickFederationMember.name}',FederationMember:'PubKey:'{kicked_pubkey}',CollateralAmount:50000.00000000,CollateralMainchainAddress:{kicked_address}'"
        }
    ]
    mocker.patch.object(Voting, 'get', return_value=data)
    voting = Voting(network=network, baseuri=mocker.MagicMock())
    response = voting.executed_polls(
        vote_type=VoteKey.KickFederationMember,
        pubkey_of_member_being_voted_on=generate_compressed_pubkey
    )
    assert response == [PollViewModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    voting.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_pending_polls(mocker: MockerFixture, network, generate_compressed_pubkey, generate_p2pkh_address, generate_uint256):
    kicked_pubkey = generate_compressed_pubkey
    kicked_address = generate_p2pkh_address
    data = [
        {
            'IsPending': True,
            'IsExecuted': False,
            'Id': 1,
            'PollVotedInFavorBlockDataHash': generate_uint256,
            'PollVotedInFavorBlockDataHeight': 1414151,
            'PollStartFavorBlockDataHash': generate_uint256,
            'PollStartFavorBlockDataHeight': 1414141,
            'PollExecutedBlockDataHash': None,
            'PollExecutedBlockDataHeight': None,
            'PubKeysHexVotedInFavor': [
                generate_compressed_pubkey,
                generate_compressed_pubkey,
                generate_compressed_pubkey,
            ],
            'VotingDataString': f"Action:'{VoteKey.KickFederationMember.name}',FederationMember:'PubKey:'{kicked_pubkey}',CollateralAmount:50000.00000000,CollateralMainchainAddress:{kicked_address}'"
        }
    ]
    mocker.patch.object(Voting, 'get', return_value=data)
    voting = Voting(network=network, baseuri=mocker.MagicMock())
    response = voting.pending_polls(
        vote_type=VoteKey.KickFederationMember,
        pubkey_of_member_being_voted_on=kicked_pubkey
    )
    assert response == [PollViewModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    voting.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_finished_polls(mocker: MockerFixture, network, generate_uint256, generate_compressed_pubkey, generate_p2pkh_address):
    kicked_pubkey = generate_compressed_pubkey
    kicked_address = generate_p2pkh_address
    data = [
        {
            'IsPending': False,
            'IsExecuted': True,
            'Id': 1,
            'PollVotedInFavorBlockDataHash': generate_uint256,
            'PollVotedInFavorBlockDataHeight': 1414151,
            'PollStartFavorBlockDataHash': generate_uint256,
            'PollStartFavorBlockDataHeight': 1414141,
            'PollExecutedBlockDataHash': generate_uint256,
            'PollExecutedBlockDataHeight': 1414161,
            'PubKeysHexVotedInFavor': [
                generate_compressed_pubkey,
                generate_compressed_pubkey,
                generate_compressed_pubkey,
                generate_compressed_pubkey,
                generate_compressed_pubkey
            ],
            'VotingDataString': f"Action:'{VoteKey.KickFederationMember.name}',FederationMember:'PubKey:'{kicked_pubkey}',CollateralAmount:50000.00000000,CollateralMainchainAddress:{kicked_address}'"
        }
    ]
    mocker.patch.object(Voting, 'get', return_value=data)
    voting = Voting(network=network, baseuri=mocker.MagicMock())
    response = voting.finished_polls(
        vote_type=VoteKey.KickFederationMember,
        pubkey_of_member_being_voted_on=generate_compressed_pubkey
    )
    assert response == [PollViewModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    voting.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_scheduledvote_whitelisthash(mocker: MockerFixture, network, generate_uint256):
    mocker.patch.object(Voting, 'post', return_value=None)
    voting = Voting(network=network, baseuri=mocker.MagicMock())
    voting.schedulevote_whitelisthash(hash_id=generate_uint256)
    # noinspection PyUnresolvedReferences
    voting.post.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_scheduledvote_removehash(mocker: MockerFixture, network, generate_uint256):
    mocker.patch.object(Voting, 'post', return_value=None)
    voting = Voting(network=network, baseuri=mocker.MagicMock())
    voting.schedulevote_removehash(hash_id=generate_uint256)
    # noinspection PyUnresolvedReferences
    voting.post.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_whitelistedhashes(mocker: MockerFixture, network, generate_uint256):
    data = [
        {
            'hash': generate_uint256
        },
        {
            'hash': generate_uint256
        },
        {
            'hash': generate_uint256
        },
    ]
    mocker.patch.object(Voting, 'get', return_value=data)
    voting = Voting(network=network, baseuri=mocker.MagicMock())
    response = voting.whitelisted_hashes()
    assert response == [WhitelistedHashesModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    voting.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_scheduledvotes(mocker: MockerFixture, network, generate_uint256, generate_compressed_pubkey):
    data = [
        {
            'key': generate_compressed_pubkey,
            'hash': generate_uint256
        },
        {
            'key': generate_compressed_pubkey,
            'hash': generate_uint256
        },
        {
            'key': generate_compressed_pubkey,
            'hash': generate_uint256
        },
    ]
    mocker.patch.object(Voting, 'get', return_value=data)
    voting = Voting(network=network, baseuri=mocker.MagicMock())
    response = voting.scheduled_votes()
    assert response == [VotingDataModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    voting.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_polls_tip(mocker: MockerFixture, network):
    data = {
        "tipHeight": 10,
        "tipHeightPercentage": 100
    }
    mocker.patch.object(Voting, 'get', return_value=data)
    voting = Voting(network=network, baseuri=mocker.MagicMock())
    response = voting.polls_tip()
    assert response == PollsTipModel(**data)
    # noinspection PyUnresolvedReferences
    voting.get.assert_called_once()
