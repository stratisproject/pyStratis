import pytest
import json
from pystratis.api.node.requestmodels import *
from pystratis.core import LogRule
from pystratis.core.networks import StraxMain, CirrusMain


def test_decoderawtransactionrequest(generate_hexstring):
    data = {
        'rawHex': generate_hexstring(128)
    }
    request_model = DecodeRawTransactionRequest(
        raw_hex=data['rawHex']
    )
    assert json.dumps(data) == request_model.json()


def test_getblockheaderrequest(generate_uint256):
    data = {
        'hash': generate_uint256,
        'isJsonFormat': True
    }
    request_model = GetBlockHeaderRequest(
        block_hash=data['hash'],
        is_json_format=True
    )
    assert json.dumps(data) == request_model.json()


def test_getrawtransactionrequest(generate_uint256):
    data = {
        'trxid': generate_uint256,
        'verbose': True
    }
    request_model = GetRawTransactionRequest(
        trxid=data['trxid'],
        verbose=True
    )
    assert json.dumps(data) == request_model.json()


def test_gettxoutproofrequest(generate_uint256):
    data = {
        'txids': [
            generate_uint256,
            generate_uint256
        ],
        'blockhash': generate_uint256
    }
    request_model = GetTxOutProofRequest(
        txids=data['txids'],
        block_hash=data['blockhash']
    )
    assert json.dumps(data) == request_model.json()


def test_gettxoutrequest(generate_uint256):
    data = {
        'trxid': generate_uint256,
        'vout': 0,
        'includeMemPool': False
    }
    request_model = GetTxOutRequest(
        trxid=data['trxid'],
        vout=0,
        include_mempool=False
    )
    assert json.dumps(data) == request_model.json()


def test_logrulesrequest():
    data = {
        'logRules': [
            {
                'ruleName': 'TestRule',
                'logLevel': 'Debug',
                'filename': 'filename'
            }
        ]
    }
    request_model = LogRulesRequest(
        log_rules=[
            LogRule(rule_name='TestRule', log_level='Debug', filename='filename')
        ]
    )
    assert json.dumps(data) == request_model.json()


def test_shutdownrequest():
    data = True
    request_model = ShutdownRequest(
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_validateaddressrequest(network, generate_p2pkh_address):
    data = {
        'address': generate_p2pkh_address(network=network)
    }
    request_model = ValidateAddressRequest(
        address=data['address']
    )
    assert json.dumps(data) == request_model.json()
