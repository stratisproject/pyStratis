from typing import List, Callable
from nodes import BaseNode
from api.wallet.requestmodels import *
from pybitcoin.types import Address, Money, hexstr, uint256
from pybitcoin import ExtPubKey, Recipient, Outpoint, DestinationChain, AddressDescriptor, UtxoDescriptor


def check_wallet_endpoints(
        node: BaseNode,
        internal_address: Address,
        destination_address: Address,
        spendable_transactions: List[uint256],
        eth_address: Address,
        block_hash: uint256,
        extpubkey: ExtPubKey) -> None:
    assert check_mnemonic(node)
    mnemonic = node.wallet.mnemonic(MnemonicRequest(language='English', word_count=12))
    mnemonic = ' '.join(mnemonic)
    assert check_create(node, mnemonic)
    message = 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks'
    assert check_sign_message(node, internal_address, message)
    assert check_pubkey(node, internal_address)
    # assert check_verify_message(node, signature, internal_address, message)
    assert check_load(node)
    assert check_recover(node)
    assert check_recover_via_extpubkey(node, extpubkey)
    assert check_general_info(node)
    assert check_transaction_count(node)
    assert check_history(node, internal_address)
    assert check_balance(node)
    assert check_received_by_address(node, internal_address)
    assert check_max_balance(node)
    assert check_spendable_transactions(node)
    assert check_estimate_txfee(node, destination_address, internal_address, spendable_transactions)
    assert check_build_transaction(node, destination_address, internal_address, spendable_transactions)
    built_transaction = node.wallet.build_transaction()
    assert check_build_interflux_transaction(node, eth_address, destination_address, internal_address, spendable_transactions)
    assert check_send_transaction(node, built_transaction.hex)
    assert check_list_wallets(node)
    assert check_account(node)
    assert check_accounts(node)
    assert check_unused_address(node)
    assert check_unused_addresses(node)
    assert check_new_addresses(node)
    assert check_addresses(node)
    assert check_remove_transactions(node, spendable_transactions)
    assert check_remove_wallet(node)
    assert check_extpubkey(node)
    assert check_private_key(node, internal_address)
    assert check_sync(node, block_hash)
    assert check_sync_from_date(node)
    assert check_wallet_stats(node)
    assert check_split_coins(node)
    assert check_distribute_utxos(node, spendable_transactions)
    private_key = node.wallet.private_key(request_model=PrivateKeyRequest(password='password', wallet_name='Test', address=internal_address))
    private_keys = [private_key]
    assert check_sweep(node, private_keys, destination_address)
    assert check_build_offline_sign_request(node, destination_address, internal_address, spendable_transactions)
    # assert check_offline_sign_request(node, spendable_transactions, key_path, [destination_address], unsigned_transaction)
    assert check_consolidate(node, destination_address)


def check_mnemonic(node: BaseNode) -> bool:
    request_model = MnemonicRequest(language='English', word_count=12)
    node.wallet.mnemonic(request_model)
    return True


def check_create(node: BaseNode, mnemonic: str) -> bool:
    request_model = CreateRequest(
        mnemonic=mnemonic,
        password='password',
        passphrase='passphrase',
        name='Test'
    )
    node.wallet.create(request_model)
    return True


def check_sign_message(node: BaseNode, external_address: Address, message: str) -> bool:
    request_model = SignMessageRequest(
        wallet_name='Test',
        password='password',
        external_address=external_address,
        message=message
    )
    node.wallet.sign_message(request_model)
    return True


def check_pubkey(node: BaseNode, external_address: Address) -> bool:
    request_model = PubKeyRequest(wallet_name='Test', external_address=external_address)
    node.wallet.pubkey(request_model)
    return True


def check_verify_message(node: BaseNode, signature: str, external_address: Address, message: str) -> bool:
    request_model = VerifyMessageRequest(
        signature=signature,
        external_address=external_address,
        message=message
    )
    node.wallet.verify_message(request_model)
    return True


def check_load(node: BaseNode) -> bool:
    request_model = LoadRequest(name='Test', password='password')
    node.wallet.load(request_model)
    return True


def check_recover(node: BaseNode, get_datetime: Callable) -> bool:
    request_model = RecoverRequest(
        mnemonic='mnemonic',
        password='password',
        passphrase='passphrase',
        name='Test',
        creation_date=get_datetime(365)
    )
    node.wallet.recover(request_model)
    return True


def check_recover_via_extpubkey(node: BaseNode, extpubkey: ExtPubKey, get_datetime: Callable) -> bool:
    request_model = ExtPubRecoveryRequest(
        extpubkey=extpubkey,
        account_index=0,
        name='Test',
        creation_date=get_datetime(365)
    )
    node.wallet.recover_via_extpubkey(request_model)
    return True


def check_general_info(node: BaseNode) -> bool:
    request_model = GeneralInfoRequest(name='Test')
    node.wallet.general_info(request_model)
    return True


def check_transaction_count(node: BaseNode) -> bool:
    request_model = AccountRequest(wallet_name='Test', account_name='account 0')
    node.wallet.transaction_count(request_model)
    return True


def check_history(node: BaseNode, address: Address) -> bool:
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
    node.wallet.history(request_model)
    return True


def check_balance(node: BaseNode) -> bool:
    request_model = BalanceRequest(
        wallet_name='Test',
        account_name='account 0',
        include_balance_by_address=True
    )
    node.wallet.balance(request_model)
    return True


def check_received_by_address(node: BaseNode, address: Address) -> bool:
    request_model = ReceivedByAddressRequest(address=address)
    node.wallet.received_by_address(request_model)
    return True


def check_max_balance(node: BaseNode) -> bool:
    request_model = MaxBalanceRequest(
        wallet_name='Test',
        account_name='account 0',
        fee_type='low',
        allow_unconfirmed=True
    )
    node.wallet.max_balance(request_model)
    return True


def check_spendable_transactions(node: BaseNode) -> bool:
    request_model = SpendableTransactionsRequest(wallet_name='Test', account_name='account 0', min_confirmations=0)
    node.wallet.spendable_transactions(request_model)
    return True


def check_estimate_txfee(
        node: BaseNode,
        destination_address: Address,
        change_address: Address,
        trxids: List[uint256]) -> bool:
    request_model = EstimateTxFeeRequest(
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=x, index=0) for x in trxids],
        recipients=[
            Recipient(
                destination_address=destination_address,
                destination_script=destination_address,
                subtraction_fee_from_amount=True,
                amount=Money(100000)
            )
        ],
        op_return_data='opreturn test data',
        op_return_amount=Money(1),
        fee_type='low',
        allow_unconfirmed=True,
        shuffle_outputs=True,
        change_address=change_address
    )
    node.wallet.estimate_txfee(request_model)
    return True


def check_build_transaction(
        node: BaseNode,
        destination_address: Address,
        change_address: Address,
        trxids: List[uint256]) -> bool:
    request_model = BuildTransactionRequest(
        fee_amount=Money(10000),
        password='password',
        segwit_change_address=False,
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=x, index=0) for x in trxids],
        recipients=[
            Recipient(
                destination_address=destination_address,
                destination_script=destination_address,
                subtraction_fee_from_amount=True,
                amount=Money(100000)
            )
        ],
        op_return_data='opreturn',
        op_return_amount=Money(1),
        fee_type='low',
        allow_unconfirmed=True,
        shuffle_outputs=True,
        change_address=change_address
    )
    node.wallet.build_transaction(request_model)
    return True


def check_build_interflux_transaction(
        node: BaseNode,
        eth_address: Address,
        destination_address: Address,
        change_address: Address,
        trxids: List[uint256]) -> bool:
    request_model = BuildInterfluxTransactionRequest(
        destination_chain=DestinationChain.ETH,
        destination_address=eth_address,
        fee_amount=Money(10000),
        password='password',
        segwit_change_address=False,
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=x, index=0) for x in trxids],
        recipients=[
            Recipient(
                destination_address=destination_address,
                destination_script=destination_address,
                subtraction_fee_from_amount=True,
                amount=Money(100000)
            )
        ],
        op_return_data='opreturn',
        op_return_amount=Money(1),
        fee_type='low',
        allow_unconfirmed=True,
        shuffle_outputs=True,
        change_address=change_address
    )
    node.wallet.build_interflux_transaction(request_model)
    return True


def check_send_transaction(node: BaseNode, transaction_hex: hexstr) -> bool:
    request_model = SendTransactionRequest(hex=transaction_hex)
    node.wallet.send_transaction(request_model)
    return True


def check_list_wallets(node: BaseNode) -> bool:
    node.wallet.list_wallets()
    return True


def check_account(node: BaseNode) -> bool:
    request_model = GetUnusedAccountRequest(password='password', wallet_name='Test')
    node.wallet.account(request_model)
    return True


def check_accounts(node: BaseNode) -> bool:
    request_model = GetAccountsRequest(wallet_name='Test')
    node.wallet.accounts(request_model)
    return True


def check_unused_address(node: BaseNode) -> bool:
    request_model = GetUnusedAddressRequest(wallet_name='Test', account_name='account 0', segwit=False)
    node.wallet.unused_address(request_model)
    return True


def check_unused_addresses(node: BaseNode) -> bool:
    request_model = GetUnusedAddressesRequest(
        wallet_name='Test',
        account_name='account 0',
        count=2,
        segwit=False
    )
    node.wallet.unused_addresses(request_model)
    return True


def check_new_addresses(node: BaseNode) -> bool:
    request_model = GetNewAddressesRequest(
        wallet_name='Test',
        account_name='account 0',
        count=2,
        segwit=False
    )

    node.wallet.new_addresses(request_model)
    return True


def check_addresses(node: BaseNode) -> bool:
    request_model = GetAddressesRequest(wallet_name='Test', account_name='account 0', segwit=False)
    node.wallet.addresses(request_model)
    return True


def check_remove_transactions(node: BaseNode, trxids: List[uint256], get_datetime: Callable) -> bool:
    request_model = RemoveTransactionsRequest(
        wallet_name='Test',
        ids=trxids,
        from_date=get_datetime(365),
        all=True,
        resync=True
    )
    node.wallet.remove_transactions(request_model)
    return True


def check_remove_wallet(node: BaseNode) -> bool:
    request_model = RemoveWalletRequest(wallet_name='Test')
    node.wallet.remove_wallet(request_model)
    return True


def check_extpubkey(node: BaseNode) -> bool:
    request_model = ExtPubKeyRequest(wallet_name='Test', account_name='account 0')
    node.wallet.extpubkey(request_model)
    return True


def check_private_key(node: BaseNode, address: Address) -> bool:
    request_model = PrivateKeyRequest(password='password', wallet_name='Test', address=address)
    node.wallet.private_key(request_model)
    return True


def check_sync(node: BaseNode, block_hash: uint256) -> bool:
    request_model = SyncRequest(hash=block_hash)
    node.wallet.sync(request_model)
    return True


def check_sync_from_date(node: BaseNode, get_datetime: Callable) -> bool:
    request_model = SyncFromDateRequest(date=get_datetime(365), all=True, wallet_name='Test')
    node.wallet.sync_from_date(request_model)
    return True


def check_wallet_stats(node: BaseNode) -> bool:
    request_model = StatsRequest(
        wallet_name='Test',
        account_name='account 0',
        min_confirmations=0,
        verbose=True
    )
    node.wallet.wallet_stats(request_model)
    return True


def check_split_coins(node: BaseNode) -> bool:
    request_model = SplitCoinsRequest(
        wallet_name='Test',
        account_name='account 0',
        wallet_password='password',
        total_amount_to_split=Money(5),
        utxos_count=5
    )
    node.wallet.split_coins(request_model)
    return True


def check_distribute_utxos(node: BaseNode, trxids: List[uint256]) -> bool:
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
        outpoints=[Outpoint(transaction_id=x, index=0) for x in trxids],
        dry_run=True
    )
    node.wallet.distribute_utxos(request_model)
    return True


def check_sweep(node: BaseNode, private_keys: List[str], address: Address) -> bool:
    request_model = SweepRequest(
        private_keys=private_keys,
        destination_address=address,
        broadcast=False
    )
    node.wallet.sweep(request_model)
    return True


def check_build_offline_sign_request(
        node: BaseNode,
        destination_address: Address,
        change_address: Address,
        trxids: List[uint256]) -> bool:
    request_model = BuildOfflineSignRequest(
        fee_amount=Money(10000),
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=x, index=0) for x in trxids],
        recipients=[
            Recipient(
                destination_address=destination_address,
                destination_script=destination_address,
                subtraction_fee_from_amount=True,
                amount=Money(100000)
            )
        ],
        op_return_data='opreturn',
        op_return_amount=Money(1),
        fee_type='low',
        allow_unconfirmed=True,
        shuffle_outputs=True,
        change_address=change_address
    )
    node.wallet.build_offline_sign_request(request_model)
    return True


def check_offline_sign_request(
        node: BaseNode,
        trxids: List[uint256],
        key_path: str,
        addresses: List[Address],
        unsigned_transaction: hexstr) -> bool:
    request_model = OfflineSignRequest(
        wallet_password='password',
        wallet_name='Test',
        wallet_account='account 0',
        unsigned_transaction=unsigned_transaction,
        fee=Money(10000),
        utxos=[UtxoDescriptor(transaction_id=x, index=0, script_pubkey='scriptpubkey', amount=Money(10000000)) for x in trxids],
        addresses=[AddressDescriptor(address=x, key_path=key_path, address_type='p2pkh') for x in addresses]
    )
    node.wallet.offline_sign_request(request_model)
    return True


def check_consolidate(node: BaseNode, destination_address: Address) -> bool:
    request_model = ConsolidateRequest(
        wallet_password='password',
        wallet_name='Test',
        wallet_account='account 0',
        destination_address=destination_address,
        utxo_value_threshold=Money(1),
        broadcast=False
    )
    node.wallet.consolidate(request_model)
    return True
