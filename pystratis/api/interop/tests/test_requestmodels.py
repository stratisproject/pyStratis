import json
import pytest
from pystratis.core import DestinationChain
from pystratis.core.networks import CirrusMain
from pystratis.core.types import Address
from pystratis.api.interop.requestmodels import *


def test_ownersrequest():
    data = {
        'destinationChain': DestinationChain.ETH
    }
    request_model = OwnersRequest(
        destination_chain=data['destinationChain']
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_addownerrequest(network, generate_p2pkh_address):
    data = {
        'destinationChain': DestinationChain.ETH,
        'newOwnerAddress': generate_p2pkh_address(network=network),
        'gasPrice': 100
    }
    request_model = AddOwnerRequest(
        destination_chain=data['destinationChain'],
        new_owner_address=Address(address=data['newOwnerAddress'], network=network),
        gas_price=data['gasPrice']
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_removeownerrequest(network, generate_p2pkh_address):
    data = {
        'destinationChain': DestinationChain.ETH,
        'existingOwnerAddress': generate_p2pkh_address(network=network),
        'gasPrice': 100
    }
    request_model = RemoveOwnerRequest(
        destination_chain=data['destinationChain'],
        existing_owner_address=Address(address=data['existingOwnerAddress'], network=network),
        gas_price=data['gasPrice']
    )
    assert json.dumps(data) == request_model.json()


def test_confirmtransactionrequest():
    data = {
        'destinationChain': DestinationChain.ETH,
        'transactionId': 1,
        'gasPrice': 100
    }
    request_model = ConfirmTransactionRequest(
        destination_chain=data['destinationChain'],
        transaction_id=data['transactionId'],
        gas_price=data['gasPrice']
    )
    assert json.dumps(data) == request_model.json()


def test_multisigtransactionrequest():
    data = {
        'destinationChain': DestinationChain.ETH,
        'transactionId': 1,
        'raw': False
    }
    request_model = MultisigTransactionRequest(
        destination_chain=data['destinationChain'],
        transaction_id=data['transactionId'],
        raw=data['raw']
    )
    assert json.dumps(data) == request_model.json()


def test_multisigconfirmationsrequest():
    data = {
        'destinationChain': DestinationChain.ETH,
        'transactionId': 1,
    }
    request_model = MultisigConfirmationsRequest(
        destination_chain=data['destinationChain'],
        transaction_id=data['transactionId'],
    )
    assert json.dumps(data) == request_model.json()


def test_setoriginatorrequest():
    data = {'requestId': 1}
    request_model = SetOriginatorRequest(
        request_id=data['requestId']
    )
    assert json.dumps(data) == request_model.json()


def test_reprocessburnrequest():
    data = {
        'id': 1,
        'height': 1
    }
    request_model = ReprocessBurnRequest(
        request_id=data['id'],
        height=data['height']
    )
    assert json.dumps(data) == request_model.json()


def test_pushvoterequest():
    data = {
        'requestId': 1,
        'voteId': 1
    }
    request_model = PushVoteRequest(
        request_id=data['requestId'],
        vote_id=data['voteId']
    )
    assert json.dumps(data) == request_model.json()
