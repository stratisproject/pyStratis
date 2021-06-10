import pytest
from pytest_mock import MockerFixture
from api.federationwallet import FederationWallet
from api.federationwallet.requestmodels import *
from api.federationwallet.responsemodels import *
from pybitcoin.networks import StraxMain, CirrusMain
from pybitcoin import CoinType, CrossChainTransferStatus, RemovedTransactionModel,\
    WalletBalanceModel, WalletGeneralInfoModel


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if FederationWallet.route + '/' in endpoint:
            assert endpoint in FederationWallet.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if FederationWallet.route + '/' in endpoint:
            assert endpoint in FederationWallet.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if FederationWallet.route + '/' in endpoint:
            assert endpoint in FederationWallet.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if FederationWallet.route + '/' in endpoint:
            assert endpoint in FederationWallet.endpoints


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_general_info(mocker: MockerFixture, network, fakeuri):
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
    federation_wallet = FederationWallet(network=network, baseuri=fakeuri)

    response = federation_wallet.general_info()

    assert response == WalletGeneralInfoModel(**data)
    # noinspection PyUnresolvedReferences
    federation_wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_balance(mocker: MockerFixture, network, fakeuri, get_base_keypath, generate_p2pkh_address):
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
    federation_wallet = FederationWallet(network=network, baseuri=fakeuri)

    response = federation_wallet.balance()

    assert response == WalletBalanceModel(**data)
    # noinspection PyUnresolvedReferences
    federation_wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_history(mocker: MockerFixture, network, fakeuri, generate_uint256, generate_p2pkh_address):
    data = [
        {
            'Id': generate_uint256,
            'DepositId': generate_uint256,
            'Amount': 5,
            'PayingTo': generate_p2pkh_address(network=network),
            'BlockHeight': 5,
            'BlockHash': generate_uint256,
            'SignatureCount': 5,
            'SpendingOutputDetails': 'details',
            'TransferStatus': CrossChainTransferStatus.FullySigned
        },
        {
            'Id': generate_uint256,
            'DepositId': generate_uint256,
            'Amount': 5,
            'PayingTo': generate_p2pkh_address(network=network),
            'BlockHeight': 5,
            'BlockHash': generate_uint256,
            'SignatureCount': 5,
            'SpendingOutputDetails': 'details',
            'TransferStatus': CrossChainTransferStatus.FullySigned
        }
    ]
    mocker.patch.object(FederationWallet, 'get', return_value=data)
    federation_wallet = FederationWallet(network=network, baseuri=fakeuri)
    request_model = HistoryRequest(
        max_entries_to_return=2
    )
    response = federation_wallet.history(request_model)

    assert response == [WithdrawalModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    federation_wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_sync(mocker: MockerFixture, network, fakeuri, generate_uint256):
    data = None
    mocker.patch.object(FederationWallet, 'post', return_value=data)
    federation_wallet = FederationWallet(network=network, baseuri=fakeuri)
    request_model = SyncRequest(
        hash=generate_uint256
    )

    federation_wallet.sync(request_model)

    # noinspection PyUnresolvedReferences
    federation_wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_enable_federation(mocker: MockerFixture, network, fakeuri):
    data = None
    mocker.patch.object(FederationWallet, 'post', return_value=data)
    federation_wallet = FederationWallet(network=network, baseuri=fakeuri)
    request_model = EnableFederationRequest(
        mnemonic='secret mnemonic',
        password='password',
        passphrase='passphrase',
        timeout_seconds=60
    )

    response = federation_wallet.enable_federation(request_model)

    assert response is None
    # noinspection PyUnresolvedReferences
    federation_wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_remove_transactions(mocker: MockerFixture, network, fakeuri, generate_uint256):
    data = [{
        'transactionId': generate_uint256,
        'creationTime': '2020-01-01T00:00:01'
    }]
    mocker.patch.object(FederationWallet, 'delete', return_value=data)
    federation_wallet = FederationWallet(network=network, baseuri=fakeuri)
    request_model = RemoveTransactionsRequest(
        resync=True
    )

    response = federation_wallet.remove_transactions(request_model)

    assert response == [RemovedTransactionModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    federation_wallet.delete.assert_called_once()
