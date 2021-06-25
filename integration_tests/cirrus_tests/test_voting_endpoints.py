import pytest
from api.voting.responsemodels import *
from api.voting.requestmodels import VoteKey
from nodes import CirrusMinerNode
from pybitcoin import PollViewModel


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_executed_polls(cirrusminer_node: CirrusMinerNode, generate_compressed_pubkey):
    response = cirrusminer_node.voting.executed_polls(
        vote_type=VoteKey.KickFederationMember,
        pubkey_of_member_being_voted_on=generate_compressed_pubkey
    )
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, PollViewModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_pending_polls(cirrusminer_node: CirrusMinerNode, generate_compressed_pubkey):
    response = cirrusminer_node.voting.pending_polls(
        vote_type=VoteKey.KickFederationMember,
        pubkey_of_member_being_voted_on=generate_compressed_pubkey
    )
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, PollViewModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_finished_polls(cirrusminer_node: CirrusMinerNode, generate_compressed_pubkey):
    response = cirrusminer_node.voting.finished_polls(
        vote_type=VoteKey.KickFederationMember,
        pubkey_of_member_being_voted_on=generate_compressed_pubkey
    )
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, PollViewModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_scheduledvote_whitelisthash(cirrusminer_node: CirrusMinerNode, generate_uint256):
    cirrusminer_node.voting.schedulevote_whitelisthash(hash_id=generate_uint256)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_scheduledvote_removehash(cirrusminer_node: CirrusMinerNode, generate_uint256):
    cirrusminer_node.voting.schedulevote_removehash(hash_id=generate_uint256)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_whitelistedhashes(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.voting.whitelisted_hashes()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, WhitelistedHashesModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_scheduledvotes(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.voting.scheduled_votes()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, VotingDataModel)
