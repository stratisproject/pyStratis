import pytest
from pytest_mock import MockerFixture
from api.voting import Voting
from api.voting.requestmodels import *
from api.voting.responsemodels import *
from pybitcoin.networks import StraxMain, CirrusMain
from pybitcoin import PollViewModel


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths']]
    for endpoint in paths:
        if Voting.route + '/' in endpoint:
            assert endpoint in Voting.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths']]
    for endpoint in paths:
        if Voting.route + '/' in endpoint:
            assert endpoint in Voting.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths']]
    for endpoint in paths:
        if Voting.route + '/' in endpoint:
            assert endpoint in Voting.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Voting.route + '/' in endpoint:
            assert endpoint in Voting.endpoints


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


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
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
    voting = Voting(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())
    response = voting.executed_polls(
        vote_type=VoteKey.KickFederationMember,
        pubkey_of_member_being_voted_on=generate_compressed_pubkey
    )
    assert response == [PollViewModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    voting.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
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
    voting = Voting(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())
    response = voting.pending_polls(
        vote_type=VoteKey.KickFederationMember,
        pubkey_of_member_being_voted_on=kicked_pubkey
    )
    assert response == [PollViewModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    voting.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
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
    voting = Voting(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())
    response = voting.finished_polls(
        vote_type=VoteKey.KickFederationMember,
        pubkey_of_member_being_voted_on=generate_compressed_pubkey
    )
    assert response == [PollViewModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    voting.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_scheduledvote_whitelisthash(mocker: MockerFixture, network, generate_uint256):
    mocker.patch.object(Voting, 'post', return_value=None)
    voting = Voting(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())
    voting.schedulevote_whitelisthash(hash_id=generate_uint256)
    # noinspection PyUnresolvedReferences
    voting.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_scheduledvote_removehash(mocker: MockerFixture, network, generate_uint256):
    mocker.patch.object(Voting, 'post', return_value=None)
    voting = Voting(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())
    voting.schedulevote_removehash(hash_id=generate_uint256)
    # noinspection PyUnresolvedReferences
    voting.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
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
    voting = Voting(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())
    response = voting.whitelisted_hashes()
    assert response == [WhitelistedHashesModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    voting.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
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
    voting = Voting(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())
    response = voting.scheduled_votes()
    assert response == [VotingDataModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    voting.get.assert_called_once()
