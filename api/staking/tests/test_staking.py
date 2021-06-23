import pytest
from pytest_mock import MockerFixture
from api.staking import Staking
from api.staking.requestmodels import *
from api.staking.responsemodels import *
from pybitcoin.networks import StraxMain
from pybitcoin import WalletSecret


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths']]
    for endpoint in paths:
        if Staking.route + '/' in endpoint:
            assert endpoint in Staking.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths']]
    for endpoint in paths:
        if Staking.route + '/' in endpoint:
            assert endpoint in Staking.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths']]
    for endpoint in paths:
        if Staking.route + '/' in endpoint:
            assert endpoint in Staking.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths']]
    for endpoint in paths:
        if Staking.route + '/' in endpoint:
            assert endpoint in Staking.endpoints


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_get_staking_info(mocker: MockerFixture, network, fakeuri):
    data = {
        'enabled': True,
        'staking': True,
        'errors': '',
        'currentBlockSize': 50,
        'currentBlockTx': 2,
        'pooledTx': 2,
        'difficulty': 1000.000,
        'searchInterval': 1,
        'weight': 12345,
        'netStakeWeight': 98765343234,
        'immature': 0,
        'expectedTime': 1,
    }
    mocker.patch.object(Staking, 'get', return_value=data)
    staking = Staking(network=network, baseuri=fakeuri)

    response = staking.get_staking_info()

    assert response == GetStakingInfoModel(**data)
    # noinspection PyUnresolvedReferences
    staking.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_start_staking(mocker: MockerFixture, network, fakeuri):
    data = None
    mocker.patch.object(Staking, 'post', return_value=data)
    staking = Staking(network=network, baseuri=fakeuri)
    staking.start_staking(name='Name', password='password')

    # noinspection PyUnresolvedReferences
    staking.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_start_multistaking(mocker: MockerFixture, network, fakeuri):
    data = None
    mocker.patch.object(Staking, 'post', return_value=data)
    staking = Staking(network=network, baseuri=fakeuri)
    staking.start_multistaking(
        wallet_credentials=[
            WalletSecret(wallet_name='Wallet0', wallet_password='password0'),
            WalletSecret(wallet_name='Wallet1', wallet_password='password1'),
            WalletSecret(wallet_name='Wallet2', wallet_password='password2'),
        ]
    )

    # noinspection PyUnresolvedReferences
    staking.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_stop_staking(mocker: MockerFixture, network, fakeuri):
    data = None
    mocker.patch.object(Staking, 'post', return_value=data)
    staking = Staking(network=network, baseuri=fakeuri)
    staking.stop_staking()

    # noinspection PyUnresolvedReferences
    staking.post.assert_called_once()
