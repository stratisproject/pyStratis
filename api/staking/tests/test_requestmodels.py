import json
from pybitcoin import WalletSecret
from api.staking.requestmodels import *


def test_startmultistakingrequest():
    data = {
        'walletCredentials': [
            {
                'walletName': 'Wallet0',
                'walletPassword': 'password0'
            },
            {
                'walletName': 'Wallet1',
                'walletPassword': 'password1'
            },
            {
                'walletName': 'Wallet2',
                'walletPassword': 'password2'
            }
        ]
    }
    request_model = StartMultiStakingRequest(
        wallet_credentials=[
            WalletSecret(wallet_name='Wallet0', wallet_password='password0'),
            WalletSecret(wallet_name='Wallet1', wallet_password='password1'),
            WalletSecret(wallet_name='Wallet2', wallet_password='password2'),
        ]
    )
    assert json.dumps(data) == request_model.json()


def test_startstakingrequest():
    data = {
        'name': 'Name',
        'password': 'password'
    }
    request_model = StartStakingRequest(
        name='Name',
        password='password'
    )
    assert json.dumps(data) == request_model.json()


def test_stopstakingrequest():
    data = True
    request_model = StopStakingRequest(
    )
    assert json.dumps(data) == request_model.json()
