import json
from pybitcoin import PubKey
from api.voting.requestmodels import *


def test_pollsrequest(generate_compressed_pubkey):
    data = {
        'voteType': VoteKey.AddFederationMember.value,
        'pubKeyOfMemberBeingVotedOn': generate_compressed_pubkey
    }
    request_model = PollsRequest(
        vote_type=VoteKey.AddFederationMember,
        pubkey_of_member_being_voted_on=PubKey(data['pubKeyOfMemberBeingVotedOn'])
    )
    assert json.dumps(data) == request_model.json()


def test_schedulevoteremovehashrequest(generate_uint256):
    data = {
        'hash': generate_uint256
    }
    request_model = ScheduleVoteRemoveHashRequest(
        hash_id=data['hash']
    )
    assert json.dumps(data) == request_model.json()


def test_schedulevotewhitelisthashrequest(generate_uint256):
    data = {
        'hash': generate_uint256
    }
    request_model = ScheduleVoteWhitelistHashRequest(
        hash_id=data['hash']
    )
    assert json.dumps(data) == request_model.json()
