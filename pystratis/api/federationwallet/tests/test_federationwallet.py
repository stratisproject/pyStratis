import pytest
from pytest_mock import MockerFixture
from pystratis.api.federationwallet import FederationWallet
from pystratis.api.federationwallet.responsemodels import *
from pystratis.core.networks import StraxMain, CirrusMain
from pystratis.core import CoinType


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_general_info(mocker: MockerFixture, network):
    data = {
        'walletName': 'Test',
        'network': network.name,
        'creationTime': '2020-01-01T00:00:01',
        'isDecrypted': True,
        'lastBlockSyncedHeight': 10,
        'chainTip': 10,
        'isChainSynced': True,
        'connectedNodes': 10
    }
    mocker.patch.object(FederationWallet, 'get', return_value=data)
    federation_wallet = FederationWallet(network=network, baseuri=mocker.MagicMock())

    response = federation_wallet.general_info()

    assert response == WalletGeneralInfoModel(**data)
    # noinspection PyUnresolvedReferences
    federation_wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_balance(mocker: MockerFixture, network, get_base_keypath, generate_p2pkh_address):
    data = {
        'balances': [
            {
                'accountName': 'account 0',
                'accountHdPath': get_base_keypath,
                'coinType': CoinType.Strax,
                'amountConfirmed': 5,
                'amountUnconfirmed': 0,
                'spendableAmount': 5,
                'addresses': [
                    {
                        'address': generate_p2pkh_address(network=network),
                        'isUsed': True,
                        'isChange': False,
                        'amountConfirmed': 5,
                        'amountUnconfirmed': 0
                    }
                ]
            }
        ]
    }
    mocker.patch.object(FederationWallet, 'get', return_value=data)
    federation_wallet = FederationWallet(network=network, baseuri=mocker.MagicMock())

    response = federation_wallet.balance()

    assert response == WalletBalanceModel(**data)
    # noinspection PyUnresolvedReferences
    federation_wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_history(mocker: MockerFixture, network, generate_uint256, generate_p2pkh_address):
    data = [
        {
            'id': generate_uint256,
            'depositId': generate_uint256,
            'amount': 5,
            'payingTo': 'Rewards',
            'blockHeight': 5,
            'blockHash': generate_uint256,
            'signatureCount': 5,
            'spendingOutputDetails': 'details',
            'transferStatus': 'FullySigned'
        },
        {
            'id': generate_uint256,
            'depositId': generate_uint256,
            'amount': 5,
            'payingTo': generate_p2pkh_address(network=network),
            'blockHeight': 5,
            'blockHash': generate_uint256,
            'signatureCount': 5,
            'spendingOutputDetails': 'details',
            'transferStatus': 'SeenInBlock'
        }
    ]
    mocker.patch.object(FederationWallet, 'get', return_value=data)
    federation_wallet = FederationWallet(network=network, baseuri=mocker.MagicMock())
    response = federation_wallet.history(max_entries_to_return=2)
    assert response == [WithdrawalModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    federation_wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_sync(mocker: MockerFixture, network, generate_uint256):
    data = None
    mocker.patch.object(FederationWallet, 'post', return_value=data)
    federation_wallet = FederationWallet(network=network, baseuri=mocker.MagicMock())
    federation_wallet.sync(block_hash=generate_uint256)
    # noinspection PyUnresolvedReferences
    federation_wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_enable_federation(mocker: MockerFixture, network):
    data = None
    mocker.patch.object(FederationWallet, 'post', return_value=data)
    federation_wallet = FederationWallet(network=network, baseuri=mocker.MagicMock())
    response = federation_wallet.enable_federation(
        mnemonic='secret mnemonic',
        password='password',
        passphrase='passphrase',
        timeout_seconds=60
    )
    assert response is None
    # noinspection PyUnresolvedReferences
    federation_wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_remove_transactions(mocker: MockerFixture, network, generate_uint256):
    data = [{
        'transactionId': generate_uint256,
        'creationTime': '2020-01-01T00:00:01'
    }]
    mocker.patch.object(FederationWallet, 'delete', return_value=data)
    federation_wallet = FederationWallet(network=network, baseuri=mocker.MagicMock())
    response = federation_wallet.remove_transactions(resync=True)
    assert response == [RemovedTransactionModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    federation_wallet.delete.assert_called_once()
