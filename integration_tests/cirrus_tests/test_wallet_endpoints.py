import pytest
from nodes import BaseNode
from api import APIError
from api.wallet.requestmodels import *
from api.wallet.responsemodels import *
from pybitcoin.types import Money, Address, uint256, hexstr
from pybitcoin import Recipient, Outpoint, DestinationChain, PubKey, ExtPubKey, AccountBalanceModel, AddressModel
from pybitcoin.networks import Ethereum


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_mnemonic(cirrus_hot_node: BaseNode):
    request_model = MnemonicRequest(language='English', word_count=12)
    response = cirrus_hot_node.wallet.mnemonic(request_model)
    assert len(response) == 12
    for item in response:
        assert isinstance(item, str)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_create(cirrus_hot_node: BaseNode):
    request_model = MnemonicRequest(language='English', word_count=12)
    mnemonic = cirrus_hot_node.wallet.mnemonic(request_model)
    mnemonic = ' '.join(mnemonic)
    request_model = CreateRequest(
        mnemonic=mnemonic,
        password='password',
        passphrase='passphrase',
        name='TestCreate'
    )
    response = cirrus_hot_node.wallet.create(request_model)
    assert isinstance(response, list)
    assert len(response) == 12


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_sign_message(cirrus_hot_node: BaseNode, get_node_address_with_balance):
    message = 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.'
    address = get_node_address_with_balance(cirrus_hot_node)
    request_model = SignMessageRequest(
        wallet_name='Test',
        password='password',
        external_address=address,
        message=message
    )
    response = cirrus_hot_node.wallet.sign_message(request_model)
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_pubkey(cirrus_hot_node: BaseNode, get_node_address_with_balance):
    address = get_node_address_with_balance(cirrus_hot_node)
    request_model = PubKeyRequest(wallet_name='Test', external_address=address)
    response = cirrus_hot_node.wallet.pubkey(request_model)
    assert isinstance(response, PubKey)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_verify_message(cirrus_hot_node: BaseNode, get_node_address_with_balance):
    message = 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.'
    address = get_node_address_with_balance(cirrus_hot_node)
    request_model = SignMessageRequest(
        wallet_name='Test',
        password='password',
        external_address=address,
        message=message
    )
    signature = cirrus_hot_node.wallet.sign_message(request_model)
    request_model = VerifyMessageRequest(
        signature=signature,
        external_address=address,
        message=message
    )
    assert cirrus_hot_node.wallet.verify_message(request_model)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_load(cirrus_hot_node: BaseNode):
    request_model = LoadRequest(name='Test', password='password')
    cirrus_hot_node.wallet.load(request_model)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_recover(cirrus_hot_node: BaseNode, get_datetime):
    request_model = MnemonicRequest(language='English', word_count=12)
    mnemonic = cirrus_hot_node.wallet.mnemonic(request_model)
    mnemonic = ' '.join(mnemonic)
    request_model = RecoverRequest(
        mnemonic=mnemonic,
        password='password',
        passphrase='passphrase',
        name='TestRecover',
        creation_date=get_datetime(365)
    )
    cirrus_hot_node.wallet.recover(request_model)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_recover_via_extpubkey(cirrus_hot_node: BaseNode, get_datetime):
    request_model = ExtPubKeyRequest(wallet_name='Test', account_name='account 0')
    extpubkey = cirrus_hot_node.wallet.extpubkey(request_model)
    request_model = ExtPubRecoveryRequest(
        extpubkey=extpubkey,
        account_index=0,
        name='TestRecoverPubkey',
        creation_date=get_datetime(365)
    )
    cirrus_hot_node.wallet.recover_via_extpubkey(request_model)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_general_info(cirrus_hot_node: BaseNode):
    request_model = GeneralInfoRequest(name='Test')
    response = cirrus_hot_node.wallet.general_info(request_model)
    assert isinstance(response, WalletGeneralInfoModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_transaction_count(cirrus_hot_node: BaseNode):
    request_model = AccountRequest(wallet_name='Test', account_name='account 0')
    response = cirrus_hot_node.wallet.transaction_count(request_model)
    assert isinstance(response, int)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_history(cirrus_hot_node: BaseNode, get_node_address_with_balance):
    address = get_node_address_with_balance(cirrus_hot_node)
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
    response = cirrus_hot_node.wallet.history(request_model)
    assert isinstance(response, WalletHistoryModel)
    for item in response.history:
        assert isinstance(item, AccountHistoryModel)
        for transaction in item.transactions_history:
            assert isinstance(transaction, TransactionItemModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_balance(cirrus_hot_node: BaseNode):
    request_model = BalanceRequest(
        wallet_name='Test',
        account_name='account 0',
        include_balance_by_address=True
    )
    response = cirrus_hot_node.wallet.balance(request_model)
    assert isinstance(response, WalletBalanceModel)
    for item in response.balances:
        assert isinstance(item, AccountBalanceModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_received_by_address(cirrus_hot_node: BaseNode, get_node_address_with_balance):
    address = get_node_address_with_balance(cirrus_hot_node)
    request_model = ReceivedByAddressRequest(address=address)
    response = cirrus_hot_node.wallet.received_by_address(request_model)
    assert isinstance(response, AddressBalanceModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_max_balance(cirrus_hot_node: BaseNode):
    request_model = MaxBalanceRequest(
        wallet_name='Test',
        account_name='account 0',
        fee_type='low',
        allow_unconfirmed=True
    )
    response = cirrus_hot_node.wallet.max_balance(request_model)
    assert isinstance(response, MaxSpendableAmountModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_spendable_transactions(cirrus_hot_node: BaseNode):
    request_model = SpendableTransactionsRequest(wallet_name='Test', account_name='account 0', min_confirmations=0)
    response = cirrus_hot_node.wallet.spendable_transactions(request_model)
    assert isinstance(response, SpendableTransactionsModel)
    for item in response.transactions:
        assert isinstance(item, SpendableTransactionModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_estimate_txfee(
        cirrus_hot_node: BaseNode,
        cirrus_syncing_node: BaseNode,
        get_spendable_transactions,
        get_node_unused_address,
        get_node_address_with_balance):
    destination_address = get_node_unused_address(cirrus_syncing_node)
    change_address = get_node_address_with_balance(cirrus_hot_node)
    amount_to_send = Money(10)
    op_return_amount = Money(0.00000001)
    transactions = get_spendable_transactions(node=cirrus_hot_node, amount=amount_to_send, op_return_amount=op_return_amount, wallet_name='Test')

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
    response = cirrus_hot_node.wallet.estimate_txfee(request_model)
    assert isinstance(response, Money)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_build_transaction(
        cirrus_hot_node: BaseNode,
        cirrus_syncing_node,
        get_spendable_transactions,
        get_node_unused_address,
        get_node_address_with_balance):
    destination_address = get_node_unused_address(cirrus_syncing_node)
    change_address = get_node_address_with_balance(cirrus_hot_node)
    fee_amount = Money(0.0001)
    amount_to_send = Money(10)
    op_return_amount = Money(0.00000001)
    transactions = get_spendable_transactions(node=cirrus_hot_node, amount=amount_to_send, op_return_amount=op_return_amount, wallet_name='Test')

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
    response = cirrus_hot_node.wallet.build_transaction(request_model)
    assert isinstance(response, BuildTransactionModel)
    assert isinstance(response.transaction_id, uint256)
    assert isinstance(response.hex, hexstr)
    assert isinstance(response.fee, Money)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_build_interflux_transaction(
        cirrus_hot_node: BaseNode,
        cirrus_syncing_node: BaseNode,
        get_spendable_transactions,
        generate_ethereum_checksum_address,
        get_node_address_with_balance,
        get_node_unused_address):
    destination_address = get_node_unused_address(cirrus_syncing_node)
    change_address = get_node_address_with_balance(cirrus_hot_node)
    fee_amount = Money(0.0001)
    amount_to_send = Money(10)
    op_return_amount = Money(0.00000001)
    transactions = get_spendable_transactions(node=cirrus_hot_node, amount=amount_to_send, op_return_amount=op_return_amount, wallet_name='Test')

    request_model = BuildInterfluxTransactionRequest(
        destination_chain=DestinationChain.ETH,
        destination_address=Address(address=generate_ethereum_checksum_address, network=Ethereum()),
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
    response = cirrus_hot_node.wallet.build_interflux_transaction(request_model)
    assert isinstance(response, BuildTransactionModel)
    assert isinstance(response.transaction_id, uint256)
    assert isinstance(response.hex, hexstr)
    assert isinstance(response.fee, Money)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_send_transaction(cirrus_hot_node: BaseNode, cirrus_syncing_node: BaseNode, get_spendable_transactions,
                          get_node_address_with_balance, get_node_unused_address):
    destination_address = get_node_unused_address(cirrus_syncing_node)
    change_address = get_node_address_with_balance(cirrus_hot_node)
    fee_amount = Money(0.0001)
    amount_to_send = Money(10)
    op_return_amount = Money(0.00000001)
    transactions = get_spendable_transactions(node=cirrus_hot_node, amount=amount_to_send, op_return_amount=op_return_amount, wallet_name='Test')

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
    built_transaction = cirrus_hot_node.wallet.build_transaction(request_model)

    request_model = SendTransactionRequest(hex=built_transaction.hex)
    response = cirrus_hot_node.wallet.send_transaction(request_model)
    assert isinstance(response, WalletSendTransactionModel)
    assert isinstance(response.transaction_id, uint256)
    for item in response.outputs:
        assert isinstance(item, TransactionOutputModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_list_wallets(cirrus_hot_node: BaseNode):
    response = cirrus_hot_node.wallet.list_wallets()
    assert isinstance(response, dict)
    assert 'walletNames' in response
    assert 'watchOnlyWallets' in response


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_account(cirrus_hot_node: BaseNode):
    request_model = GetUnusedAccountRequest(password='password', wallet_name='Test')
    response = cirrus_hot_node.wallet.account(request_model)
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_accounts(cirrus_hot_node: BaseNode):
    request_model = GetAccountsRequest(wallet_name='Test')
    response = cirrus_hot_node.wallet.accounts(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, str)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_unused_address(cirrus_hot_node: BaseNode):
    request_model = GetUnusedAddressRequest(wallet_name='Test', account_name='account 0', segwit=False)
    response = cirrus_hot_node.wallet.unused_address(request_model)
    assert isinstance(response, Address)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_unused_addresses(cirrus_hot_node: BaseNode):
    request_model = GetUnusedAddressesRequest(
        wallet_name='Test',
        account_name='account 0',
        count=2,
        segwit=False
    )
    response = cirrus_hot_node.wallet.unused_addresses(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, Address)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_new_addresses(cirrus_hot_node: BaseNode):
    request_model = GetNewAddressesRequest(
        wallet_name='Test',
        account_name='account 0',
        count=2,
        segwit=False
    )
    response = cirrus_hot_node.wallet.new_addresses(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, Address)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_addresses(cirrus_hot_node: BaseNode):
    request_model = GetAddressesRequest(wallet_name='Test', account_name='account 0', segwit=False)
    response = cirrus_hot_node.wallet.addresses(request_model)
    assert isinstance(response, AddressesModel)
    for item in response.addresses:
        assert isinstance(item, AddressModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_remove_transactions(cirrus_hot_node: BaseNode, get_datetime):
    from api.wallet.requestmodels import SpendableTransactionsRequest
    request_model = SpendableTransactionsRequest(wallet_name='Test', account_name='account 0', min_confirmations=10)
    spendable_transactions = cirrus_hot_node.wallet.spendable_transactions(request_model)
    trxids = [x.transaction_id for x in spendable_transactions.transactions]
    request_model = RemoveTransactionsRequest(
        wallet_name='Test',
        ids=trxids[:2],
        resync=True
    )
    response = cirrus_hot_node.wallet.remove_transactions(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, RemovedTransactionModel)
    request_model = RemoveTransactionsRequest(
        wallet_name='Test',
        from_date=get_datetime(365),
        resync=True
    )
    try:
        response = cirrus_hot_node.wallet.remove_transactions(request_model)
        assert isinstance(response, list)
        for item in response:
            assert isinstance(item, RemovedTransactionModel)
    except APIError:
        # TODO remove_transactions using 'from_date' not implemented on full node as of release 1.0.9.0
        pass
    
    
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_remove_wallet(cirrus_hot_node: BaseNode):
    request_model = MnemonicRequest(language='English', word_count=12)
    mnemonic = cirrus_hot_node.wallet.mnemonic(request_model)
    mnemonic = ' '.join(mnemonic)
    request_model = CreateRequest(
        mnemonic=mnemonic,
        password='password',
        passphrase='passphrase',
        name='TestRemove'
    )
    cirrus_hot_node.wallet.create(request_model)
    request_model = RemoveWalletRequest(wallet_name='TestRemove')
    cirrus_hot_node.wallet.remove_wallet(request_model)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_extpubkey(cirrus_hot_node: BaseNode):
    request_model = ExtPubKeyRequest(wallet_name='Test', account_name='account 0')
    response = cirrus_hot_node.wallet.extpubkey(request_model)
    assert isinstance(response, ExtPubKey)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_private_key(cirrus_hot_node: BaseNode, get_node_address_with_balance):
    address = get_node_address_with_balance(cirrus_hot_node)
    request_model = PrivateKeyRequest(password='password', wallet_name='Test', address=address)
    response = cirrus_hot_node.wallet.private_key(request_model)
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_sync(cirrus_hot_node: BaseNode):
    from api.consensus.requestmodels import GetBlockHashRequest
    request_model = GetBlockHashRequest(height=1)
    block_hash = cirrus_hot_node.consensus.get_blockhash(request_model)
    request_model = SyncRequest(hash=block_hash)
    cirrus_hot_node.wallet.sync(request_model)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_sync_from_date(cirrus_hot_node: BaseNode, get_datetime):
    request_model = SyncFromDateRequest(date=get_datetime(365), all=True, wallet_name='Test')
    cirrus_hot_node.wallet.sync_from_date(request_model)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_wallet_stats(cirrus_hot_node: BaseNode):
    request_model = StatsRequest(
        wallet_name='Test',
        account_name='account 0',
        min_confirmations=0,
        verbose=True
    )
    response = cirrus_hot_node.wallet.wallet_stats(request_model)
    assert isinstance(response, WalletStatsModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_split_coins(cirrus_hot_node: BaseNode, node_mines_some_blocks_and_syncs):
    node_mines_some_blocks_and_syncs(mining_node=cirrus_hot_node, num_blocks_to_mine=15)
    request_model = SplitCoinsRequest(
        wallet_name='Test',
        account_name='account 0',
        wallet_password='password',
        total_amount_to_split=Money(10),
        utxos_count=5
    )
    response = cirrus_hot_node.wallet.split_coins(request_model)
    assert isinstance(response, WalletSendTransactionModel)
    assert isinstance(response.transaction_id, uint256)
    for item in response.outputs:
        assert isinstance(item, TransactionOutputModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_distribute_utxos(cirrus_hot_node: BaseNode, node_mines_some_blocks_and_syncs):
    node_mines_some_blocks_and_syncs(mining_node=cirrus_hot_node, num_blocks_to_mine=15)
    from api.wallet.requestmodels import SpendableTransactionsRequest
    request_model = SpendableTransactionsRequest(wallet_name='Test', account_name='account 0', min_confirmations=10)
    spendable_transactions = cirrus_hot_node.wallet.spendable_transactions(request_model)
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
    response = cirrus_hot_node.wallet.distribute_utxos(request_model)
    assert isinstance(response, DistributeUtxoModel)
    for item in response.wallet_send_transaction:
        assert isinstance(item, WalletSendTransactionModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_sweep(cirrus_hot_node: BaseNode, get_node_address_with_balance):
    address = get_node_address_with_balance(cirrus_hot_node)
    request_model = PrivateKeyRequest(
        password='password',
        wallet_name='Test',
        address=address
    )
    private_key = cirrus_hot_node.wallet.private_key(request_model)
    request_model = SweepRequest(
        private_keys=[private_key],
        destination_address=address,
        broadcast=False
    )
    response = cirrus_hot_node.wallet.sweep(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, uint256)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_build_offline_sign_request(
        cirrus_hot_node: BaseNode,
        cirrus_syncing_node: BaseNode,
        get_spendable_transactions,
        get_node_address_with_balance,
        get_node_unused_address):
    destination_address = get_node_unused_address(cirrus_syncing_node)
    change_address = get_node_address_with_balance(cirrus_hot_node)
    fee_amount = Money(0.0001)
    amount_to_send = Money(10)
    op_return_amount = Money(0.00000001)
    transactions = get_spendable_transactions(node=cirrus_hot_node, fee_amount=fee_amount, amount=amount_to_send, op_return_amount=op_return_amount, wallet_name='Test')

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
    response = cirrus_hot_node.wallet.build_offline_sign_request(request_model)
    assert isinstance(response, BuildOfflineSignModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_offline_sign_request(
        cirrus_hot_node: BaseNode,
        cirrus_syncing_node: BaseNode,
        get_spendable_transactions,
        node_mines_some_blocks_and_syncs,
        get_node_address_with_balance,
        get_node_unused_address):
    node_mines_some_blocks_and_syncs(mining_node=cirrus_hot_node, num_blocks_to_mine=15)
    destination_address = get_node_unused_address(cirrus_syncing_node)
    change_address = get_node_address_with_balance(cirrus_hot_node)
    fee_amount = Money(0.0001)
    amount_to_send = Money(10)
    op_return_amount = Money(0.00000001)
    transactions = get_spendable_transactions(node=cirrus_hot_node, amount=amount_to_send, op_return_amount=op_return_amount, wallet_name='Test')

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
    offline_sign_model = cirrus_hot_node.wallet.build_offline_sign_request(request_model)

    request_model = OfflineSignRequest(
        wallet_password='password',
        wallet_name='Test',
        wallet_account='account 0',
        unsigned_transaction=offline_sign_model.unsigned_transaction,
        fee=offline_sign_model.fee,
        utxos=offline_sign_model.utxos,
        addresses=offline_sign_model.addresses
    )
    response = cirrus_hot_node.wallet.offline_sign_request(request_model)
    assert isinstance(response, BuildTransactionModel)
    assert isinstance(response.transaction_id, uint256)
    assert isinstance(response.hex, hexstr)
    assert isinstance(response.fee, Money)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_consolidate(cirrus_hot_node: BaseNode, get_node_address_with_balance, node_mines_some_blocks_and_syncs):
    node_mines_some_blocks_and_syncs(mining_node=cirrus_hot_node, num_blocks_to_mine=15)
    from api.wallet.requestmodels import SpendableTransactionsRequest
    request_model = SpendableTransactionsRequest(wallet_name='Test', account_name='account 0', min_confirmations=10)
    spendable_transactions = cirrus_hot_node.wallet.spendable_transactions(request_model)
    spendable_transactions = [x for x in spendable_transactions.transactions if x.amount < 100_0000_0000]
    assert len(spendable_transactions) > 1  # Count must be more than 1 to consolidate.
    destination_address = get_node_address_with_balance(cirrus_hot_node)
    request_model = ConsolidateRequest(
        wallet_password='password',
        wallet_name='Test',
        wallet_account='account 0',
        destination_address=destination_address,
        utxo_value_threshold_in_satoshis=100_0000_0000,
        broadcast=False
    )
    response = cirrus_hot_node.wallet.consolidate(request_model)
    assert isinstance(response, hexstr)
