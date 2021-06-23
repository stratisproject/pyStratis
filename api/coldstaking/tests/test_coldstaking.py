import pytest
from pytest_mock import MockerFixture
from api.coldstaking import ColdStaking
from api.coldstaking.requestmodels import *
from api.coldstaking.responsemodels import *
from pybitcoin.networks import StraxMain
from pybitcoin.types import Address, Money


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths']]
    for endpoint in paths:
        if ColdStaking.route + '/' in endpoint:
            assert endpoint in ColdStaking.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths']]
    for endpoint in paths:
        if ColdStaking.route + '/' in endpoint:
            assert endpoint in ColdStaking.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths']]
    for endpoint in paths:
        if ColdStaking.route + '/' in endpoint:
            assert endpoint in ColdStaking.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths']]
    for endpoint in paths:
        if ColdStaking.route + '/' in endpoint:
            assert endpoint in ColdStaking.endpoints


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_info(mocker: MockerFixture, network, fakeuri):
    data = {'coldWalletAccountExists': True, 'hotWalletAccountExists': True}
    mocker.patch.object(ColdStaking, 'get', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.info(wallet_name='Test')

    assert response.cold_wallet_account_exists == data['coldWalletAccountExists']
    assert response.hot_wallet_account_exists == data['hotWalletAccountExists']
    # noinspection PyUnresolvedReferences
    coldstaking.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_cold_account_with_extpubkey(mocker: MockerFixture, network, fakeuri, generate_extpubkey):
    extpubkey = generate_extpubkey
    data = {'accountName': 'ColdStakingAccount'}
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.account(
        wallet_name='Test',
        wallet_password='password',
        is_cold_wallet_account=True,
        extpubkey=extpubkey
    )

    assert response.account_name == data['accountName']
    # noinspection PyUnresolvedReferences
    coldstaking.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_cold_account_no_extpubkey(mocker: MockerFixture, network, fakeuri):
    data = {'accountName': 'ColdStakingAccount'}
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.account(
        wallet_name='Test',
        wallet_password='password',
        is_cold_wallet_account=True
    )

    assert response.account_name == data['accountName']
    # noinspection PyUnresolvedReferences
    coldstaking.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_hot_account_with_extpubkey(mocker: MockerFixture, network, fakeuri, generate_extpubkey):
    extpubkey = generate_extpubkey

    data = {'accountName': 'HotStakingAccount'}
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.account(
        wallet_name='Test',
        wallet_password='password',
        is_cold_wallet_account=False,
        extpubkey=extpubkey
    )

    assert response.account_name == data['accountName']
    # noinspection PyUnresolvedReferences
    coldstaking.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_hot_account_no_extpubkey(mocker: MockerFixture, network, fakeuri):
    data = {'accountName': 'HotStakingAccount'}
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.account(
        wallet_name='Test',
        wallet_password='password',
        is_cold_wallet_account=False
    )

    assert response.account_name == data['accountName']
    # noinspection PyUnresolvedReferences
    coldstaking.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_address(mocker: MockerFixture, network, fakeuri, generate_p2pkh_address):
    data = {'address': generate_p2pkh_address(network=network)}
    mocker.patch.object(ColdStaking, 'get', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.address(wallet_name='Test', is_cold_wallet_address=True)

    assert str(response.address) == data['address']
    # noinspection PyUnresolvedReferences
    coldstaking.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_segwit_address(mocker: MockerFixture, network, fakeuri, generate_p2wpkh_address):
    data = {'address': generate_p2wpkh_address(network=network)}
    mocker.patch.object(ColdStaking, 'get', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.address(
        wallet_name='Test',
        is_cold_wallet_address=True,
        segwit=True
    )

    assert str(response.address) == data['address']
    # noinspection PyUnresolvedReferences
    coldstaking.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_setup_coldstaking(mocker: MockerFixture, network, fakeuri,
                                       generate_p2pkh_address, generate_hexstring):
    data = {'transactionHex': generate_hexstring(256)}
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.setup(
        wallet_name='Test',
        wallet_account='account 0',
        wallet_password='password',
        cold_wallet_address=Address(address=generate_p2pkh_address(network=network), network=network),
        hot_wallet_address=Address(address=generate_p2pkh_address(network=network), network=network),
        amount=Money(10),
        fees=Money(0.0001)
    )

    assert response.transaction_hex == data['transactionHex']
    # noinspection PyUnresolvedReferences
    coldstaking.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_setup_offline_coldstaking(mocker: MockerFixture, network, fakeuri,
                                               generate_p2pkh_address, generate_uint256, generate_hexstring,
                                               get_base_keypath):
    data = {
        'walletName': 'Test',
        'walletAccount': 'account 0',
        'fee': 1,
        'unsignedTransaction': generate_hexstring(256),
        'utxos': [{
            'transactionId': generate_uint256,
            'index': 0,
            'scriptPubKey': f'OP_DUP OP_HASH160 {generate_hexstring(40)} OP_EQUALVERIFY OP_CHECKSIG',
            'amount': 10
        }],
        'addresses': [{
            'address': str(Address(address=generate_p2pkh_address(network=network), network=network)),
            'keyPath': get_base_keypath,
            'addressType': 'p2pkh'
        }]
    }
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.setup_offline(
        wallet_name='Test',
        wallet_account='account 0',
        cold_wallet_address=Address(address=generate_p2pkh_address(network=network), network=network),
        hot_wallet_address=Address(address=generate_p2pkh_address(network=network), network=network),
        amount=Money(10),
        fees=Money(0.0001)
    )

    assert response == BuildOfflineSignModel(**data)
    # noinspection PyUnresolvedReferences
    coldstaking.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_estimate_setup_tx_fee(mocker: MockerFixture, network, fakeuri,
                                           generate_p2pkh_address):
    data = 10000
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.estimate_setup_tx_fee(
        wallet_name='Test',
        wallet_account='account 0',
        wallet_password='password',
        cold_wallet_address=Address(address=generate_p2pkh_address(network=network), network=network),
        hot_wallet_address=Address(address=generate_p2pkh_address(network=network), network=network),
        amount=Money(10),
        fees=Money(0.0001)
    )

    assert response == Money.from_satoshi_units(data)
    # noinspection PyUnresolvedReferences
    coldstaking.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_estimate_offline_setup_tx_fee(mocker: MockerFixture, network, fakeuri,
                                                   generate_p2pkh_address):
    data = 10000
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.estimate_offline_setup_tx_fee(
        wallet_name='Test',
        wallet_account='account 0',
        cold_wallet_address=Address(address=generate_p2pkh_address(network=network), network=network),
        hot_wallet_address=Address(address=generate_p2pkh_address(network=network), network=network),
        amount=Money(10),
        fees=Money(0.0001)
    )

    assert response == Money.from_satoshi_units(data)
    # noinspection PyUnresolvedReferences
    coldstaking.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_withdrawal(mocker: MockerFixture, network, fakeuri,
                                generate_p2pkh_address, generate_uint256):
    data = {'transactionHex': generate_uint256}
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.withdrawal(
        wallet_name='Test',
        wallet_password='password',
        receiving_address=Address(address=generate_p2pkh_address(network=network), network=network),
        amount=Money(10),
        fees=Money(0.0001)
    )

    assert response == WithdrawalModel(**data)
    # noinspection PyUnresolvedReferences
    coldstaking.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_offline_withdrawal(mocker: MockerFixture, network, fakeuri,
                                        generate_p2pkh_address, get_base_keypath, generate_hexstring,
                                        generate_uint256):
    data = {
        'walletName': 'Test',
        'walletAccount': 'account 0',
        'fee': 10000,
        'unsignedTransaction': generate_hexstring(256),
        'utxos': [{
            'transactionId': generate_uint256,
            'index': 0,
            'scriptPubKey': f'OP_DUP OP_HASH160 {generate_hexstring(40)} OP_EQUALVERIFY OP_CHECKSIG',
            'amount': 10
        }],
        'addresses': [{
            'address': str(Address(address=generate_p2pkh_address(network=network), network=network)),
            'keyPath': get_base_keypath,
            'addressType': 'p2pkh'
        }]
    }
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.offline_withdrawal(
        wallet_name='Test',
        account_name='account 0',
        receiving_address=Address(address=generate_p2pkh_address(network=network), network=network),
        amount=Money(10),
        fees=Money(0.0001),
        subtractFeeFromAmount=True
    )

    assert response == BuildOfflineSignModel(**data)
    # noinspection PyUnresolvedReferences
    coldstaking.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_estimate_offline_withdrawal_fee(mocker: MockerFixture, network, fakeuri,
                                                     generate_p2pkh_address):
    data = 10000
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.estimate_offline_withdrawal_tx_fee(
        wallet_name='Test',
        account_name='account 0',
        receiving_address=Address(address=generate_p2pkh_address(network=network), network=network),
        amount=Money(10)
    )

    assert response == Money.from_satoshi_units(data)
    # noinspection PyUnresolvedReferences
    coldstaking.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_estimate_withdrawal_fee(mocker: MockerFixture, network, fakeuri,
                                             generate_p2pkh_address):
    data = 10000
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.estimate_withdrawal_tx_fee(
        wallet_name='Test',
        account_name='account 0',
        wallet_password='password',
        receiving_address=Address(address=generate_p2pkh_address(network=network), network=network),
        amount=Money(10),
        fees=Money(0.0001)
    )

    assert response == Money.from_satoshi_units(data)
    # noinspection PyUnresolvedReferences
    coldstaking.post.assert_called_once()
