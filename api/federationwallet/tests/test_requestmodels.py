import json
from api.federationwallet.requestmodels import *


def test_enablefederationrequest():
    data = {
        'mnemonic': 'secret mnemonic',
        'password': 'password',
        'passphrase': 'passphrase',
        'timeoutSeconds': 60
    }
    request_model = EnableFederationRequest(
        mnemonic='secret mnemonic',
        password='password',
        passphrase='passphrase',
        timeout_seconds=60
    )
    assert json.dumps(data) == request_model.json()


def test_historyrequest():
    data = {
        'maxEntriesToReturn': 50
    }
    request_model = HistoryRequest(
        max_entries_to_return=50
    )
    assert json.dumps(data) == request_model.json()


def test_removetransactionsrequest():
    data = {
        'ReSync': True
    }
    request_model = RemoveTransactionsRequest(
        resync=True
    )
    assert json.dumps(data) == request_model.json()


def test_syncrequest(generate_uint256):
    data = {
        'hash': generate_uint256
    }
    request_model = SyncRequest(
        block_hash=data['hash']
    )
    assert json.dumps(data) == request_model.json()
