import json
from pystratis.api.federationgateway.requestmodels import *


def test_depositsrequest():
    data = {
        'blockHeight': 5
    }
    request_model = DepositsRequest(
        block_height=5
    )
    assert json.dumps(data) == request_model.json()


def test_fullysignedtransferrequest(generate_uint256):
    data = {
        'depositId': generate_uint256,
        'transactionId': generate_uint256
    }
    request_model = FullySignedTransferRequest(
        deposit_id=data['depositId'],
        transaction_id=data['transactionId']
    )
    assert json.dumps(data) == request_model.json()


def test_memberipaddrequest():
    data = {
        'endpoint': 'http://localhost'
    }
    request_model = MemberIPAddRequest(
        endpoint=data['endpoint']
    )
    assert json.dumps(data) == request_model.json()


def test_memberipremoverequest():
    data = {
        'endpoint': 'http://localhost'
    }
    request_model = MemberIPRemoveRequest(
        endpoint=data['endpoint']
    )
    assert json.dumps(data) == request_model.json()


def test_memberipreplacerequest():
    data = {
        'endpointtouse': 'http://newhost',
        'endpoint': 'http://localhost'
    }
    request_model = MemberIPReplaceRequest(
        endpointtouse=data['endpointtouse'],
        endpoint=data['endpoint']
    )
    assert json.dumps(data) == request_model.json()


def test_pendingtransferrequest(generate_uint256):
    data = {
        'depositId': generate_uint256,
        'transactionId': generate_uint256
    }
    request_model = PendingTransferRequest(
        deposit_id=data['depositId'],
        transaction_id=data['transactionId']
    )
    assert json.dumps(data) == request_model.json()


def test_verifytransferrequest(generate_uint256):
    data = {
        'depositIdTransactionId': generate_uint256
    }
    request_model = VerifyTransferRequest(
        deposit_id_transaction_id=data['depositIdTransactionId']
    )
    assert json.dumps(data) == request_model.json()


def test_transferrequest(generate_uint256):
    data = {
        'depositId': generate_uint256
    }
    request_model = TransferRequest(
        deposit_id=data['depositId']
    )
    assert json.dumps(data) == request_model.json()
