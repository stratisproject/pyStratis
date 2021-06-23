import pytest
import json
from api.blockstore.requestmodels import *
from pybitcoin.types import Address
from pybitcoin.networks import StraxMain, CirrusMain


def test_blockrequest(generate_uint256):
    data = {
        'Hash': generate_uint256,
        'ShowTransactionDetails': True,
        'OutputJson': True
    }
    request_model = BlockRequest(
        block_hash=data['Hash'],
        show_transaction_details=True
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getaddressesbalancesrequest(network, generate_p2pkh_address):
    addresses = [Address(address=generate_p2pkh_address(network=network), network=network) for _ in range(5)]
    data_single = {
        'addresses': addresses[0].json(),
        'minConfirmations': 5
    }
    request_model_single = GetAddressesBalancesRequest(
        addresses=addresses[0],
        min_confirmations=5
    )
    assert json.dumps(data_single) == request_model_single.json()
    data_multiple = {
        'addresses': ','.join([x.json() for x in addresses]),
        'minConfirmations': 5
    }
    request_model_multiple = GetAddressesBalancesRequest(
        addresses=addresses,
        min_confirmations=5
    )
    assert json.dumps(data_multiple) == request_model_multiple.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getlastbalanceupdatetransactionrequest(network, generate_p2pkh_address):
    data = {
        'address': generate_p2pkh_address(network=network)
    }
    request_model = GetLastBalanceUpdateTransactionRequest(
        address=Address(address=data['address'], network=network)
    )
    assert json.dumps(data) == request_model.json()


def getutxosetrequest():
    data = {
        'atBlockHeight': 5
    }
    request_model = GetUTXOSetRequest(
        at_block_height=5
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def getverboseaddressesbalancesrequest(network, generate_p2pkh_address):
    addresses = [Address(address=generate_p2pkh_address(network=network), network=network) for _ in range(5)]
    data_single = {
        'addresses': addresses[0].json()
    }
    request_model_single = GetVerboseAddressesBalancesRequest(
        addresses=addresses[0],
        min_confirmations=5
    )
    assert json.dumps(data_single) == request_model_single.json()
    data_multiple = {
        'addresses': ','.join([x.json() for x in addresses])
    }
    request_model_multiple = GetVerboseAddressesBalancesRequest(
        addresses=addresses,
        min_confirmations=5
    )
    assert json.dumps(data_multiple) == request_model_multiple.json()
