import pytest
import json
from pystratis.api.coldstaking.requestmodels import *
from pystratis.core import ExtPubKey
from pystratis.core.types import Address, Money
from pystratis.core.networks import StraxMain, CirrusMain


def test_accountrequest(generate_extpubkey):
    data = {
        'walletName': 'Test',
        'walletPassword': 'password',
        'isColdWalletAccount': False,
        'extPubKey': generate_extpubkey
    }
    request_model = AccountRequest(
        wallet_name='Test',
        wallet_password='password',
        is_cold_wallet_account=False,
        extpubkey=ExtPubKey(data['extPubKey'])
    )
    assert json.dumps(data) == request_model.json()


def test_addressrequest():
    data = {
        'WalletName': 'Test',
        'IsColdWalletAddress': False,
        'Segwit': False
    }
    request_model = AddressRequest(
        wallet_name='Test',
        is_cold_wallet_address=False,
        segwit=False
    )
    assert json.dumps(data) == request_model.json()
    data = {
        'WalletName': 'Test',
        'IsColdWalletAddress': False,
        'Segwit': False
    }
    request_model = AddressRequest(
        wallet_name='Test',
        is_cold_wallet_address=False
    )
    assert json.dumps(data) == request_model.json()


def test_inforequest():
    data = {
        'WalletName': 'Test'
    }
    request_model = InfoRequest(
        wallet_name='Test'
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_offlinewithdrawalfeeestimationrequest(network, generate_p2pkh_address):
    data = {
        'walletName': 'Test',
        'accountName': 'account 0',
        'receivingAddress': generate_p2pkh_address(network=network),
        'amount': '5.00000000',
        'subtractFeeFromAmount': True
    }
    request_model = OfflineWithdrawalFeeEstimationRequest(
        wallet_name='Test',
        account_name='account 0',
        receiving_address=Address(address=data['receivingAddress'], network=network),
        amount=Money(5),
        subtract_fee_from_amount=True
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_offlinewithdrawalrequest(network, generate_p2pkh_address):
    data = {
        'receivingAddress': generate_p2pkh_address(network=network),
        'walletName': 'Test',
        'accountName': 'account 0',
        'amount': '5.00000000',
        'fees': '0.00010000',
        'subtractFeeFromAmount': True
    }
    request_model = OfflineWithdrawalRequest(
        receiving_address=Address(address=data['receivingAddress'], network=network),
        wallet_name='Test',
        account_name='account 0',
        amount=Money(5),
        fees=Money(0.0001),
        subtract_fee_from_amount=True
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_setupofflinerequest(network, generate_p2pkh_address):
    data = {
        'coldWalletAddress': generate_p2pkh_address(network=network),
        'hotWalletAddress': generate_p2pkh_address(network=network),
        'walletName': 'Test',
        'walletAccount': 'account 0',
        'amount': '5.00000000',
        'fees': "0.00010000",
        'subtractFeeFromAmount': True,
        'splitCount': 1,
        'segwitChangeAddress': False
    }
    request_model = SetupOfflineRequest(
        cold_wallet_address=Address(address=data['coldWalletAddress'], network=network),
        hot_wallet_address=Address(address=data['hotWalletAddress'], network=network),
        wallet_name='Test',
        wallet_account='account 0',
        amount=Money(5),
        fees=Money(0.0001),
        subtract_fee_from_amount=True,
        split_count=1,
        segwit_change_address=False
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_setuprequest(network, generate_p2pkh_address):
    data = {
        'coldWalletAddress': generate_p2pkh_address(network=network),
        'hotWalletAddress': generate_p2pkh_address(network=network),
        'walletName': 'Test',
        'walletAccount': 'account 0',
        'amount': '5.00000000',
        'fees': '0.00010000',
        'subtractFeeFromAmount': True,
        'splitCount': 1,
        'segwitChangeAddress': False,
        'walletPassword': 'password'
    }
    request_model = SetupRequest(
        cold_wallet_address=Address(address=data['coldWalletAddress'], network=network),
        hot_wallet_address=Address(address=data['hotWalletAddress'], network=network),
        wallet_name='Test',
        wallet_account='account 0',
        amount=Money(5),
        fees=Money(0.0001),
        subtract_fee_from_amount=True,
        split_count=1,
        segwit_change_address=False,
        wallet_password='password'
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_withdrawalrequest(network, generate_p2pkh_address):
    data = {
        'receivingAddress': generate_p2pkh_address(network=network),
        'walletPassword': 'password',
        'walletName': 'Test',
        'amount': '5.00000000',
        'subtractFeeFromAmount': True,
        'fees': '0.00010000'
    }
    request_model = WithdrawalRequest(
        receiving_address=Address(address=data['receivingAddress'], network=network),
        wallet_password='password',
        wallet_name='Test',
        amount=Money(5),
        subtract_fee_from_amount=True,
        fees=Money(0.0001)
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_retrievefilteredutxosrequest(network, generate_hexstring):
    data = {
        'walletName': 'Test',
        'walletPassword': 'password',
        'walletAccount': 'account 0',
        'hex': generate_hexstring(128),
        'broadcast': False
    }
    request_model = RetrieveFilteredUTXOsRequest(
        wallet_name='Test',
        wallet_password='password',
        wallet_account='account 0',
        trx_hex=data['hex'],
        broadcast=False
    )
    assert json.dumps(data) == request_model.json()
