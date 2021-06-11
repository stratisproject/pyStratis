from typing import Callable, Union, Tuple
from nodes import StraxNode, InterfluxStraxNode
from api.coldstaking.requestmodels import *
from api.coldstaking.responsemodels import *
from pybitcoin.types import Address, Money
from api.wallet.requestmodels import ExtPubRecoveryRequest, GetUnusedAddressRequest, \
    ExtPubKeyRequest, SendTransactionRequest, OfflineSignRequest
import pdb


def check_coldstaking_endpoints(
        hot_node: Union[StraxNode, InterfluxStraxNode],
        cold_node: Union[StraxNode, InterfluxStraxNode],
        mining_address: Address,
        node_creates_a_wallet: Callable,
        send_a_transaction: Callable,
        get_datetime: Callable,
        node_mines_some_blocks_and_syncs: Callable) -> None:
    hot_wallet_name = 'Test'
    cold_node_default_wallet_name = 'mywallet'
    restored_cold_on_hot_wallet_name = 'coldwallet'

    # Set up the coldstaking accounts and addresses on both the online and offline nodes.
    cold_address, hot_address, cold_account, hot_account = get_coldstaking_addresses_and_accounts(
        cold_node=cold_node, hot_node=hot_node, mining_address=mining_address, node_creates_a_wallet=node_creates_a_wallet,
        send_a_transaction=send_a_transaction, node_mines_some_blocks_and_syncs=node_mines_some_blocks_and_syncs,
        hot_wallet_name=hot_wallet_name, cold_node_default_wallet_name=cold_node_default_wallet_name,
        restored_cold_on_hot_wallet_name=restored_cold_on_hot_wallet_name, get_datetime=get_datetime
    )
    assert check_info(
        cold_node=cold_node, hot_node=hot_node, hot_wallet_name=hot_wallet_name,
        cold_wallet_name=cold_node_default_wallet_name
    )

    # Running to validate responses and throwing them away.
    check_estimate_offline_setup_tx_fee(
        hot_node=hot_node, wallet_name=hot_wallet_name,
        cold_address=cold_address, hot_address=hot_address
    )
    check_estimate_setup_tx_fee(
        hot_node=hot_node, wallet_name=hot_wallet_name,
        cold_address=cold_address, hot_address=hot_address
    )
    check_setup(
        hot_node=hot_node, wallet_name=hot_wallet_name,
        cold_address=cold_address, hot_address=hot_address
    )
    # Actually setting up the coldstaking here.
    # First, create a template on the hot node, send to cold node for signing, and broadcast back on hot node.
    offline_template = check_setup_offline(
        hot_node=hot_node, wallet_name=restored_cold_on_hot_wallet_name,
        cold_address=cold_address, hot_address=hot_address
    )
    request_model = OfflineSignRequest(
        wallet_password='password',
        wallet_name=cold_node_default_wallet_name,
        wallet_account=offline_template.wallet_account,
        unsigned_transaction=offline_template.unsigned_transaction,
        fee=offline_template.fee,
        utxos=offline_template.utxos,
        addresses=offline_template.addresses
    )
    pdb.set_trace()
    built_transaction = cold_node.wallet.offline_sign_request(request_model)

    # Send the coldstaking creation transaction and mine some blocks to confirm.
    hot_node.wallet.send_transaction(SendTransactionRequest(hex=built_transaction.hex))
    assert node_mines_some_blocks_and_syncs(mining_node=hot_node, syncing_node=None, num_blocks_to_mine=15)

    # Running to validate responses and throwing them away.
    check_estimate_offline_withdrawal_fee(
        hot_node=hot_node, wallet_name=hot_wallet_name, account_name=hot_account.account_name, receiving_address=mining_address
    )
    check_estimate_withdrawal_fee(
        hot_node=hot_node, wallet_name=hot_wallet_name, account_name=hot_account.account_name, receiving_address=mining_address
    )
    check_withdrawal(
        hot_node=hot_node, wallet_name=hot_wallet_name, account_name=hot_account.account_name, receiving_address=mining_address
    )
    # Building the withdrawal transaction template on the hot node
    build_offline_sign_model = check_offline_withdrawal(
        hot_node=hot_node, wallet_name=hot_wallet_name, account_name=hot_account.account_name,
        receiving_address=mining_address
    )
    request_model = OfflineSignRequest(
        wallet_password='password',
        wallet_name=cold_node_default_wallet_name,
        wallet_account='coldStakingColdAddresses',
        unsigned_transaction=build_offline_sign_model.unsigned_transaction,
        fee=build_offline_sign_model.fee,
        utxos=build_offline_sign_model.utxos,
        addresses=build_offline_sign_model.addresses
    )
    built_transaction = cold_node.wallet.offline_sign_request(request_model)

    # Send the transaction and mine some blocks to confirm.
    hot_node.wallet.send_transaction(SendTransactionRequest(hex=built_transaction.hex))
    assert node_mines_some_blocks_and_syncs(mining_node=hot_node, syncing_node=None, num_blocks_to_mine=15)


def get_coldstaking_addresses_and_accounts(
        cold_node: Union[StraxNode, InterfluxStraxNode],
        hot_node: Union[StraxNode, InterfluxStraxNode],
        mining_address: Address,
        hot_wallet_name: str,
        cold_node_default_wallet_name: str,
        restored_cold_on_hot_wallet_name: str,
        node_creates_a_wallet: Callable,
        send_a_transaction: Callable,
        get_datetime: Callable,
        node_mines_some_blocks_and_syncs: Callable) -> Tuple[Address, Address, AccountModel, AccountModel]:
    # Setup a wallet on the cold node.
    assert node_creates_a_wallet(cold_node, name=cold_node_default_wallet_name)

    # Get the extpubkey from the cold node so it can be restored on the hot node.
    cold_wallet_default_extpubkey = cold_node.wallet.extpubkey(
        ExtPubKeyRequest(wallet_name=cold_node_default_wallet_name, account_name='account 0')
    )

    # Use the cold extpubkey to load the cold wallet on the online node.
    hot_node.wallet.recover_via_extpubkey(
        ExtPubRecoveryRequest(
            extpubkey=cold_wallet_default_extpubkey,
            name=restored_cold_on_hot_wallet_name,
            account_index=0,
            creation_date=get_datetime(days_back=1)
        )
    )
    # Setup the hot account from the hot node.
    hot_account = check_account(hot_node, hot_wallet_name, False)

    # Get the hot address from the hot node.
    hot_address = check_address(hot_node, hot_wallet_name, False)

    # Get an address on the cold node for staking setup.
    cold_default_address = hot_node.wallet.unused_address(
        GetUnusedAddressRequest(wallet_name=restored_cold_on_hot_wallet_name, account_name='account 0', segwit=False)
    )

    # Fund the cold wallet default address
    assert send_a_transaction(
        node=hot_node, sending_address=mining_address, receiving_address=cold_default_address,
        amount=Money(5000000000)
    )
    assert node_mines_some_blocks_and_syncs(mining_node=hot_node, syncing_node=None, num_blocks_to_mine=15)

    # Set up cold staking account of cold node to get the cold address
    cold_account = check_account(cold_node, cold_node_default_wallet_name, True)
    cold_address = check_address(cold_node, cold_node_default_wallet_name, True)
    return cold_address, hot_address, cold_account, hot_account


def check_info(cold_node: Union[StraxNode, InterfluxStraxNode],
               hot_node: Union[StraxNode, InterfluxStraxNode],
               cold_wallet_name: str, hot_wallet_name: str) -> bool:
    hot_node.coldstaking.info(request_model=InfoRequest(wallet_name=hot_wallet_name))
    cold_node.coldstaking.info(request_model=InfoRequest(wallet_name=cold_wallet_name))
    return True


def check_account(
        node: Union[StraxNode, InterfluxStraxNode],
        wallet_name: str,
        is_cold_wallet_account: bool) -> AccountModel:
    return node.coldstaking.account(
        AccountRequest(wallet_name=wallet_name, wallet_password='password',
                       is_cold_wallet_account=is_cold_wallet_account)
    )


def check_address(
        node: Union[StraxNode, InterfluxStraxNode],
        wallet_name: str,
        is_cold_wallet_address: bool) -> Address:
    return node.coldstaking.address(
        request_model=AddressRequest(
            wallet_name=wallet_name, is_cold_wallet_address=is_cold_wallet_address
        )
    ).address


def check_estimate_offline_setup_tx_fee(
        hot_node: Union[StraxNode, InterfluxStraxNode],
        wallet_name: str,
        cold_address: Address,
        hot_address: Address) -> Money:
    request_model = SetupOfflineRequest(
        wallet_name=wallet_name,
        wallet_account='account 0',
        cold_wallet_address=cold_address,
        hot_wallet_address=hot_address,
        amount=Money(500000000),
        fees=Money(20000),
        split_count=1
    )
    return hot_node.coldstaking.estimate_offline_setup_tx_fee(request_model=request_model)


def check_setup_offline(
        hot_node: Union[StraxNode, InterfluxStraxNode],
        cold_address: Address,
        hot_address: Address,
        wallet_name: str,
        fees: Money = Money(20000)) -> BuildOfflineSignModel:
    request_model = SetupOfflineRequest(
        wallet_name=wallet_name,
        wallet_account='account 0',
        cold_wallet_address=cold_address,
        hot_wallet_address=hot_address,
        amount=Money(5000000000),
        fees=fees,
        split_count=10
    )
    return hot_node.coldstaking.setup_offline(request_model=request_model)


def check_estimate_setup_tx_fee(
        hot_node: Union[StraxNode, InterfluxStraxNode],
        wallet_name: str,
        cold_address: Address,
        hot_address: Address) -> Money:
    request_model = SetupRequest(
        wallet_name=wallet_name,
        wallet_account='account 0',
        wallet_password='password',
        cold_wallet_address=cold_address,
        hot_wallet_address=hot_address,
        amount=Money(500000000),
        fees=Money(20000),
        split_count=1
    )
    return hot_node.coldstaking.estimate_setup_tx_fee(request_model=request_model)


def check_setup(
        hot_node: Union[StraxNode, InterfluxStraxNode],
        wallet_name: str,
        cold_address: Address,
        hot_address: Address,
        fees: Money = Money(20000)) -> SetupModel:
    request_model = SetupRequest(
        wallet_name=wallet_name,
        wallet_account='account 0',
        wallet_password='password',
        cold_wallet_address=cold_address,
        hot_wallet_address=hot_address,
        amount=Money(500000000),
        fees=fees,
        split_count=1
    )
    return hot_node.coldstaking.setup(request_model=request_model)


def check_offline_withdrawal(
        hot_node: Union[StraxNode, InterfluxStraxNode],
        wallet_name: str,
        account_name: str,
        receiving_address: Address) -> BuildOfflineSignModel:
    request_model = OfflineWithdrawalRequest(
        wallet_name=wallet_name,
        account_name=account_name,
        receiving_address=receiving_address,
        amount=Money(20000000),
        fees=Money(20000),
        subtractFeeFromAmount=True
    )
    pdb.set_trace()
    return hot_node.coldstaking.offline_withdrawal(request_model=request_model)


def check_withdrawal(
        hot_node: Union[StraxNode, InterfluxStraxNode],
        wallet_name: str,
        account_name: str,
        receiving_address: Address) -> WithdrawalModel:
    request_model = WithdrawalRequest(
        wallet_name=wallet_name,
        account_name=account_name,
        wallet_password='password',
        receiving_address=receiving_address,
        amount=Money(20000000),
        fees=Money(20000),
        subtractFeeFromAmount=True
    )
    pdb.set_trace()
    return hot_node.coldstaking.withdrawal(request_model=request_model)


def check_estimate_offline_withdrawal_fee(
        hot_node: Union[StraxNode, InterfluxStraxNode],
        wallet_name: str,
        account_name: str,
        receiving_address: Address) -> Money:
    request_model = OfflineWithdrawalFeeEstimationRequest(
        wallet_name=wallet_name,
        account_name=account_name,
        receiving_address=receiving_address,
        amount=Money(400000000)
    )
    pdb.set_trace()
    return hot_node.coldstaking.estimate_offline_withdrawal_tx_fee(request_model=request_model)


def check_estimate_withdrawal_fee(
        hot_node: Union[StraxNode, InterfluxStraxNode],
        wallet_name: str,
        account_name: str,
        receiving_address: Address, fees: Money = Money(20000)) -> Money:
    request_model = WithdrawalRequest(
        wallet_name=wallet_name,
        account_name=account_name,
        wallet_password='password',
        receiving_address=receiving_address,
        amount=Money(400000000),
        fees=fees
    )
    pdb.set_trace()
    return hot_node.coldstaking.estimate_withdrawal_tx_fee(request_model=request_model)
