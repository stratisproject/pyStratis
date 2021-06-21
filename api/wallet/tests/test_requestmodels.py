import pytest
import json
import ecdsa
import base64
from pybitcoin import DestinationChain, Outpoint, Recipient, UtxoDescriptor, AddressDescriptor
from pybitcoin.types import Address, Money
from api.wallet.requestmodels import *
from pybitcoin.networks import StraxMain, CirrusMain, Ethereum


def test_accountrequest():
    data = {
        'WalletName': 'Test',
        'AccountName': 'account 0'
    }
    request_model = AccountRequest(
        wallet_name='Test',
        account_name='account 0'
    )
    assert json.dumps(data) == request_model.json()


def test_balancerequest():
    data = {
        'WalletName': 'Test',
        'AccountName': 'account 0',
        'IncludeBalanceByAddress': True
    }
    request_model = BalanceRequest(
        wallet_name='Test',
        account_name='account 0',
        include_balance_by_address=True
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_buildinterfluxtransactionrequest(network, generate_ethereum_checksum_address, generate_uint256,
                                          generate_p2pkh_address, generate_p2sh_address):
    data = {
        'destinationChain': DestinationChain.ETH,
        'destinationAddress': generate_ethereum_checksum_address,
        'feeAmount': '0.00010000',
        'password': 'password',
        'segwitChangeAddress': False,
        'walletName': 'Test',
        'accountName': 'account 0',
        'outpoints': [
            {
                'transactionId': generate_uint256,
                'index': 0
            }
        ],
        'recipients': [
            {
                'destinationAddress': generate_p2pkh_address(network=network),
                'destinationScript': generate_p2sh_address(network=network),
                'subtractFeeFromAmount': True,
                'amount': '10.00000000'
            }
        ],
        'opReturnData': 'opreturn',
        'opReturnAmount': '0.00000001',
        'allowUnconfirmed': True,
        'shuffleOutputs': True,
        'changeAddress': generate_p2pkh_address(network=network)
    }
    request_model = BuildInterfluxTransactionRequest(
        destination_chain=DestinationChain.ETH,
        destination_address=Address(address=data['destinationAddress'], network=Ethereum()),
        fee_amount=Money(0.0001),
        password='password',
        segwit_change_address=False,
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=data['outpoints'][0]['transactionId'], index=0)],
        recipients=[
            Recipient(
                destination_address=Address(address=data['recipients'][0]['destinationAddress'], network=network),
                destination_script=Address(address=data['recipients'][0]['destinationScript'], network=network),
                subtraction_fee_from_amount=True,
                amount=Money(10)
            )
        ],
        op_return_data='opreturn',
        op_return_amount=Money(0.00000001),
        allow_unconfirmed=True,
        shuffle_outputs=True,
        change_address=Address(address=data['changeAddress'], network=network)
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_buildofflinesignrequest(network, generate_uint256, generate_p2pkh_address, generate_p2sh_address):
    data = {
        'feeAmount': '0.00010000',
        'walletName': 'Test',
        'accountName': 'account 0',
        'outpoints': [
            {
                'transactionId': generate_uint256,
                'index': 0
            }
        ],
        'recipients': [
            {
                'destinationAddress': generate_p2pkh_address(network=network),
                'destinationScript': generate_p2sh_address(network=network),
                'subtractFeeFromAmount': True,
                'amount': '10.00000000'
            }
        ],
        'opReturnData': 'opreturn',
        'opReturnAmount': '0.00000001',
        'allowUnconfirmed': True,
        'shuffleOutputs': True,
        'changeAddress': generate_p2pkh_address(network=network)
    }
    request_model = BuildOfflineSignRequest(
        fee_amount=Money(0.0001),
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=data['outpoints'][0]['transactionId'], index=0)],
        recipients=[
            Recipient(
                destination_address=Address(address=data['recipients'][0]['destinationAddress'], network=network),
                destination_script=Address(address=data['recipients'][0]['destinationScript'], network=network),
                subtraction_fee_from_amount=True,
                amount=Money(10)
            )
        ],
        op_return_data='opreturn',
        op_return_amount=Money(0.00000001),
        allow_unconfirmed=True,
        shuffle_outputs=True,
        change_address=Address(address=data['changeAddress'], network=network)
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_buildtransactionrequest(network, generate_uint256, generate_p2pkh_address, generate_p2sh_address):
    data = {
        'feeAmount': '0.00010000',
        'password': 'password',
        'segwitChangeAddress': False,
        'walletName': 'Test',
        'accountName': 'account 0',
        'outpoints': [
            {
                'transactionId': generate_uint256,
                'index': 0
            }
        ],
        'recipients': [
            {
                'destinationAddress': generate_p2pkh_address(network=network),
                'destinationScript': generate_p2sh_address(network=network),
                'subtractFeeFromAmount': True,
                'amount': '10.00000000'
            }
        ],
        'opReturnData': 'opreturn',
        'opReturnAmount': '0.00000001',
        'allowUnconfirmed': True,
        'shuffleOutputs': True,
        'changeAddress': generate_p2pkh_address(network=network)
    }
    request_model = BuildTransactionRequest(
        fee_amount=Money(0.0001),
        password='password',
        segwit_change_address=False,
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=data['outpoints'][0]['transactionId'], index=0)],
        recipients=[
            Recipient(
                destination_address=Address(address=data['recipients'][0]['destinationAddress'], network=network),
                destination_script=Address(address=data['recipients'][0]['destinationScript'], network=network),
                subtraction_fee_from_amount=True,
                amount=Money(10)
            )
        ],
        op_return_data='opreturn',
        op_return_amount=Money(0.00000001),
        allow_unconfirmed=True,
        shuffle_outputs=True,
        change_address=Address(address=data['changeAddress'], network=network)
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_consolidaterequest(network, generate_p2pkh_address):
    data = {
        'walletPassword': 'password',
        'walletName': 'Test',
        'walletAccount': 'account 0',
        'destinationAddress': generate_p2pkh_address(network=network),
        'utxoValueThreshold': 10000000000,
        'broadcast': False
    }
    request_model = ConsolidateRequest(
        wallet_password='password',
        wallet_name='Test',
        wallet_account='account 0',
        destination_address=Address(address=data['destinationAddress'], network=network),
        utxo_value_threshold_in_satoshis=100_0000_0000,
        broadcast=False
    )
    assert json.dumps(data) == request_model.json()


def test_createrequest():
    data = {
        'mnemonic': 'mnemonic',
        'password': 'password',
        'passphrase': 'passphrase',
        'name': 'Test'
    }
    request_model = CreateRequest(
        mnemonic='mnemonic',
        password='password',
        passphrase='passphrase',
        name='Test'
    )
    assert json.dumps(data) == request_model.json()


def test_distributeutxosrequest(generate_uint256):
    data = {
        'walletName': 'Test',
        'accountName': 'account 0',
        'walletPassword': 'password',
        'useUniqueAddressPerUtxo': True,
        'reuseAddresses': False,
        'useChangeAddresses': False,
        'utxosCount': 5,
        'utxoPerTransaction': 5,
        'timestampDifferenceBetweenTransactions': 5,
        'minConfirmations': 0,
        'outpoints': [
            {
                'transactionId': generate_uint256,
                'index': 0
            }
        ],
        'dryRun': True
    }
    # noinspection PyTypeChecker
    request_model = DistributeUTXOsRequest(
        wallet_name='Test',
        account_name='account 0',
        wallet_password='password',
        use_unique_address_per_utxo=True,
        reuse_addresses=False,
        use_change_addresses=False,
        utxos_count=5,
        utxo_per_transaction=5,
        timestamp_difference_between_transactions=5,
        min_confirmations=0,
        outpoints=[Outpoint(transaction_id=data['outpoints'][0]['transactionId'], index=0)],
        dry_run=True
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_estimatetxfeerequest(network, generate_uint256, generate_p2pkh_address, generate_p2sh_address):
    data = {
        'walletName': 'Test',
        'accountName': 'account 0',
        'outpoints': [
            {
                'transactionId': generate_uint256,
                'index': 0
            }
        ],
        'recipients': [
            {
                'destinationAddress': generate_p2pkh_address(network=network),
                'destinationScript': generate_p2sh_address(network=network),
                'subtractFeeFromAmount': True,
                'amount': '10.00000000'
            }
        ],
        'opReturnData': 'opreturn',
        'opReturnAmount': '0.00000001',
        'feeType': 'low',
        'allowUnconfirmed': True,
        'shuffleOutputs': True,
        'changeAddress': generate_p2pkh_address(network=network)
    }
    request_model = EstimateTxFeeRequest(
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=data['outpoints'][0]['transactionId'], index=0)],
        recipients=[
            Recipient(
                destination_address=Address(address=data['recipients'][0]['destinationAddress'], network=network),
                destination_script=Address(address=data['recipients'][0]['destinationScript'], network=network),
                subtraction_fee_from_amount=True,
                amount=Money(10)
            )
        ],
        op_return_data='opreturn',
        op_return_amount=Money(0.00000001),
        fee_type='low',
        allow_unconfirmed=True,
        shuffle_outputs=True,
        change_address=Address(address=data['changeAddress'], network=network)
    )
    assert json.dumps(data) == request_model.json()


def test_extpubkeyrequest():
    data = {
        'WalletName': 'Test',
        'AccountName': 'account 0'
    }
    request_model = ExtPubKeyRequest(
        wallet_name='Test',
        account_name='account 0'
    )
    assert json.dumps(data) == request_model.json()


def test_extpubrecoveryrequest(generate_extpubkey):
    data = {
        'extPubKey': generate_extpubkey,
        'accountIndex': 0,
        'name': 'Test',
        'creationDate': '2020-01-01T00:00:01'
    }
    request_model = ExtPubRecoveryRequest(
        extpubkey=data['extPubKey'],
        account_index=0,
        name='Test',
        creation_date='2020-01-01T00:00:01'
    )
    assert json.dumps(data) == request_model.json()


def test_generalinforequest():
    data = {
        'Name': 'Test'
    }
    request_model = GeneralInfoRequest(
        name='Test'
    )
    assert json.dumps(data) == request_model.json()


def test_getaccountsrequest():
    data = {
        'WalletName': 'Test'
    }
    request_model = GetAccountsRequest(
        wallet_name='Test'
    )
    assert json.dumps(data) == request_model.json()


def test_getaddressesrequest():
    data = {
        'WalletName': 'Test',
        'AccountName': 'account 0',
        'Segwit': False
    }
    request_model = GetAddressesRequest(
        wallet_name='Test',
        account_name='account 0',
        segwit=False
    )
    assert json.dumps(data) == request_model.json()


def test_getnewaddressesrequest():
    data = {
        'WalletName': 'Test',
        'AccountName': 'account 0',
        'Count': 2,
        'Segwit': False
    }
    request_model = GetNewAddressesRequest(
        wallet_name='Test',
        account_name='account 0',
        count=2,
        segwit=False
    )
    assert json.dumps(data) == request_model.json()


def test_getunusedaccountrequest():
    data = {
        'password': 'password',
        'walletName': 'Test'
    }
    request_model = GetUnusedAccountRequest(
        password='password',
        wallet_name='Test'
    )
    assert json.dumps(data) == request_model.json()


def test_getunusedaddressesrequest():
    data = {
        'WalletName': 'Test',
        'AccountName': 'account 0',
        'Count': 2,
        'Segwit': False
    }
    request_model = GetUnusedAddressesRequest(
        wallet_name='Test',
        account_name='account 0',
        count=2,
        segwit=False
    )
    assert json.dumps(data) == request_model.json()


def test_getunusedaddressrequest():
    data = {
        'WalletName': 'Test',
        'AccountName': 'account 0',
        'Segwit': False
    }
    request_model = GetUnusedAddressRequest(
        wallet_name='Test',
        account_name='account 0',
        segwit=False
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_historyrequest(network, generate_p2pkh_address):
    data = {
        'WalletName': 'Test',
        'AccountName': 'account 0',
        'Address': generate_p2pkh_address(network=network),
        'Skip': 2,
        'Take': 2,
        'PrevOutputTxTime': 0,
        'PrevOutputIndex': 0,
        'SearchQuery': 'query'
    }
    request_model = HistoryRequest(
        wallet_name='Test',
        account_name='account 0',
        address=Address(address=data['Address'], network=network),
        skip=2,
        take=2,
        prev_output_tx_time=0,
        prev_output_index=0,
        search_query='query'
    )
    assert json.dumps(data) == request_model.json()


def test_loadrequest():
    data = {
        'name': 'Test',
        'password': 'password'
    }
    request_model = LoadRequest(
        name='Test',
        password='password'
    )
    assert json.dumps(data) == request_model.json()


def test_maxbalancerequest():
    data = {
        'WalletName': 'Test',
        'AccountName': 'account 0',
        'FeeType': 'low',
        'AllowUnconfirmed': True
    }
    request_model = MaxBalanceRequest(
        wallet_name='Test',
        account_name='account 0',
        fee_type='low',
        allow_unconfirmed=True
    )
    assert json.dumps(data) == request_model.json()


def test_mnemonicrequest():
    data = {
        'language': 'English',
        'wordCount': 12
    }
    request_model = MnemonicRequest(
        language='English',
        word_count=12
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_offlinesignrequest(network, generate_hexstring, generate_uint256, generate_p2pkh_address, get_base_keypath):
    data = {
        'walletPassword': 'password',
        'walletName': 'Test',
        'walletAccount': 'account 0',
        'unsignedTransaction': generate_hexstring(128),
        'fee': '0.00010000',
        'utxos': [
            {
                'transactionId': generate_uint256,
                'index': 0,
                'scriptPubKey': 'scriptpubkey',
                'amount': '10.00000000'
            }
        ],
        'addresses': [
            {
                'address': generate_p2pkh_address(network=network),
                'keyPath': get_base_keypath,
                'addressType': 'p2pkh'
            }
        ]
    }
    request_model = OfflineSignRequest(
        wallet_password='password',
        wallet_name='Test',
        wallet_account='account 0',
        unsigned_transaction=data['unsignedTransaction'],
        fee=Money(0.0001),
        utxos=[
            UtxoDescriptor(
                transaction_id=data['utxos'][0]['transactionId'],
                index=0,
                script_pubkey='scriptpubkey',
                amount=Money(10)
            )
        ],
        addresses=[
            AddressDescriptor(
                address=Address(address=data['addresses'][0]['address'], network=network),
                key_path=get_base_keypath,
                address_type='p2pkh'
            )
        ]
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_privatekeyrequest(network, generate_p2pkh_address):
    data = {
        'password': 'password',
        'walletName': 'Test',
        'address': generate_p2pkh_address(network=network)
    }
    request_model = PrivateKeyRequest(
        password='password',
        wallet_name='Test',
        address=Address(address=data['address'], network=network)
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_pubkeyrequest(network, generate_p2pkh_address):
    data = {
        'walletName': 'Test',
        'externalAddress': generate_p2pkh_address(network=network)
    }
    request_model = PubKeyRequest(
        wallet_name='Test',
        external_address=Address(address=data['externalAddress'], network=network)
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_receivedbyaddressrequest(network, generate_p2pkh_address):
    data = {
        'Address': generate_p2pkh_address(network=network)
    }
    request_model = ReceivedByAddressRequest(
        address=Address(address=data['Address'], network=network)
    )
    assert json.dumps(data) == request_model.json()


def test_recoverrequest():
    data = {
        'mnemonic': 'mnemonic',
        'password': 'password',
        'passphrase': 'passphrase',
        'name': 'Test',
        'creationDate': '2020-01-01T00:00:01'
    }
    request_model = RecoverRequest(
        mnemonic='mnemonic',
        password='password',
        passphrase='passphrase',
        name='Test',
        creation_date='2020-01-01T00:00:01'
    )
    assert json.dumps(data) == request_model.json()


def test_removetransactionsrequest(generate_uint256):
    data = {
        'WalletName': 'Test',
        'ids': [
            generate_uint256,
            generate_uint256,
            generate_uint256
        ],
        'fromDate': '2020-01-01T00:00:01',
        'all': True,
        'ReSync': True
    }
    request_model = RemoveTransactionsRequest(
        wallet_name='Test',
        ids=data['ids'],
        from_date='2020-01-01T00:00:01',
        all=True,
        resync=True
    )
    assert json.dumps(data) == request_model.json()


def test_removewalletrequest():
    data = {
        'WalletName': 'Test'
    }
    request_model = RemoveWalletRequest(
        wallet_name='Test'
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_signmessagerequest(network, generate_p2pkh_address):
    data = {
        'walletName': 'Test',
        'password': 'password',
        'externalAddress': generate_p2pkh_address(network=network),
        'message': 'message'
    }
    request_model = SignMessageRequest(
        wallet_name='Test',
        password='password',
        external_address=Address(address=data['externalAddress'], network=network),
        message='message'
    )
    assert json.dumps(data) == request_model.json()


def test_spendabletransactionrequest():
    data = {
        'WalletName': 'Test',
        'AccountName': 'account 0',
        'MinConfirmations': 0
    }
    request_model = SpendableTransactionsRequest(
        wallet_name='Test',
        account_name='account 0',
        min_confirmations=0
    )
    assert json.dumps(data) == request_model.json()


def test_splitcoinsrequest():
    data = {
        'walletName': 'Test',
        'accountName': 'account 0',
        'walletPassword': 'password',
        'totalAmountToSplit': '5.00000000',
        'utxosCount': 5
    }
    request_model = SplitCoinsRequest(
        wallet_name='Test',
        account_name='account 0',
        wallet_password='password',
        total_amount_to_split=Money(5),
        utxos_count=5
    )
    assert json.dumps(data) == request_model.json()


def test_statsrequest():
    data = {
        'WalletName': 'Test',
        'AccountName': 'account 0',
        'MinConfirmations': 0,
        'Verbose': True
    }
    request_model = StatsRequest(
        wallet_name='Test',
        account_name='account 0',
        min_confirmations=0,
        verbose=True
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_sweeprequest(network, generate_privatekey, generate_p2pkh_address):
    data = {
        'privateKeys': [
            generate_privatekey(),
            generate_privatekey(),
            generate_privatekey()
        ],
        'destinationAddress': generate_p2pkh_address(network=network),
        'broadcast': False
    }
    request_model = SweepRequest(
        private_keys=data['privateKeys'],
        destination_address=Address(address=data['destinationAddress'], network=network),
        broadcast=False
    )
    data['privateKeys'] = [str(x) for x in data['privateKeys']]
    assert json.dumps(data) == request_model.json()


def test_syncfromdaterequest():
    data = {
        'date': '2020-01-01T00:00:01',
        'all': True,
        'walletName': 'Test'
    }
    request_model = SyncFromDateRequest(
        date='2020-01-01T00:00:01',
        all=True,
        wallet_name='Test'
    )
    assert json.dumps(data) == request_model.json()


def test_syncrequest(generate_uint256):
    data = {
        'hash': generate_uint256
    }
    request_model = SyncRequest(
        hash=data['hash']
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_verifymessagerequest(network, generate_p2pkh_address, generate_privatekey):
    message = 'This is my message'
    private_key_bytes = generate_privatekey().get_bytes()
    key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    sig = base64.b64encode(key.sign(bytes(message, 'ascii'))).decode('ascii')
    data = {
        'signature': sig,
        'externalAddress': generate_p2pkh_address(network=network),
        'message': message
    }
    request_model = VerifyMessageRequest(
        signature=sig,
        external_address=Address(address=data['externalAddress'], network=network),
        message=message
    )
    assert json.dumps(data) == request_model.json()
