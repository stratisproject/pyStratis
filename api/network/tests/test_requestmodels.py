import pytest
import json
from api.network.requestmodels import *


def test_clearbannedrequest():
    data = True
    request_model = ClearBannedRequest(
    )
    assert json.dumps(data) == request_model.json()


def test_disconnectpeerrequest():
    data = {
        'peerAddress': 'http://peeraddress'
    }
    request_model = DisconnectPeerRequest(
        peer_address=data['peerAddress']
    )
    assert json.dumps(data) == request_model.json()


def test_setbanrequest_invalid_command_raises_error():
    with pytest.raises(ValueError):
        SetBanRequest(
            ban_command='badcommand',
            ban_duration_seconds=60,
            peer_address='http://localhost'
        )


def test_setbanrequest():
    data = {
        'banCommand': 'add',
        'banDurationSeconds': 60,
        'peerAddress': 'http://localhost'
    }
    request_model = SetBanRequest(
        ban_command='add',
        ban_duration_seconds=60,
        peer_address='http://localhost'
    )
    assert json.dumps(data) == request_model.json()
