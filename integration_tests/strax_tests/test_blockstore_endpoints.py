import pytest
from nodes import BaseNode
from api.blockstore.requestmodels import *
from api.blockstore.responsemodels import *
from pybitcoin.types import uint256, hexstr


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
    request_model = BlockRequest(hash=block_hash, show_transaction_details=True, output_json=True)
    response = strax_hot_node.blockstore.block(request_model=request_model)
    assert isinstance(response, BlockModel)

    # Request hex output.
    request_model = BlockRequest(hash=block_hash, show_transaction_details=True, output_json=False)
    response = strax_hot_node.blockstore.block(request_model=request_model)
    assert isinstance(response, hexstr)

    # Request a hash that doesn't exist.
    bad_block_hash = uint256('fffdf')
    request_model = BlockRequest(hash=bad_block_hash, show_transaction_details=True, output_json=False)
    response = strax_hot_node.blockstore.block(request_model=request_model)
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
    request_model = GetAddressesBalancesRequest(addresses=addresses[0])
    response = strax_hot_node.blockstore.get_addresses_balances(request_model=request_model)
    assert isinstance(response, GetAddressesBalancesModel)
    assert len(response.balances) == 1
    assert isinstance(response.balances[0], AddressBalanceModel)

    request_model = GetAddressesBalancesRequest(addresses=addresses)
    response = strax_hot_node.blockstore.get_addresses_balances(request_model=request_model)
    assert isinstance(response, GetAddressesBalancesModel)
    for item in response.balances:
        assert isinstance(item, AddressBalanceModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_verbose_addresses_balances(strax_hot_node: BaseNode, strax_syncing_node: BaseNode, get_node_address_with_balance):
    mining_address = get_node_address_with_balance(strax_hot_node)
    receiving_address = get_node_address_with_balance(strax_syncing_node)
    addresses = [mining_address, receiving_address]
    request_model = GetVerboseAddressesBalancesRequest(addresses=addresses[0])
    response = strax_hot_node.blockstore.get_verbose_addresses_balances(request_model=request_model)
    assert isinstance(response, GetVerboseAddressesBalancesModel)
    assert len(response.balances_data) == 1
    assert isinstance(response.balances_data[0], VerboseAddressBalanceModel)

    request_model = GetVerboseAddressesBalancesRequest(addresses=addresses)
    response = strax_hot_node.blockstore.get_verbose_addresses_balances(request_model=request_model)
    assert isinstance(response, GetVerboseAddressesBalancesModel)
    assert len(response.balances_data) == 2
    for item in response.balances_data:
        assert isinstance(item, VerboseAddressBalanceModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_utxoset(strax_hot_node: BaseNode):
    height = strax_hot_node.blockstore.get_block_count()
    request_model = GetUTXOSetRequest(at_block_height=height)
    response = strax_hot_node.blockstore.get_utxo_set(request_model=request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, UTXOModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_last_balance_update_transaction(strax_hot_node: BaseNode, strax_syncing_node: BaseNode, get_node_address_with_balance):
    receiving_address = get_node_address_with_balance(strax_syncing_node)
    request_model = GetLastBalanceUpdateTransactionRequest(address=receiving_address)
    response = strax_hot_node.blockstore.get_last_balance_update_transaction(request_model=request_model)
    assert isinstance(response, GetLastBalanceUpdateTransactionModel)
