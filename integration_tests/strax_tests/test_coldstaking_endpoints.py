import pytest
from nodes import StraxNode
from api.coldstaking.responsemodels import *
from pybitcoin.types import Money, Address, hexstr


@pytest.fixture(scope='module')
def hot_wallet_name() -> str:
    return 'Test'


@pytest.fixture(scope='module')
def offline_node_default_wallet_name() -> str:
    return 'mywallet'


@pytest.fixture(scope='module')
def restored_offline_on_hot_wallet_name() -> str:
    return 'coldwallet'


@pytest.fixture(scope='module')
def setup_coldstaking_accounts_and_addresses(
        strax_hot_node: StraxNode,
        strax_offline_node: StraxNode,
        hot_wallet_name,
        offline_node_default_wallet_name,
        restored_offline_on_hot_wallet_name,
        get_node_address_with_balance,
        node_creates_a_wallet,
        send_a_transaction,
        get_datetime,
        node_mines_some_blocks_and_syncs) -> dict:
    mining_address = get_node_address_with_balance(strax_hot_node)
    credentials = {}
    # Setup a wallet on the cold node.
    assert node_creates_a_wallet(strax_offline_node, wallet_name=offline_node_default_wallet_name)

    # Get the extpubkey from the cold node so it can be restored on the hot node.
    offline_wallet_default_extpubkey = strax_offline_node.wallet.extpubkey(
        ExtPubKeyRequest(wallet_name=offline_node_default_wallet_name, account_name='account 0')
    )
    credentials['offline_wallet_default_extpubkey'] = offline_wallet_default_extpubkey

    # Use the cold extpubkey to load the cold wallet on the online node.
    strax_hot_node.wallet.recover_via_extpubkey(
        ExtPubRecoveryRequest(
            extpubkey=offline_wallet_default_extpubkey,
            name=restored_offline_on_hot_wallet_name,
            account_index=0,
            creation_date=get_datetime(days_back=1)
        )
    )
    # Setup the hot account from the hot node.
    credentials['hot_account'] = strax_hot_node.coldstaking.account(
        wallet_name=hot_wallet_name,
        wallet_password='password',
        is_cold_wallet_account=False
    )

    # Get the hot address from the hot node.
    credentials['hot_address'] = strax_hot_node.coldstaking.address(
        wallet_name=hot_wallet_name,
        is_cold_wallet_address=False,
        segwit=False
    ).address

    # Get an address on the cold node for staking setup.
    cold_default_address = strax_hot_node.wallet.unused_address(
        wallet_name=restored_offline_on_hot_wallet_name,
        account_name='account 0',
        segwit=False
    )
    credentials['cold_default_address'] = cold_default_address

    # Fund the cold wallet default address
    assert send_a_transaction(
        node=strax_hot_node,
        sending_address=mining_address,
        receiving_address=cold_default_address,
        amount_to_send=Money(200)
    )
    assert node_mines_some_blocks_and_syncs(mining_node=strax_hot_node, syncing_node=None, num_blocks_to_mine=15)

    # Set up cold staking account of cold node to get the cold address
    credentials['cold_account'] = strax_offline_node.coldstaking.account(
        wallet_name=offline_node_default_wallet_name,
        wallet_password='password',
        is_cold_wallet_account=True
    )
    credentials['cold_address'] = strax_offline_node.coldstaking.address(
        wallet_name=offline_node_default_wallet_name,
        is_cold_wallet_address=True,
        segwit=False
    ).address
    return credentials


@pytest.fixture(scope='module')
def setup_coldstaking_transaction_and_send(
        strax_hot_node: StraxNode, strax_offline_node: StraxNode,
        node_mines_some_blocks_and_syncs,
        restored_offline_on_hot_wallet_name,
        offline_node_default_wallet_name,
        setup_coldstaking_accounts_and_addresses) -> True:
    offline_template = strax_hot_node.coldstaking.setup_offline(
        wallet_name=restored_offline_on_hot_wallet_name,
        wallet_account='account 0',
        cold_wallet_address=setup_coldstaking_accounts_and_addresses['cold_address'],
        hot_wallet_address=setup_coldstaking_accounts_and_addresses['hot_address'],
        amount=Money(10),
        fees=Money(0.0002),
        split_count=10
    )

    built_transaction = strax_offline_node.wallet.offline_sign_request(
        wallet_password='password',
        wallet_name=offline_node_default_wallet_name,
        wallet_account=offline_template.wallet_account,
        unsigned_transaction=offline_template.unsigned_transaction,
        fee=offline_template.fee,
        utxos=offline_template.utxos,
        addresses=offline_template.addresses
    )

    # Send the coldstaking creation transaction and mine some blocks to confirm.
    strax_hot_node.wallet.send_transaction(hex=built_transaction.hex)
    assert node_mines_some_blocks_and_syncs(mining_node=strax_hot_node, syncing_node=None, num_blocks_to_mine=15)
    return True


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_info(strax_hot_node: StraxNode, strax_offline_node: StraxNode, setup_coldstaking_accounts_and_addresses,
              hot_wallet_name, offline_node_default_wallet_name):
    response = strax_hot_node.coldstaking.info(wallet_name=hot_wallet_name)
    assert isinstance(response, InfoModel)

    response = strax_offline_node.coldstaking.info(wallet_name=offline_node_default_wallet_name)
    assert isinstance(response, InfoModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_account(strax_hot_node: StraxNode, setup_coldstaking_accounts_and_addresses, hot_wallet_name):
    response = strax_hot_node.coldstaking.account(
        wallet_name=hot_wallet_name,
        wallet_password='password',
        is_cold_wallet_account=False
    )
    assert isinstance(response, AccountModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_address(strax_hot_node: StraxNode, setup_coldstaking_accounts_and_addresses, hot_wallet_name):
    response = strax_hot_node.coldstaking.address(wallet_name=hot_wallet_name, is_cold_wallet_address=False)
    assert isinstance(response, AddressModel)
    assert isinstance(response.address, Address)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_estimate_offline_setup_tx_fee(strax_hot_node: StraxNode, setup_coldstaking_accounts_and_addresses, restored_offline_on_hot_wallet_name):
    response = strax_hot_node.coldstaking.estimate_offline_setup_tx_fee(
        wallet_name=restored_offline_on_hot_wallet_name,
        wallet_account='account 0',
        cold_wallet_address=setup_coldstaking_accounts_and_addresses['cold_address'],
        hot_wallet_address=setup_coldstaking_accounts_and_addresses['hot_address'],
        amount=Money(5),
        fees=Money(0.0002),
        split_count=1
    )
    assert isinstance(response, Money)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_setup_offline(strax_hot_node: StraxNode, setup_coldstaking_accounts_and_addresses, restored_offline_on_hot_wallet_name):
    response = strax_hot_node.coldstaking.setup_offline(
        wallet_name=restored_offline_on_hot_wallet_name,
        wallet_account='account 0',
        cold_wallet_address=setup_coldstaking_accounts_and_addresses['cold_address'],
        hot_wallet_address=setup_coldstaking_accounts_and_addresses['hot_address'],
        amount=Money(5),
        fees=Money(0.0002),
        split_count=10
    )
    assert isinstance(response, BuildOfflineSignModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_estimate_setup_tx_fee(strax_hot_node: StraxNode, setup_coldstaking_accounts_and_addresses, hot_wallet_name):
    response = strax_hot_node.coldstaking.estimate_setup_tx_fee(
        wallet_name=hot_wallet_name,
        wallet_account='account 0',
        wallet_password='password',
        cold_wallet_address=setup_coldstaking_accounts_and_addresses['cold_address'],
        hot_wallet_address=setup_coldstaking_accounts_and_addresses['hot_address'],
        amount=Money(5),
        fees=Money(0.0002),
        split_count=1
    )
    assert isinstance(response, Money)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_setup(strax_hot_node: StraxNode, setup_coldstaking_accounts_and_addresses, hot_wallet_name):
    response = strax_hot_node.coldstaking.setup(
        wallet_name=hot_wallet_name,
        wallet_account='account 0',
        wallet_password='password',
        cold_wallet_address=setup_coldstaking_accounts_and_addresses['cold_address'],
        hot_wallet_address=setup_coldstaking_accounts_and_addresses['hot_address'],
        amount=Money(5),
        fees=Money(0.0002),
        split_count=1
    )
    assert isinstance(response, SetupModel)
    assert isinstance(response.transaction_hex, hexstr)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_offline_withdrawal(strax_hot_node: StraxNode,
                            setup_coldstaking_accounts_and_addresses,
                            setup_coldstaking_transaction_and_send,
                            hot_wallet_name,
                            get_node_address_with_balance):
    assert setup_coldstaking_transaction_and_send
    receiving_address = get_node_address_with_balance(strax_hot_node)
    response = strax_hot_node.coldstaking.offline_withdrawal(
        wallet_name=hot_wallet_name,
        account_name='account 0',
        receiving_address=receiving_address,
        amount=Money(0.2),
        fees=Money(0.0002),
        subtractFeeFromAmount=True
    )
    assert isinstance(response, BuildOfflineSignModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_withdrawal(
        strax_hot_node: StraxNode,
        strax_offline_node: StraxNode,
        connect_two_nodes,
        sync_two_nodes,
        get_node_address_with_balance,
        offline_node_default_wallet_name,
        setup_coldstaking_accounts_and_addresses,
        setup_coldstaking_transaction_and_send):
    # Normally would keep the offline node offline, but need to have it sync to find the transactions here to test this endpoint.
    assert connect_two_nodes(strax_hot_node, strax_offline_node)
    assert sync_two_nodes(strax_hot_node, strax_offline_node)
    assert setup_coldstaking_transaction_and_send
    receiving_address = get_node_address_with_balance(strax_hot_node)
    response = strax_offline_node.coldstaking.withdrawal(
        wallet_name=offline_node_default_wallet_name,
        account_name=setup_coldstaking_accounts_and_addresses['cold_account'].account_name,
        wallet_password='password',
        receiving_address=receiving_address,
        amount=Money(0.2),
        fees=Money(0.0002),
        subtractFeeFromAmount=True
    )
    assert isinstance(response, WithdrawalModel)
    assert isinstance(response.transaction_hex, hexstr)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_estimate_offline_withdrawal_fee(
        strax_hot_node: StraxNode,
        strax_offline_node: StraxNode,
        setup_coldstaking_accounts_and_addresses,
        setup_coldstaking_transaction_and_send,
        connect_two_nodes,
        sync_two_nodes,
        offline_node_default_wallet_name,
        get_node_address_with_balance):
    # Normally would keep the offline node offline, but need to have it sync to find the transactions here to test this endpoint.
    assert connect_two_nodes(strax_hot_node, strax_offline_node)
    assert sync_two_nodes(strax_hot_node, strax_offline_node)
    assert setup_coldstaking_transaction_and_send
    receiving_address = get_node_address_with_balance(strax_hot_node)
    response = strax_offline_node.coldstaking.estimate_offline_withdrawal_tx_fee(
        wallet_name=offline_node_default_wallet_name,
        account_name=setup_coldstaking_accounts_and_addresses['cold_account'].account_name,
        receiving_address=receiving_address,
        amount=Money(4)
    )
    assert isinstance(response, Money)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_estimate_withdrawal_fee(
        strax_hot_node: StraxNode,
        strax_offline_node: StraxNode,
        connect_two_nodes,
        sync_two_nodes,
        offline_node_default_wallet_name,
        setup_coldstaking_accounts_and_addresses,
        setup_coldstaking_transaction_and_send,
        get_node_address_with_balance):
    # Normally would keep the offline node offline, but need to have it sync to find the transactions here to test this endpoint.
    assert connect_two_nodes(strax_hot_node, strax_offline_node)
    assert sync_two_nodes(strax_hot_node, strax_offline_node)
    assert setup_coldstaking_transaction_and_send
    receiving_address = get_node_address_with_balance(strax_hot_node)

    response = strax_offline_node.coldstaking.estimate_withdrawal_tx_fee(
        wallet_name=offline_node_default_wallet_name,
        account_name=setup_coldstaking_accounts_and_addresses['cold_account'].account_name,
        wallet_password='password',
        receiving_address=receiving_address,
        amount=Money(4),
        fees=Money(0.0002)
    )
    assert isinstance(response, Money)
