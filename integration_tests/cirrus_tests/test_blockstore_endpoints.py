import pytest
from typing import Callable
from nodes import BaseNode
from api.blockstore.requestmodels import *
from api.blockstore.responsemodels import *
from pybitcoin.types import uint256, hexstr


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_addressindexer_tip(cirrus_hot_node: BaseNode):
    response = cirrus_hot_node.blockstore.addressindexer_tip()
    assert isinstance(response, AddressIndexerTipModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_block(cirrus_hot_node: BaseNode):
    # Request json output with maximum details.
    block_hash = cirrus_hot_node.consensus.get_best_blockhash()
    request_model = BlockRequest(hash=block_hash, show_transaction_details=True, output_json=True)
    response = cirrus_hot_node.blockstore.block(request_model=request_model)
    assert isinstance(response, BlockModel)

    # Request hex output.
    request_model = BlockRequest(hash=block_hash, show_transaction_details=True, output_json=False)
    response = cirrus_hot_node.blockstore.block(request_model=request_model)
    assert isinstance(response, hexstr)

    # Request a hash that doesn't exist.
    bad_block_hash = uint256('fffdf')
    request_model = BlockRequest(hash=bad_block_hash, show_transaction_details=True, output_json=False)
    response = cirrus_hot_node.blockstore.block(request_model=request_model)
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_block_count(cirrus_hot_node: BaseNode):
    response = cirrus_hot_node.blockstore.get_block_count()
    assert isinstance(response, int)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_addresses_balances(cirrus_hot_node: BaseNode, syncing_node: BaseNode,
                                get_node_address_with_balance: Callable):
    mining_address = get_node_address_with_balance(cirrus_hot_node)
    receiving_address = get_node_address_with_balance(syncing_node)
    addresses = [mining_address, receiving_address]
    request_model = GetAddressesBalancesRequest(addresses=addresses[0])
    response = cirrus_hot_node.blockstore.get_addresses_balances(request_model=request_model)
    assert isinstance(response, GetAddressesBalancesModel)
    assert len(response.balances) == 1
    assert isinstance(response.balances[0], AddressBalanceModel)

    request_model = GetAddressesBalancesRequest(addresses=addresses)
    cirrus_hot_node.blockstore.get_addresses_balances(request_model=request_model)
    assert isinstance(response, GetAddressesBalancesModel)
    for item in response.balances:
        assert isinstance(item, AddressBalanceModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_verbose_addresses_balances(cirrus_hot_node: BaseNode, syncing_node: BaseNode,
                                        get_node_address_with_balance: Callable):
    mining_address = get_node_address_with_balance(cirrus_hot_node)
    receiving_address = get_node_address_with_balance(syncing_node)
    addresses = [mining_address, receiving_address]
    request_model = GetVerboseAddressesBalancesRequest(addresses=addresses[0])
    response = cirrus_hot_node.blockstore.get_verbose_addresses_balances(request_model=request_model)
    assert isinstance(response, GetVerboseAddressesBalancesModel)
    assert len(response.balances_data) == 1
    assert isinstance(response.balances_data[0], VerboseAddressBalanceModel)

    request_model = GetVerboseAddressesBalancesRequest(addresses=addresses)
    response = cirrus_hot_node.blockstore.get_verbose_addresses_balances(request_model=request_model)
    assert isinstance(response, GetVerboseAddressesBalancesModel)
    assert len(response.balances_data) == 2
    for item in response.balances_data:
        assert isinstance(item, VerboseAddressBalanceModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_utxoset(cirrus_hot_node: BaseNode):
    height = cirrus_hot_node.blockstore.get_block_count()
    request_model = GetUTXOSetRequest(at_block_height=height)
    response = cirrus_hot_node.blockstore.get_utxo_set(request_model=request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, UTXOModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_last_balance_update_transaction(cirrus_hot_node: BaseNode, syncing_node: BaseNode,
                                             get_node_address_with_balance: Callable):
    receiving_address = get_node_address_with_balance(syncing_node)
    request_model = GetLastBalanceUpdateTransactionRequest(address=receiving_address)
    response = cirrus_hot_node.blockstore.get_last_balance_update_transaction(request_model=request_model)
    assert isinstance(response, GetLastBalanceUpdateTransactionModel)
