import pytest
from pytest_mock import MockerFixture
import ecdsa
import base64
from api.wallet import Wallet
from api.wallet.requestmodels import *
from api.wallet.responsemodels import *
from pybitcoin import PubKey, CoinType, Recipient, Outpoint, \
    DestinationChain, ExtPubKey, UtxoDescriptor, AddressDescriptor
from pybitcoin.types import Address, Money, uint256
from pybitcoin.networks import StraxMain, CirrusMain, Ethereum


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths']]
    for endpoint in paths:
        if Wallet.route + '/' in endpoint:
            assert endpoint in Wallet.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths']]
    for endpoint in paths:
        if Wallet.route + '/' in endpoint:
            assert endpoint in Wallet.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths']]
    for endpoint in paths:
        if Wallet.route + '/' in endpoint:
            assert endpoint in Wallet.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths']]
    for endpoint in paths:
        if Wallet.route + '/' in endpoint:
            assert endpoint in Wallet.endpoints


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_mnemonic(mocker: MockerFixture, network, fakeuri):
    data = 'a b c d e f g h i j k l'
    mocker.patch.object(Wallet, 'get', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.mnemonic(language='English', word_count=12)

    assert response == data.split(' ')
    assert len(response) == 12
    # noinspection PyUnresolvedReferences
    wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_create(mocker: MockerFixture, network, fakeuri):
    data = 'a b c d e f g h i j k l'
    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.create(
        mnemonic=data,
        password='password',
        passphrase='passphrase',
        name='Test'
    )

    assert response == data.split(' ')
    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_sign_message(mocker: MockerFixture, network, fakeuri, generate_p2pkh_address,
                      generate_privatekey):
    message = 'This is my message'
    private_key_bytes = generate_privatekey().get_bytes()
    key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    sig = base64.b64encode(key.sign(bytes(message, 'ascii'))).decode('ascii')
    data = sig
    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.sign_message(
        wallet_name='Test',
        password='password',
        external_address=Address(address=generate_p2pkh_address(network=network), network=network),
        message=message
    )

    assert response == data
    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_pubkey(mocker: MockerFixture, network, fakeuri, generate_uncompressed_pubkey,
                generate_p2pkh_address):
    data = generate_uncompressed_pubkey
    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.pubkey(
        wallet_name='Test',
        external_address=Address(address=generate_p2pkh_address(network=network), network=network)
    )

    assert response == PubKey(data)
    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_verify_message(mocker: MockerFixture, network, fakeuri, generate_p2pkh_address, generate_privatekey):
    message = 'This is my message'
    private_key_bytes = generate_privatekey().get_bytes()
    key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    sig = base64.b64encode(key.sign(bytes(message, 'ascii'))).decode('ascii')
    data = True
    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)
    response = wallet.verify_message(
        signature=sig,
        external_address=Address(address=generate_p2pkh_address(network=network), network=network),
        message=message
    )

    assert response == data
    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_load(mocker: MockerFixture, network, fakeuri):
    data = None
    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    wallet.load(name='Test', password='password')

    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_recover(mocker: MockerFixture, network, fakeuri):
    data = None
    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)
    wallet.recover(
        mnemonic='mnemonic',
        password='password',
        passphrase='passphrase',
        name='Test',
        creation_date='2020-01-01T00:00:01'
    )

    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_recover_via_extpubkey(mocker: MockerFixture, network, fakeuri, generate_extpubkey):
    data = None
    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)
    wallet.recover_via_extpubkey(
        extpubkey=generate_extpubkey,
        account_index=0,
        name='Test',
        creation_date='2020-01-01T00:00:01'
    )

    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


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
    mocker.patch.object(Wallet, 'get', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)
    response = wallet.general_info(name='Test')

    assert response == WalletGeneralInfoModel(**data)
    # noinspection PyUnresolvedReferences
    wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_transaction_count(mocker: MockerFixture, network, fakeuri):
    data = {'transactionCount': 5}
    mocker.patch.object(Wallet, 'get', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.transaction_count(
        wallet_name='Test',
        account_name='account 0'
    )

    assert response == data['transactionCount']
    # noinspection PyUnresolvedReferences
    wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_history(mocker: MockerFixture, network, fakeuri, generate_p2pkh_address, generate_uint256):
    data = {
        'history': [
            {
                'accountName': 'account 0',
                'accountHdPath': 'hdpath',
                'coinType': CoinType.Strax,
                'transactionsHistory': [
                    {
                        'type': 'received',
                        'toAddress': generate_p2pkh_address(network=network),
                        'id': generate_uint256,
                        'amount': '5.0',
                        'payments': [
                            {
                                'destinationAddress': generate_p2pkh_address(network=network),
                                'amount': '5.0',
                                'isChange': False
                            }
                        ],
                        'fee': 10000,
                        'confirmedInBlock': 2,
                        'timestamp': 'timestamp',
                        'txOutputTime': 1,
                        'txOutputIndex': 0,
                        'blockIndex': 1
                    }
                ]
            }
        ]
    }
    mocker.patch.object(Wallet, 'get', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.history(
        wallet_name='Test',
        account_name='account 0',
        address=Address(address=generate_p2pkh_address(network=network), network=network),
        skip=2,
        take=2,
        prev_output_tx_time=0,
        prev_output_index=0,
        search_query='query'
    )

    assert response == WalletHistoryModel(**data)
    # noinspection PyUnresolvedReferences
    wallet.get.assert_called_once()


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
    mocker.patch.object(Wallet, 'get', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)
    response = wallet.balance(
        wallet_name='Test',
        account_name='account 0',
        include_balance_by_address=True
    )

    assert response == WalletBalanceModel(**data)
    # noinspection PyUnresolvedReferences
    wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_received_by_address(mocker: MockerFixture, network, fakeuri, generate_p2pkh_address):
    data = {
        'address': generate_p2pkh_address(network=network),
        'coinType': CoinType.Strax,
        'amountConfirmed': 5,
        'amountUnconfirmed': 0,
        'spendableAmount': 5
    }
    mocker.patch.object(Wallet, 'get', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.received_by_address(address=Address(address=data['address'], network=network))

    assert response == AddressBalanceModel(**data)
    # noinspection PyUnresolvedReferences
    wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_max_balance(mocker: MockerFixture, network, fakeuri):
    data = {
        'maxSpendableAmount': 5,
        'fee': 10000
    }
    mocker.patch.object(Wallet, 'get', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.max_balance(
        wallet_name='Test',
        account_name='account 0',
        fee_type='low',
        allow_unconfirmed=True
    )

    assert response == MaxSpendableAmountModel(**data)
    # noinspection PyUnresolvedReferences
    wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_spendable_transactions(mocker: MockerFixture, network, fakeuri, generate_uint256, generate_p2pkh_address):
    data = {
        'transactions': [
            {
                'id': generate_uint256,
                'index': 0,
                'address': generate_p2pkh_address(network=network),
                'isChange': True,
                'amount': '5.0',
                'creationTime': '2020-01-01T00:00:01',
                'confirmations': 5,
            }
        ]
    }
    mocker.patch.object(Wallet, 'get', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)
    response = wallet.spendable_transactions(
        wallet_name='Test',
        account_name='account 0',
        min_confirmations=0
    )

    assert response == SpendableTransactionsModel(**data)
    # noinspection PyUnresolvedReferences
    wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_estimate_txfee(mocker: MockerFixture, network, fakeuri, generate_uint256, generate_p2pkh_address):
    data = 10000
    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)
    response = wallet.estimate_txfee(
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=generate_uint256, index=0)],
        recipients=[
            Recipient(
                destination_address=Address(address=generate_p2pkh_address(network=network), network=network),
                destination_script=Address(address=generate_p2pkh_address(network=network), network=network),
                subtraction_fee_from_amount=True,
                amount=Money(10)
            )
        ],
        op_return_data='opreturn',
        op_return_amount=Money(0.00000001),
        fee_type='low',
        allow_unconfirmed=True,
        shuffle_outputs=True,
        change_address=Address(address=generate_p2pkh_address(network=network), network=network)
    )

    assert response == Money.from_satoshi_units(data)
    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_build_transaction(mocker: MockerFixture, network, fakeuri, generate_p2pkh_address,
                           generate_uint256, generate_hexstring):
    data = {
        'fee': 10000,
        'hex': generate_hexstring(128),
        'transactionId': generate_uint256
    }
    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.build_transaction(
        fee_amount=Money(0.0001),
        password='password',
        segwit_change_address=False,
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=generate_uint256, index=0)],
        recipients=[
            Recipient(
                destination_address=Address(address=generate_p2pkh_address(network=network), network=network),
                destination_script=Address(address=generate_p2pkh_address(network=network), network=network),
                subtraction_fee_from_amount=True,
                amount=Money(10)
            )
        ],
        op_return_data='opreturn',
        op_return_amount=Money(0.00000001),
        allow_unconfirmed=True,
        shuffle_outputs=True,
        change_address=Address(address=generate_p2pkh_address(network=network), network=network)
    )

    assert response == BuildTransactionModel(**data)
    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_build_interflux_transaction(mocker: MockerFixture, network, fakeuri, generate_p2pkh_address,
                                     generate_ethereum_checksum_address, generate_uint256, generate_hexstring):
    data = {
        'fee': 10000,
        'hex': generate_hexstring(128),
        'transactionId': generate_uint256
    }
    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.build_interflux_transaction(
        destination_chain=DestinationChain.ETH,
        destination_address=Address(address=generate_ethereum_checksum_address, network=Ethereum()),
        fee_amount=Money(0.0001),
        password='password',
        segwit_change_address=False,
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=generate_uint256, index=0)],
        recipients=[
            Recipient(
                destination_address=Address(address=generate_p2pkh_address(network=network), network=network),
                destination_script=Address(address=generate_p2pkh_address(network=network), network=network),
                subtraction_fee_from_amount=True,
                amount=Money(10)
            )
        ],
        op_return_data='opreturn',
        op_return_amount=Money(0.00000001),
        allow_unconfirmed=True,
        shuffle_outputs=True,
        change_address=Address(address=generate_p2pkh_address(network=network), network=network)
    )

    assert response == BuildTransactionModel(**data)
    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_send_transaction(mocker: MockerFixture, network, fakeuri, generate_uint256, generate_p2pkh_address,
                          generate_hexstring):
    data = {
        'transactionId': generate_uint256,
        'outputs': [
            {
                'address': generate_p2pkh_address(network=network),
                'amount': '10',
                'OpReturnData': f'{generate_p2pkh_address(network=network)}'
            }
        ]
    }
    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.send_transaction(transaction_hex=generate_hexstring(128))

    assert response == WalletSendTransactionModel(**data)
    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_list_wallets(mocker: MockerFixture, network, fakeuri):
    data = {'walletNames': ['Test'], 'watchOnlyWallets': []}
    mocker.patch.object(Wallet, 'get', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.list_wallets()

    assert response == data
    # noinspection PyUnresolvedReferences
    wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_account(mocker: MockerFixture, network, fakeuri):
    data = 'Test'
    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.account(password='password', wallet_name='Test')

    assert response == data
    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_accounts(mocker: MockerFixture, network, fakeuri):
    data = ['account 0', 'account 1']
    mocker.patch.object(Wallet, 'get', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.accounts(wallet_name='Test')

    assert response == data
    # noinspection PyUnresolvedReferences
    wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_unused_address(mocker: MockerFixture, network, fakeuri, generate_p2pkh_address):
    data = generate_p2pkh_address(network=network)
    mocker.patch.object(Wallet, 'get', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.unused_address(
        wallet_name='Test',
        account_name='account 0',
        segwit=False
    )

    assert response == Address(address=data, network=network)
    # noinspection PyUnresolvedReferences
    wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_unused_addresses(mocker: MockerFixture, network, fakeuri, generate_p2pkh_address):
    data = [
        generate_p2pkh_address(network=network),
        generate_p2pkh_address(network=network)
    ]
    mocker.patch.object(Wallet, 'get', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.unused_addresses(
        wallet_name='Test',
        account_name='account 0',
        count=2,
        segwit=False
    )

    assert response == [Address(address=x, network=network) for x in data]
    # noinspection PyUnresolvedReferences
    wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_new_addresses(mocker: MockerFixture, network, fakeuri, generate_p2pkh_address):
    data = [
        generate_p2pkh_address(network=network),
        generate_p2pkh_address(network=network)
    ]
    mocker.patch.object(Wallet, 'get', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.new_addresses(
        wallet_name='Test',
        account_name='account 0',
        count=2,
        segwit=False
    )

    assert response == [Address(address=x, network=network) for x in data]
    # noinspection PyUnresolvedReferences
    wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_addresses(mocker: MockerFixture, network, fakeuri, generate_p2pkh_address):
    data = {
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
    mocker.patch.object(Wallet, 'get', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.addresses(
        wallet_name='Test',
        account_name='account 0',
        segwit=False
    )

    assert response == AddressesModel(**data)
    # noinspection PyUnresolvedReferences
    wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_remove_transactions(mocker: MockerFixture, network, fakeuri, generate_uint256):
    ids = [
        generate_uint256,
        generate_uint256
    ]
    data = [
        {
            'transactionId': ids[0],
            'creationTime': '2020-01-01T00:00:01'
        },
        {
            'transactionId': ids[1],
            'creationTime': '2020-01-01T00:00:01'
        }
    ]
    mocker.patch.object(Wallet, 'delete', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.remove_transactions(
        wallet_name='Test',
        ids=ids,
        from_date='2020-01-01T00:00:01',
        all=True,
        resync=True
    )

    assert response == [RemovedTransactionModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    wallet.delete.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_remove_wallet(mocker: MockerFixture, network, fakeuri):
    data = None
    mocker.patch.object(Wallet, 'delete', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    wallet.remove_wallet(wallet_name='Test')

    # noinspection PyUnresolvedReferences
    wallet.delete.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_extpubkey(mocker: MockerFixture, network, fakeuri, generate_extpubkey):
    data = generate_extpubkey
    mocker.patch.object(Wallet, 'get', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.extpubkey(wallet_name='Test', account_name='account 0')

    assert str(response) == str(ExtPubKey(data))
    # noinspection PyUnresolvedReferences
    wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_private_key(mocker: MockerFixture, network, fakeuri, generate_privatekey, generate_p2pkh_address):
    data = generate_privatekey()
    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.private_key(
        password='password',
        wallet_name='Test',
        address=Address(address=generate_p2pkh_address(network=network), network=network)
    )

    assert response == data
    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_sync(mocker: MockerFixture, network, fakeuri, generate_uint256):
    data = None
    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    wallet.sync(block_hash=generate_uint256)

    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_sync_from_date(mocker: MockerFixture, network, fakeuri):
    data = None
    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    wallet.sync_from_date(
        date='2020-01-01T00:00:01',
        all=True,
        wallet_name='Test'
    )

    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_wallet_stats(mocker: MockerFixture, network, fakeuri):
    data = {
        'walletName': 'Test',
        'totalUtxoCount': 1,
        'uniqueTransactionCount': 1,
        'uniqueBlockCount': 1,
        'countOfTransactionsWithAtLeastMaxReorgConfirmations': 1,
        'utxoAmounts': [
            {
                'amount': 5,
                'Count': 1
            }
        ],
        'utxoPerTransaction': [
            {
                'utxoPerTransaction': 1,
                'Count': 1
            }
        ],
        'utxoPerBlock': [
            {
                'utxoPerBlock': 1,
                'Count': 1
            }
        ]
    }
    mocker.patch.object(Wallet, 'get', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.wallet_stats(
        wallet_name=data['walletName'],
        account_name='account 0',
        min_confirmations=0,
        verbose=True
    )

    assert response == WalletStatsModel(**data)
    # noinspection PyUnresolvedReferences
    wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_split_coins(mocker: MockerFixture, network, fakeuri, generate_uint256, generate_p2pkh_address):
    data = {
        'transactionId': generate_uint256,
        'outputs': [
            {
                'address': generate_p2pkh_address(network=network),
                'amount': '1',
                'OpReturnData': ''
            },
            {
                'address': generate_p2pkh_address(network=network),
                'amount': '1',
                'OpReturnData': ''
            },
            {
                'address': generate_p2pkh_address(network=network),
                'amount': '1',
                'OpReturnData': ''
            },
            {
                'address': generate_p2pkh_address(network=network),
                'amount': '1',
                'OpReturnData': ''
            },
            {
                'address': generate_p2pkh_address(network=network),
                'amount': '1',
                'OpReturnData': ''
            },
        ]
    }
    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.split_coins(
        wallet_name='Test',
        account_name='account 0',
        wallet_password='password',
        total_amount_to_split=Money(5),
        utxos_count=5
    )

    assert response == WalletSendTransactionModel(**data)
    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_distribute_utxos(mocker: MockerFixture, network, fakeuri, generate_uint256, generate_p2pkh_address):
    data = {
        'walletName': 'Test',
        'useUniqueAddressPerUtxo': True,
        'utxosCount': 5,
        'utxoPerTransaction': 1,
        'timestampDifferenceBetweenTransactions': 1,
        'minConfirmations': 0,
        'dryRun': True,
        'walletSendTransaction': [
            {
                'transactionId': generate_uint256,
                'outputs': [
                    {
                        'address': generate_p2pkh_address(network=network),
                        'amount': '1',
                        'OpReturnData': ''
                    },
                    {
                        'address': generate_p2pkh_address(network=network),
                        'amount': '1',
                        'OpReturnData': ''
                    },
                    {
                        'address': generate_p2pkh_address(network=network),
                        'amount': '1',
                        'OpReturnData': ''
                    },
                    {
                        'address': generate_p2pkh_address(network=network),
                        'amount': '1',
                        'OpReturnData': ''
                    },
                    {
                        'address': generate_p2pkh_address(network=network),
                        'amount': '1.0',
                        'OpReturnData': ''
                    },
                ]
            }
        ]
    }

    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.distribute_utxos(
        wallet_name='Test',
        account_name='account 0',
        wallet_password='password',
        use_unique_address_per_utxo=True,
        reuse_addresses=False,
        use_change_addresses=False,
        utxos_count=5,
        utxo_per_transaction=1,
        timestamp_difference_between_transactions=1,
        min_confirmations=0,
        outpoints=[Outpoint(transaction_id=generate_uint256, index=0)],
        dry_run=True
    )

    assert response == DistributeUtxoModel(**data)
    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_sweep(mocker: MockerFixture, network, fakeuri, generate_privatekey, generate_uint256,
               generate_p2pkh_address):
    private_keys = [
        generate_privatekey(),
        generate_privatekey(),
        generate_privatekey()
    ]
    data = [
        generate_uint256,
        generate_uint256,
        generate_uint256
    ]
    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.sweep(
        private_keys=private_keys,
        destination_address=Address(address=generate_p2pkh_address(network=network), network=network),
        broadcast=False
    )

    assert response == [uint256(x) for x in data]
    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_build_offline_sign_request(mocker: MockerFixture, network, fakeuri, generate_p2pkh_address,
                                    generate_uint256, generate_hexstring, get_base_keypath):
    data = {
        'walletName': 'Test',
        'walletAccount': 'account 0',
        'fee': 10000,
        'unsignedTransaction': generate_hexstring(256),
        'utxos': [{
            'transactionId': generate_uint256,
            'index': 0,
            'scriptPubKey': f'OP_DUP OP_HASH160 {generate_hexstring(40)} OP_EQUALVERIFY OP_CHECKSIG',
            'amount': '10.0'
        }],
        'addresses': [{
            'address': generate_p2pkh_address(network=network),
            'keyPath': get_base_keypath,
            'addressType': 'p2pkh'
        }]
    }

    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.build_offline_sign_request(
        fee_amount=Money(0.0001),
        wallet_name=data['walletName'],
        account_name=data['walletAccount'],
        outpoints=[Outpoint(transaction_id=generate_uint256, index=0)],
        recipients=[
            Recipient(
                destination_address=Address(address=generate_p2pkh_address(network=network), network=network),
                destination_script=Address(address=generate_p2pkh_address(network=network), network=network),
                subtraction_fee_from_amount=True,
                amount=Money(10)
            )
        ],
        op_return_data='opreturn',
        op_return_amount=Money(0.00000001),
        allow_unconfirmed=True,
        shuffle_outputs=True,
        change_address=Address(address=generate_p2pkh_address(network=network), network=network)
    )

    assert response == BuildOfflineSignModel(**data)
    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_offline_sign_request(mocker: MockerFixture, network, fakeuri, get_base_keypath,
                              generate_uint256, generate_hexstring, generate_p2pkh_address):
    data = {
        'fee': 10000,
        'hex': generate_hexstring(128),
        'transactionId': generate_uint256
    }
    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.offline_sign_request(
        wallet_password='password',
        wallet_name='Test',
        wallet_account='account 0',
        unsigned_transaction=generate_hexstring(128),
        fee=Money(0.0001),
        utxos=[
            UtxoDescriptor(
                transaction_id=generate_uint256,
                index=0,
                script_pubkey='scriptpubkey',
                amount=Money(1)
            )
        ],
        addresses=[
            AddressDescriptor(
                address=Address(address=generate_p2pkh_address(network=network), network=network),
                key_path=get_base_keypath,
                address_type='p2pkh'
            )
        ]
    )

    assert response == BuildTransactionModel(**data)
    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_consolidate(mocker: MockerFixture, network, fakeuri, generate_p2pkh_address, generate_hexstring):
    data = generate_hexstring(128)
    mocker.patch.object(Wallet, 'post', return_value=data)
    wallet = Wallet(network=network, baseuri=fakeuri)

    response = wallet.consolidate(
        wallet_password='password',
        wallet_name='Test',
        wallet_account='account 0',
        destination_address=Address(address=generate_p2pkh_address(network=network), network=network),
        utxo_value_threshold_in_satoshis=100_0000_0000,
        broadcast=False
    )

    assert response == data
    # noinspection PyUnresolvedReferences
    wallet.post.assert_called_once()
