import pytest
from nodes import StraxNode
from api.coldstaking.requestmodels import *
from pybitcoin.types import Money
from api.wallet.requestmodels import ExtPubRecoveryRequest, GetUnusedAddressRequest, \
    ExtPubKeyRequest, SendTransactionRequest, OfflineSignRequest

hot_wallet_name = 'Test'
offline_node_default_wallet_name = 'mywallet'
restored_offline_on_hot_wallet_name = 'coldwallet'


@pytest.fixture(scope='session')
def setup_coldstaking_accounts_and_addresses(
        hot_node: StraxNode,
        offline_node: StraxNode,
        get_node_address_with_balance,
        node_creates_a_wallet,
        send_a_transaction,
        get_datetime,
        node_mines_some_blocks_and_syncs) -> dict:
    mining_address = get_node_address_with_balance(hot_node)
    credentials = {}
    # Setup a wallet on the cold node.
    assert node_creates_a_wallet(offline_node, name=offline_node_default_wallet_name)

    # Get the extpubkey from the cold node so it can be restored on the hot node.
    offline_wallet_default_extpubkey = offline_node.wallet.extpubkey(
        ExtPubKeyRequest(wallet_name=offline_node_default_wallet_name, account_name='account 0')
    )

    # Use the cold extpubkey to load the cold wallet on the online node.
    hot_node.wallet.recover_via_extpubkey(
        ExtPubRecoveryRequest(
            extpubkey=offline_wallet_default_extpubkey,
            name=restored_offline_on_hot_wallet_name,
            account_index=0,
            creation_date=get_datetime(days_back=1)
        )
    )
    # Setup the hot account from the hot node.
    credentials['hot_account'] = hot_node.coldstaking.account(
        AccountRequest(wallet_name=hot_wallet_name, wallet_password='password',
                       is_cold_wallet_account=False)
    )

    # Get the hot address from the hot node.
    credentials['hot_address'] = hot_node.coldstaking.address(
        request_model=AddressRequest(
            wallet_name=hot_wallet_name, is_cold_wallet_address=False
        )
    ).address

    # Get an address on the cold node for staking setup.
    cold_default_address = hot_node.wallet.unused_address(
        GetUnusedAddressRequest(wallet_name=restored_offline_on_hot_wallet_name, account_name='account 0', segwit=False)
    )

    # Fund the cold wallet default address
    assert send_a_transaction(
        node=hot_node, sending_address=mining_address, receiving_address=cold_default_address,
        amount=Money(50)
    )
    assert node_mines_some_blocks_and_syncs(mining_node=hot_node, syncing_node=None, num_blocks_to_mine=15)

    # Set up cold staking account of cold node to get the cold address
    credentials['cold_account'] = offline_node.coldstaking.account(
        AccountRequest(wallet_name=offline_node_default_wallet_name, wallet_password='password',
                       is_cold_wallet_account=True)
    )
    credentials['cold_address'] = offline_node.wallet.unused_address(
        GetUnusedAddressRequest(wallet_name=offline_node_default_wallet_name, account_name='account 0', segwit=True)
    )
    return credentials


@pytest.fixture(scope='session')
def setup_coldstaking_transaction_and_send(
        hot_node: StraxNode, offline_node: StraxNode,
        node_mines_some_blocks_and_syncs,
        setup_coldstaking_accounts_and_addresses) -> True:
    request_model = SetupOfflineRequest(
        wallet_name=hot_wallet_name,
        wallet_account='account 0',
        cold_wallet_address=setup_coldstaking_accounts_and_addresses['cold_address'],
        hot_wallet_address=setup_coldstaking_accounts_and_addresses['hot_address'],
        amount=Money(50),
        fees=Money(0.0002),
        split_count=10
    )
    offline_template = hot_node.coldstaking.setup_offline(request_model=request_model)

    request_model = OfflineSignRequest(
        wallet_password='password',
        wallet_name=offline_node_default_wallet_name,
        wallet_account=offline_template.wallet_account,
        unsigned_transaction=offline_template.unsigned_transaction,
        fee=offline_template.fee,
        utxos=offline_template.utxos,
        addresses=offline_template.addresses
    )
    built_transaction = offline_node.wallet.offline_sign_request(request_model)

    # Send the coldstaking creation transaction and mine some blocks to confirm.
    hot_node.wallet.send_transaction(SendTransactionRequest(hex=built_transaction.hex))
    assert node_mines_some_blocks_and_syncs(mining_node=hot_node, syncing_node=None, num_blocks_to_mine=15)
    return True


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_info(hot_node: StraxNode, offline_node: StraxNode, setup_coldstaking_accounts_and_addresses):
    hot_node.coldstaking.info(request_model=InfoRequest(wallet_name=hot_wallet_name))
    offline_node.coldstaking.info(request_model=InfoRequest(wallet_name=offline_node_default_wallet_name))


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_account(hot_node: StraxNode, setup_coldstaking_accounts_and_addresses):
    hot_node.coldstaking.account(
        AccountRequest(wallet_name=hot_wallet_name, wallet_password='password',
                       is_cold_wallet_account=False)
    )


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_address(hot_node: StraxNode, setup_coldstaking_accounts_and_addresses):
    hot_node.coldstaking.address(
        request_model=AddressRequest(
            wallet_name=hot_wallet_name, is_cold_wallet_address=False
        )
    )


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_estimate_offline_setup_tx_fee(hot_node: StraxNode, setup_coldstaking_accounts_and_addresses):
    request_model = SetupOfflineRequest(
        wallet_name=hot_wallet_name,
        wallet_account='account 0',
        cold_wallet_address=setup_coldstaking_accounts_and_addresses['cold_address'],
        hot_wallet_address=setup_coldstaking_accounts_and_addresses['hot_address'],
        amount=Money(5),
        fees=Money(0.0002),
        split_count=1
    )
    hot_node.coldstaking.estimate_offline_setup_tx_fee(request_model=request_model)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_setup_offline(hot_node: StraxNode, setup_coldstaking_accounts_and_addresses):
    request_model = SetupOfflineRequest(
        wallet_name=hot_wallet_name,
        wallet_account='account 0',
        cold_wallet_address=setup_coldstaking_accounts_and_addresses['cold_address'],
        hot_wallet_address=setup_coldstaking_accounts_and_addresses['hot_address'],
        amount=Money(50),
        fees=Money(0.0002),
        split_count=10
    )
    hot_node.coldstaking.setup_offline(request_model=request_model)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_estimate_setup_tx_fee(hot_node: StraxNode, setup_coldstaking_accounts_and_addresses):
    request_model = SetupRequest(
        wallet_name=hot_wallet_name,
        wallet_account='account 0',
        wallet_password='password',
        cold_wallet_address=setup_coldstaking_accounts_and_addresses['cold_address'],
        hot_wallet_address=setup_coldstaking_accounts_and_addresses['hot_address'],
        amount=Money(5),
        fees=Money(0.0002),
        split_count=1
    )
    hot_node.coldstaking.estimate_setup_tx_fee(request_model=request_model)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_setup(hot_node: StraxNode, setup_coldstaking_accounts_and_addresses):
    request_model = SetupRequest(
        wallet_name=hot_wallet_name,
        wallet_account='account 0',
        wallet_password='password',
        cold_wallet_address=setup_coldstaking_accounts_and_addresses['cold_address'],
        hot_wallet_address=setup_coldstaking_accounts_and_addresses['hot_address'],
        amount=Money(5),
        fees=Money(0.0002),
        split_count=1
    )
    return hot_node.coldstaking.setup(request_model=request_model)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_offline_withdrawal(hot_node: StraxNode,
                            setup_coldstaking_accounts_and_addresses,
                            setup_coldstaking_transaction_and_send,
                            get_node_address_with_balance):
    assert setup_coldstaking_transaction_and_send
    receiving_address = get_node_address_with_balance(hot_node)
    request_model = OfflineWithdrawalRequest(
        wallet_name=hot_wallet_name,
        account_name='account 0',
        receiving_address=receiving_address,
        amount=Money(0.2),
        fees=Money(0.0002),
        subtractFeeFromAmount=True
    )
    hot_node.coldstaking.offline_withdrawal(request_model=request_model)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_withdrawal(
        hot_node: StraxNode,
        get_node_address_with_balance,
        setup_coldstaking_transaction_and_send):
    assert setup_coldstaking_transaction_and_send
    receiving_address = get_node_address_with_balance(hot_node)
    request_model = WithdrawalRequest(
        wallet_name=hot_wallet_name,
        account_name='account 0',
        wallet_password='password',
        receiving_address=receiving_address,
        amount=Money(0.2),
        fees=Money(0.0002),
        subtractFeeFromAmount=True
    )
    hot_node.coldstaking.withdrawal(request_model=request_model)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_estimate_offline_withdrawal_fee(
        hot_node: StraxNode,
        setup_coldstaking_transaction_and_send,
        get_node_address_with_balance):
    assert setup_coldstaking_transaction_and_send
    receiving_address = get_node_address_with_balance(hot_node)
    request_model = OfflineWithdrawalFeeEstimationRequest(
        wallet_name=hot_wallet_name,
        account_name='account 0',
        receiving_address=receiving_address,
        amount=Money(400000000)
    )
    hot_node.coldstaking.estimate_offline_withdrawal_tx_fee(request_model=request_model)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_estimate_withdrawal_fee(
        hot_node: StraxNode,
        setup_coldstaking_transaction_and_send,
        get_node_address_with_balance):
    assert setup_coldstaking_transaction_and_send
    receiving_address = get_node_address_with_balance(hot_node)
    request_model = WithdrawalRequest(
        wallet_name=hot_wallet_name,
        account_name='account 0',
        wallet_password='password',
        receiving_address=receiving_address,
        amount=Money(400000000),
        fees=Money(0.0002)
    )
    hot_node.coldstaking.estimate_withdrawal_tx_fee(request_model=request_model)
