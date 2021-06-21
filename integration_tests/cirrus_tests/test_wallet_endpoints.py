import pytest
from nodes import CirrusMinerNode
from api import APIError
from api.wallet.requestmodels import *
from api.wallet.responsemodels import *
from pybitcoin.types import Money, Address, uint256, hexstr
from pybitcoin import Recipient, Outpoint, DestinationChain, PubKey, ExtPubKey, AccountBalanceModel, AddressModel
from pybitcoin.networks import CirrusRegTest


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_mnemonic(cirrusminer_node: CirrusMinerNode):
    request_model = MnemonicRequest(language='English', word_count=12)
    response = cirrusminer_node.wallet.mnemonic(request_model)
    assert len(response) == 12
    for item in response:
        assert isinstance(item, str)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_create(cirrusminer_node: CirrusMinerNode):
    request_model = MnemonicRequest(language='English', word_count=12)
    mnemonic = cirrusminer_node.wallet.mnemonic(request_model)
    mnemonic = ' '.join(mnemonic)
    request_model = CreateRequest(
        mnemonic=mnemonic,
        password='password',
        passphrase='passphrase',
        name='TestCreate'
    )
    response = cirrusminer_node.wallet.create(request_model)
    assert isinstance(response, list)
    assert len(response) == 12


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_sign_message(cirrusminer_node: CirrusMinerNode, get_node_address_with_balance):
    message = 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.'
    address = get_node_address_with_balance(cirrusminer_node)
    request_model = SignMessageRequest(
        wallet_name='Test',
        password='password',
        external_address=address,
        message=message
    )
    response = cirrusminer_node.wallet.sign_message(request_model)
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_pubkey(cirrusminer_node: CirrusMinerNode, get_node_address_with_balance):
    address = get_node_address_with_balance(cirrusminer_node)
    request_model = PubKeyRequest(wallet_name='Test', external_address=address)
    response = cirrusminer_node.wallet.pubkey(request_model)
    assert isinstance(response, PubKey)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_verify_message(cirrusminer_node: CirrusMinerNode, get_node_address_with_balance):
    message = 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.'
    address = get_node_address_with_balance(cirrusminer_node)
    request_model = SignMessageRequest(
        wallet_name='Test',
        password='password',
        external_address=address,
        message=message
    )
    signature = cirrusminer_node.wallet.sign_message(request_model)
    request_model = VerifyMessageRequest(
        signature=signature,
        external_address=address,
        message=message
    )
    assert cirrusminer_node.wallet.verify_message(request_model)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_load(cirrusminer_node: CirrusMinerNode):
    request_model = LoadRequest(name='Test', password='password')
    cirrusminer_node.wallet.load(request_model)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_recover(cirrusminer_node: CirrusMinerNode, get_datetime):
    request_model = MnemonicRequest(language='English', word_count=12)
    mnemonic = cirrusminer_node.wallet.mnemonic(request_model)
    mnemonic = ' '.join(mnemonic)
    request_model = RecoverRequest(
        mnemonic=mnemonic,
        password='password',
        passphrase='passphrase',
        name='TestRecover',
        creation_date=get_datetime(365)
    )
    cirrusminer_node.wallet.recover(request_model)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_recover_via_extpubkey(cirrusminer_node: CirrusMinerNode, get_datetime):
    request_model = ExtPubKeyRequest(wallet_name='Test', account_name='account 0')
    extpubkey = cirrusminer_node.wallet.extpubkey(request_model)
    request_model = ExtPubRecoveryRequest(
        extpubkey=extpubkey,
        account_index=0,
        name='TestRecoverPubkey',
        creation_date=get_datetime(365)
    )
    cirrusminer_node.wallet.recover_via_extpubkey(request_model)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_general_info(cirrusminer_node: CirrusMinerNode):
    request_model = GeneralInfoRequest(name='Test')
    response = cirrusminer_node.wallet.general_info(request_model)
    assert isinstance(response, WalletGeneralInfoModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_transaction_count(cirrusminer_node: CirrusMinerNode):
    request_model = AccountRequest(wallet_name='Test', account_name='account 0')
    response = cirrusminer_node.wallet.transaction_count(request_model)
    assert isinstance(response, int)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_history(cirrusminer_node: CirrusMinerNode, get_node_address_with_balance):
    address = get_node_address_with_balance(cirrusminer_node)
    request_model = HistoryRequest(
        wallet_name='Test',
        account_name='account 0',
        address=address,
        skip=2,
        take=2,
        prev_output_tx_time=0,
        prev_output_index=0,
        search_query='query'
    )
    response = cirrusminer_node.wallet.history(request_model)
    assert isinstance(response, WalletHistoryModel)
    for item in response.history:
        assert isinstance(item, AccountHistoryModel)
        for transaction in item.transactions_history:
            assert isinstance(transaction, TransactionItemModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_balance(cirrusminer_node: CirrusMinerNode):
    request_model = BalanceRequest(
        wallet_name='Test',
        account_name='account 0',
        include_balance_by_address=True
    )
    response = cirrusminer_node.wallet.balance(request_model)
    assert isinstance(response, WalletBalanceModel)
    for item in response.balances:
        assert isinstance(item, AccountBalanceModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_received_by_address(cirrusminer_node: CirrusMinerNode, get_node_address_with_balance):
    address = get_node_address_with_balance(cirrusminer_node)
    request_model = ReceivedByAddressRequest(address=address)
    response = cirrusminer_node.wallet.received_by_address(request_model)
    assert isinstance(response, AddressBalanceModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_max_balance(cirrusminer_node: CirrusMinerNode):
    request_model = MaxBalanceRequest(
        wallet_name='Test',
        account_name='account 0',
        fee_type='low',
        allow_unconfirmed=True
    )
    response = cirrusminer_node.wallet.max_balance(request_model)
    assert isinstance(response, MaxSpendableAmountModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_spendable_transactions(cirrusminer_node: CirrusMinerNode, wait_n_blocks_and_sync):
    wait_n_blocks_and_sync(1)
    request_model = SpendableTransactionsRequest(wallet_name='Test', account_name='account 0', min_confirmations=0)
    response = cirrusminer_node.wallet.spendable_transactions(request_model)
    assert isinstance(response, SpendableTransactionsModel)
    for item in response.transactions:
        assert isinstance(item, SpendableTransactionModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_estimate_txfee(
        cirrusminer_node: CirrusMinerNode,
        cirrusminer_syncing_node: CirrusMinerNode,
        get_spendable_transactions,
        get_node_unused_address,
        wait_n_blocks_and_sync,
        get_node_address_with_balance):
    wait_n_blocks_and_sync(2)
    destination_address = get_node_unused_address(cirrusminer_syncing_node)
    change_address = get_node_address_with_balance(cirrusminer_node)
    amount_to_send = Money(10)
    op_return_amount = Money(0.00000001)
    transactions = get_spendable_transactions(node=cirrusminer_node, amount=amount_to_send, op_return_amount=op_return_amount, wallet_name='Test')

    request_model = EstimateTxFeeRequest(
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=x.transaction_id, index=x.index) for x in transactions],
        recipients=[Recipient(destination_address=destination_address, subtraction_fee_from_amount=True, amount=amount_to_send)],
        op_return_data='opreturn test data',
        op_return_amount=op_return_amount,
        fee_type='low',
        allow_unconfirmed=False,
        shuffle_outputs=True,
        change_address=change_address
    )
    response = cirrusminer_node.wallet.estimate_txfee(request_model)
    assert isinstance(response, Money)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_build_transaction(
        cirrusminer_node: CirrusMinerNode,
        cirrusminer_syncing_node: CirrusMinerNode,
        get_spendable_transactions,
        get_node_unused_address,
        wait_n_blocks_and_sync,
        get_node_address_with_balance):
    wait_n_blocks_and_sync(1)
    destination_address = get_node_unused_address(cirrusminer_syncing_node)
    change_address = get_node_address_with_balance(cirrusminer_node)
    fee_amount = Money(0.0001)
    amount_to_send = Money(10)
    op_return_amount = Money(0.00000001)
    transactions = get_spendable_transactions(node=cirrusminer_node, amount=amount_to_send, op_return_amount=op_return_amount, wallet_name='Test')

    request_model = BuildTransactionRequest(
        fee_amount=fee_amount,
        password='password',
        segwit_change_address=False,
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=x.transaction_id, index=x.index) for x in transactions],
        recipients=[Recipient(destination_address=destination_address, subtraction_fee_from_amount=True, amount=amount_to_send)],
        op_return_data='opreturn',
        op_return_amount=op_return_amount,
        allow_unconfirmed=False,
        shuffle_outputs=True,
        change_address=change_address
    )
    response = cirrusminer_node.wallet.build_transaction(request_model)
    assert isinstance(response, BuildTransactionModel)
    assert isinstance(response.transaction_id, uint256)
    assert isinstance(response.hex, hexstr)
    assert isinstance(response.fee, Money)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_build_interflux_transaction(
        cirrusminer_node: CirrusMinerNode,
        cirrusminer_syncing_node: CirrusMinerNode,
        get_spendable_transactions,
        wait_n_blocks_and_sync,
        generate_p2sh_address,
        generate_ethereum_checksum_address,
        get_node_address_with_balance,
        get_node_unused_address):
    wait_n_blocks_and_sync(1)
    destination_address = get_node_unused_address(cirrusminer_syncing_node)
    change_address = get_node_address_with_balance(cirrusminer_node)
    fee_amount = Money(0.0001)
    amount_to_send = Money(10)
    op_return_amount = Money(0.00000001)
    transactions = get_spendable_transactions(node=cirrusminer_node, amount=amount_to_send, op_return_amount=op_return_amount, wallet_name='Test')

    request_model = BuildInterfluxTransactionRequest(
        destination_chain=DestinationChain.ETH,
        destination_address=Address(address=generate_p2sh_address, network=CirrusRegTest()),
        fee_amount=fee_amount,
        password='password',
        segwit_change_address=False,
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=x.transaction_id, index=x.index) for x in transactions],
        recipients=[Recipient(destination_address=destination_address, subtraction_fee_from_amount=True, amount=amount_to_send)],
        op_return_data=generate_ethereum_checksum_address,
        op_return_amount=op_return_amount,
        allow_unconfirmed=False,
        shuffle_outputs=True,
        change_address=change_address
    )
    response = cirrusminer_node.wallet.build_interflux_transaction(request_model)
    assert isinstance(response, BuildTransactionModel)
    assert isinstance(response.transaction_id, uint256)
    assert isinstance(response.hex, hexstr)
    assert isinstance(response.fee, Money)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_send_transaction(cirrusminer_node: CirrusMinerNode,
                          cirrusminer_syncing_node: CirrusMinerNode,
                          get_spendable_transactions,
                          wait_n_blocks_and_sync,
                          get_node_address_with_balance,
                          get_node_unused_address):
    wait_n_blocks_and_sync(1)
    destination_address = get_node_unused_address(cirrusminer_syncing_node)
    change_address = get_node_address_with_balance(cirrusminer_node)
    fee_amount = Money(0.0001)
    amount_to_send = Money(10)
    op_return_amount = Money(0.00000001)
    transactions = get_spendable_transactions(node=cirrusminer_node, amount=amount_to_send, op_return_amount=op_return_amount, wallet_name='Test')

    request_model = BuildTransactionRequest(
        fee_amount=fee_amount,
        password='password',
        segwit_change_address=False,
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=x.transaction_id, index=x.index) for x in transactions],
        recipients=[Recipient(destination_address=destination_address, subtraction_fee_from_amount=True, amount=amount_to_send)],
        op_return_data='opreturn',
        op_return_amount=op_return_amount,
        allow_unconfirmed=False,
        shuffle_outputs=True,
        change_address=change_address
    )
    built_transaction = cirrusminer_node.wallet.build_transaction(request_model)

    request_model = SendTransactionRequest(hex=built_transaction.hex)
    response = cirrusminer_node.wallet.send_transaction(request_model)
    wait_n_blocks_and_sync(1)
    assert isinstance(response, WalletSendTransactionModel)
    assert isinstance(response.transaction_id, uint256)
    for item in response.outputs:
        assert isinstance(item, TransactionOutputModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_list_wallets(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.wallet.list_wallets()
    assert isinstance(response, dict)
    assert 'walletNames' in response
    assert 'watchOnlyWallets' in response


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_account(cirrusminer_node: CirrusMinerNode):
    request_model = GetUnusedAccountRequest(password='password', wallet_name='Test')
    response = cirrusminer_node.wallet.account(request_model)
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_accounts(cirrusminer_node: CirrusMinerNode):
    request_model = GetAccountsRequest(wallet_name='Test')
    response = cirrusminer_node.wallet.accounts(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, str)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_unused_address(cirrusminer_node: CirrusMinerNode):
    request_model = GetUnusedAddressRequest(wallet_name='Test', account_name='account 0', segwit=False)
    response = cirrusminer_node.wallet.unused_address(request_model)
    assert isinstance(response, Address)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_unused_addresses(cirrusminer_node: CirrusMinerNode):
    request_model = GetUnusedAddressesRequest(
        wallet_name='Test',
        account_name='account 0',
        count=2,
        segwit=False
    )
    response = cirrusminer_node.wallet.unused_addresses(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, Address)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_new_addresses(cirrusminer_node: CirrusMinerNode):
    request_model = GetNewAddressesRequest(
        wallet_name='Test',
        account_name='account 0',
        count=2,
        segwit=False
    )
    response = cirrusminer_node.wallet.new_addresses(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, Address)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_addresses(cirrusminer_node: CirrusMinerNode):
    request_model = GetAddressesRequest(wallet_name='Test', account_name='account 0', segwit=False)
    response = cirrusminer_node.wallet.addresses(request_model)
    assert isinstance(response, AddressesModel)
    for item in response.addresses:
        assert isinstance(item, AddressModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_remove_transactions(cirrusminer_node: CirrusMinerNode, wait_n_blocks_and_sync, get_datetime):
    wait_n_blocks_and_sync(2)
    request_model = SpendableTransactionsRequest(wallet_name='Test', account_name='account 0', min_confirmations=10)
    spendable_transactions = cirrusminer_node.wallet.spendable_transactions(request_model)
    trxids = [x.transaction_id for x in spendable_transactions.transactions]

    request_model = RemoveTransactionsRequest(
        wallet_name='Test',
        ids=trxids[:1],
        resync=True
    )
    try:
        response = cirrusminer_node.wallet.remove_transactions(request_model)
        assert isinstance(response, list)
        for item in response:
            assert isinstance(item, RemovedTransactionModel)
    except APIError:
        # Caught if there are no spendable transactions to remove
        pass
    request_model = RemoveTransactionsRequest(
        wallet_name='Test',
        from_date=get_datetime(365),
        resync=True
    )
    try:
        response = cirrusminer_node.wallet.remove_transactions(request_model)
        assert isinstance(response, list)
        for item in response:
            assert isinstance(item, RemovedTransactionModel)
    except APIError:
        # TODO remove_transactions using 'from_date' not implemented on full node as of release 1.0.9.0
        pass
    
    
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_remove_wallet(cirrusminer_node: CirrusMinerNode):
    request_model = MnemonicRequest(language='English', word_count=12)
    mnemonic = cirrusminer_node.wallet.mnemonic(request_model)
    mnemonic = ' '.join(mnemonic)
    request_model = CreateRequest(
        mnemonic=mnemonic,
        password='password',
        passphrase='passphrase',
        name='TestRemove'
    )
    cirrusminer_node.wallet.create(request_model)
    request_model = RemoveWalletRequest(wallet_name='TestRemove')
    cirrusminer_node.wallet.remove_wallet(request_model)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_extpubkey(cirrusminer_node: CirrusMinerNode):
    request_model = ExtPubKeyRequest(wallet_name='Test', account_name='account 0')
    response = cirrusminer_node.wallet.extpubkey(request_model)
    assert isinstance(response, ExtPubKey)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_private_key(cirrusminer_node: CirrusMinerNode, get_node_address_with_balance):
    address = get_node_address_with_balance(cirrusminer_node)
    request_model = PrivateKeyRequest(password='password', wallet_name='Test', address=address)
    response = cirrusminer_node.wallet.private_key(request_model)
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_sync(cirrusminer_node: CirrusMinerNode):
    from api.consensus.requestmodels import GetBlockHashRequest
    request_model = GetBlockHashRequest(height=1)
    block_hash = cirrusminer_node.consensus.get_blockhash(request_model)
    request_model = SyncRequest(hash=block_hash)
    cirrusminer_node.wallet.sync(request_model)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_sync_from_date(cirrusminer_node: CirrusMinerNode, get_datetime):
    request_model = SyncFromDateRequest(date=get_datetime(365), all=True, wallet_name='Test')
    cirrusminer_node.wallet.sync_from_date(request_model)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_wallet_stats(cirrusminer_node: CirrusMinerNode):
    request_model = StatsRequest(
        wallet_name='Test',
        account_name='account 0',
        min_confirmations=0,
        verbose=True
    )
    response = cirrusminer_node.wallet.wallet_stats(request_model)
    assert isinstance(response, WalletStatsModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_split_coins(cirrusminer_node: CirrusMinerNode, wait_n_blocks_and_sync):
    wait_n_blocks_and_sync(1)
    request_model = SplitCoinsRequest(
        wallet_name='Test',
        account_name='account 0',
        wallet_password='password',
        total_amount_to_split=Money(10),
        utxos_count=5
    )
    response = cirrusminer_node.wallet.split_coins(request_model)
    assert isinstance(response, WalletSendTransactionModel)
    assert isinstance(response.transaction_id, uint256)
    for item in response.outputs:
        assert isinstance(item, TransactionOutputModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_distribute_utxos(cirrusminer_node: CirrusMinerNode, wait_n_blocks_and_sync):
    wait_n_blocks_and_sync(2)
    # Need to split the coins first
    request_model = SplitCoinsRequest(
        wallet_name='Test',
        account_name='account 0',
        wallet_password='password',
        total_amount_to_split=Money(10),
        utxos_count=10
    )
    cirrusminer_node.wallet.split_coins(request_model)
    wait_n_blocks_and_sync(3)
    request_model = SpendableTransactionsRequest(wallet_name='Test', account_name='account 0', min_confirmations=2)
    spendable_transactions = cirrusminer_node.wallet.spendable_transactions(request_model)
    spendable_transactions = [x for x in spendable_transactions.transactions]
    request_model = DistributeUTXOsRequest(
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
        outpoints=[Outpoint(transaction_id=x.transaction_id, index=x.index) for x in spendable_transactions],
        dry_run=True
    )
    response = cirrusminer_node.wallet.distribute_utxos(request_model)
    assert isinstance(response, DistributeUtxoModel)
    for item in response.wallet_send_transaction:
        assert isinstance(item, WalletSendTransactionModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_sweep(cirrusminer_node: CirrusMinerNode, wait_n_blocks_and_sync, get_node_address_with_balance, get_node_unused_address):
    wait_n_blocks_and_sync(3)
    address = get_node_address_with_balance(cirrusminer_node)
    receiving_address = get_node_unused_address(cirrusminer_node)
    request_model = PrivateKeyRequest(
        password='password',
        wallet_name='Test',
        address=address
    )
    private_key = cirrusminer_node.wallet.private_key(request_model)
    request_model = SweepRequest(
        private_keys=[private_key],
        destination_address=receiving_address,
        broadcast=False
    )
    response = cirrusminer_node.wallet.sweep(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, uint256)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_build_offline_sign_request(
        cirrusminer_node: CirrusMinerNode,
        cirrusminer_syncing_node: CirrusMinerNode,
        get_spendable_transactions,
        wait_n_blocks_and_sync,
        get_node_address_with_balance,
        get_node_unused_address):
    wait_n_blocks_and_sync(3)
    destination_address = get_node_unused_address(cirrusminer_syncing_node)
    change_address = get_node_address_with_balance(cirrusminer_node)
    fee_amount = Money(0.0001)
    amount_to_send = Money(10)
    op_return_amount = Money(0.00000001)
    transactions = get_spendable_transactions(node=cirrusminer_node, amount=amount_to_send, op_return_amount=op_return_amount,
                                              wallet_name='Test', min_confirmations=2)

    request_model = BuildOfflineSignRequest(
        fee_amount=fee_amount,
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=x.transaction_id, index=x.index) for x in transactions],
        recipients=[Recipient(destination_address=destination_address, subtraction_fee_from_amount=True, amount=amount_to_send)],
        op_return_data='opreturn',
        op_return_amount=op_return_amount,
        allow_unconfirmed=False,
        shuffle_outputs=True,
        change_address=change_address
    )
    response = cirrusminer_node.wallet.build_offline_sign_request(request_model)
    assert isinstance(response, BuildOfflineSignModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_offline_sign_request(
        cirrusminer_node: CirrusMinerNode,
        cirrusminer_syncing_node: CirrusMinerNode,
        get_spendable_transactions,
        get_node_address_with_balance,
        get_node_unused_address,
        wait_n_blocks_and_sync):
    wait_n_blocks_and_sync(3)
    destination_address = get_node_unused_address(cirrusminer_syncing_node)
    change_address = get_node_address_with_balance(cirrusminer_node)
    fee_amount = Money(0.0001)
    amount_to_send = Money(10)
    op_return_amount = Money(0.00000001)
    transactions = get_spendable_transactions(node=cirrusminer_node, amount=amount_to_send,
                                              op_return_amount=op_return_amount, wallet_name='Test', min_confirmations=2)

    request_model = BuildOfflineSignRequest(
        fee_amount=fee_amount,
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=x.transaction_id, index=x.index) for x in transactions],
        recipients=[Recipient(destination_address=destination_address, subtraction_fee_from_amount=True, amount=amount_to_send)],
        op_return_data='opreturn',
        op_return_amount=op_return_amount,
        allow_unconfirmed=False,
        shuffle_outputs=True,
        change_address=change_address
    )
    offline_sign_model = cirrusminer_node.wallet.build_offline_sign_request(request_model)

    request_model = OfflineSignRequest(
        wallet_password='password',
        wallet_name='Test',
        wallet_account='account 0',
        unsigned_transaction=offline_sign_model.unsigned_transaction,
        fee=offline_sign_model.fee,
        utxos=offline_sign_model.utxos,
        addresses=offline_sign_model.addresses
    )
    # Occasionally this will fail because of regtest environment setup. Try, try again.
    for i in range(5):
        try:
            response = cirrusminer_node.wallet.offline_sign_request(request_model)
            assert isinstance(response, BuildTransactionModel)
            assert isinstance(response.transaction_id, uint256)
            assert isinstance(response.hex, hexstr)
            assert isinstance(response.fee, Money)
            break
        except APIError as e:
            if i == 4:
                raise e


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_consolidate(cirrusminer_node: CirrusMinerNode,
                     cirrusminer_syncing_node: CirrusMinerNode,
                     get_node_address_with_balance,
                     wait_n_blocks_and_sync):
    wait_n_blocks_and_sync(2)
    # Need to split the coins first
    request_model = SplitCoinsRequest(
        wallet_name='Test',
        account_name='account 0',
        wallet_password='password',
        total_amount_to_split=Money(10),
        utxos_count=10
    )
    cirrusminer_node.wallet.split_coins(request_model)
    cirrusminer_syncing_node.wallet.split_coins(request_model)
    wait_n_blocks_and_sync(2)
    request_model = SpendableTransactionsRequest(wallet_name='Test', account_name='account 0', min_confirmations=10)
    spendable_transactions = cirrusminer_node.wallet.spendable_transactions(request_model)
    spendable_transactions = [x for x in spendable_transactions.transactions if x.amount < 100_0000_0000]
    assert len(spendable_transactions) > 1  # Count must be more than 1 to consolidate.
    destination_address = get_node_address_with_balance(cirrusminer_node)
    request_model = ConsolidateRequest(
        wallet_password='password',
        wallet_name='Test',
        wallet_account='account 0',
        destination_address=destination_address,
        utxo_value_threshold_in_satoshis=100_0000_0000,
        broadcast=False
    )
    response = cirrusminer_node.wallet.consolidate(request_model)
    assert isinstance(response, hexstr)
