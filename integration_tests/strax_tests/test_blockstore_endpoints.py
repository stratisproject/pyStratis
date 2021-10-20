import pytest
from pystratis.nodes import BaseNode
from pystratis.core.types import uint256, hexstr
from pystratis.api.blockstore.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_addressindexer_tip(strax_hot_node: BaseNode):
    response = strax_hot_node.blockstore.addressindexer_tip()
    assert isinstance(response, AddressIndexerTipModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_block(strax_hot_node: BaseNode):
    # Request json output with maximum details.
    block_hash = strax_hot_node.consensus.get_best_blockhash()
    response = strax_hot_node.blockstore.block(block_hash=block_hash, show_transaction_details=True, output_json=True)
    assert isinstance(response, BlockModel)

    # Request hex output.
    response = strax_hot_node.blockstore.block(block_hash=block_hash, show_transaction_details=True, output_json=False)
    assert isinstance(response, hexstr)

    # Request a hash that doesn't exist.
    bad_block_hash = uint256('fffdf')
    response = strax_hot_node.blockstore.block(block_hash=bad_block_hash, show_transaction_details=True, output_json=False)
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_block_count(strax_hot_node: BaseNode):
    response = strax_hot_node.blockstore.get_block_count()
    assert isinstance(response, int)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_addresses_balances(strax_hot_node: BaseNode, strax_syncing_node: BaseNode, get_node_address_with_balance):
    mining_address = get_node_address_with_balance(strax_hot_node)
    receiving_address = get_node_address_with_balance(strax_syncing_node)
    addresses = [mining_address, receiving_address]
    response = strax_hot_node.blockstore.get_addresses_balances(addresses=addresses[0])
    assert isinstance(response, GetAddressesBalancesModel)
    assert len(response.balances) == 1
    assert isinstance(response.balances[0], AddressBalanceModel)

    response = strax_hot_node.blockstore.get_addresses_balances(addresses=addresses)
    assert isinstance(response, GetAddressesBalancesModel)
    for item in response.balances:
        assert isinstance(item, AddressBalanceModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_verbose_addresses_balances(strax_hot_node: BaseNode, strax_syncing_node: BaseNode, get_node_address_with_balance):
    mining_address = get_node_address_with_balance(strax_hot_node)
    receiving_address = get_node_address_with_balance(strax_syncing_node)
    addresses = [mining_address, receiving_address]
    response = strax_hot_node.blockstore.get_verbose_addresses_balances(addresses=addresses[0])
    assert isinstance(response, GetVerboseAddressesBalancesModel)
    assert len(response.balances_data) == 1
    assert isinstance(response.balances_data[0], VerboseAddressBalanceModel)

    response = strax_hot_node.blockstore.get_verbose_addresses_balances(addresses=addresses)
    assert isinstance(response, GetVerboseAddressesBalancesModel)
    assert len(response.balances_data) == 2
    for item in response.balances_data:
        assert isinstance(item, VerboseAddressBalanceModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_utxoset(strax_hot_node: BaseNode):
    height = strax_hot_node.blockstore.get_block_count()
    response = strax_hot_node.blockstore.get_utxo_set(at_block_height=height)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, UTXOModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_last_balance_update_transaction(strax_hot_node: BaseNode, strax_syncing_node: BaseNode, get_node_address_with_balance):
    receiving_address = get_node_address_with_balance(strax_syncing_node)
    response = strax_hot_node.blockstore.get_last_balance_update_transaction(address=receiving_address)
    assert isinstance(response, GetLastBalanceUpdateTransactionModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_utxoset_for_address(strax_hot_node: BaseNode, strax_syncing_node: BaseNode, get_node_address_with_balance):
    receiving_address = get_node_address_with_balance(strax_syncing_node)
    response = strax_hot_node.blockstore.get_utxoset_for_address(address=receiving_address)
    assert isinstance(response, GetUTXOsForAddressModel)
