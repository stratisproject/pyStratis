import pytest
from pytest_mock import MockerFixture
from pystratis.api.staking import Staking
from pystratis.api.staking.responsemodels import *
from pystratis.core.networks import StraxMain
from pystratis.core import WalletSecret


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_get_staking_info(mocker: MockerFixture, network):
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
    staking = Staking(network=network, baseuri=mocker.MagicMock())

    response = staking.get_staking_info()

    assert response == GetStakingInfoModel(**data)
    # noinspection PyUnresolvedReferences
    staking.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_start_staking(mocker: MockerFixture, network):
    data = None
    mocker.patch.object(Staking, 'post', return_value=data)
    staking = Staking(network=network, baseuri=mocker.MagicMock())
    staking.start_staking(name='Name', password='password')

    # noinspection PyUnresolvedReferences
    staking.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_start_multistaking(mocker: MockerFixture, network):
    data = None
    mocker.patch.object(Staking, 'post', return_value=data)
    staking = Staking(network=network, baseuri=mocker.MagicMock())
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
def test_stop_staking(mocker: MockerFixture, network):
    data = None
    mocker.patch.object(Staking, 'post', return_value=data)
    staking = Staking(network=network, baseuri=mocker.MagicMock())
    staking.stop_staking()

    # noinspection PyUnresolvedReferences
    staking.post.assert_called_once()
