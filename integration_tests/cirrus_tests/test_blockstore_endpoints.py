import pytest
from nodes import CirrusMinerNode
from api.blockstore.responsemodels import *
from pybitcoin.types import uint256, hexstr


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_addressindexer_tip(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.blockstore.addressindexer_tip()
    assert isinstance(response, AddressIndexerTipModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_block(cirrusminer_node: CirrusMinerNode):
    # Request json output with maximum details.
    block_hash = cirrusminer_node.consensus.get_best_blockhash()
    response = cirrusminer_node.blockstore.block(block_hash=block_hash, show_transaction_details=True, output_json=True)
    assert isinstance(response, BlockModel)

    # Request hex output.
    response = cirrusminer_node.blockstore.block(block_hash=block_hash, show_transaction_details=True, output_json=False)
    assert isinstance(response, hexstr)

    # Request a hash that doesn't exist.
    bad_block_hash = uint256('fffdf')
    response = cirrusminer_node.blockstore.block(block_hash=bad_block_hash, show_transaction_details=True, output_json=False)
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_block_count(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.blockstore.get_block_count()
    assert isinstance(response, int)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_addresses_balances(cirrusminer_node: CirrusMinerNode,
                                cirrusminer_syncing_node: CirrusMinerNode,
                                get_node_address_with_balance):
    mining_address = get_node_address_with_balance(cirrusminer_node)
    receiving_address = get_node_address_with_balance(cirrusminer_syncing_node)
    addresses = [mining_address, receiving_address]
    response = cirrusminer_node.blockstore.get_addresses_balances(addresses=addresses[0])
    assert isinstance(response, GetAddressesBalancesModel)
    assert len(response.balances) == 1
    assert isinstance(response.balances[0], AddressBalanceModel)

    response = cirrusminer_node.blockstore.get_addresses_balances(addresses=addresses)
    assert isinstance(response, GetAddressesBalancesModel)
    for item in response.balances:
        assert isinstance(item, AddressBalanceModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_verbose_addresses_balances(cirrusminer_node: CirrusMinerNode,
                                        cirrusminer_syncing_node: CirrusMinerNode,
                                        get_node_address_with_balance):
    mining_address = get_node_address_with_balance(cirrusminer_node)
    receiving_address = get_node_address_with_balance(cirrusminer_syncing_node)
    addresses = [mining_address, receiving_address]
    response = cirrusminer_node.blockstore.get_verbose_addresses_balances(addresses=addresses[0])
    assert isinstance(response, GetVerboseAddressesBalancesModel)
    assert len(response.balances_data) == 1
    assert isinstance(response.balances_data[0], VerboseAddressBalanceModel)

    response = cirrusminer_node.blockstore.get_verbose_addresses_balances(addresses=addresses)
    assert isinstance(response, GetVerboseAddressesBalancesModel)
    assert len(response.balances_data) == 2
    for item in response.balances_data:
        assert isinstance(item, VerboseAddressBalanceModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_utxoset(cirrusminer_node: CirrusMinerNode):
    height = cirrusminer_node.blockstore.get_block_count()
    response = cirrusminer_node.blockstore.get_utxo_set(at_block_height=height)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, UTXOModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_last_balance_update_transaction(
        cirrusminer_node: CirrusMinerNode,
        cirrusminer_syncing_node: CirrusMinerNode,
        get_node_address_with_balance):
    # Check address on both nodes
    receiving_address = get_node_address_with_balance(cirrusminer_syncing_node)
    response = cirrusminer_node.blockstore.get_last_balance_update_transaction(address=receiving_address)
    if response is not None:
        assert isinstance(response, GetLastBalanceUpdateTransactionModel)
    response = cirrusminer_syncing_node.blockstore.get_last_balance_update_transaction(address=receiving_address)
    if response is not None:
        assert isinstance(response, GetLastBalanceUpdateTransactionModel)

    receiving_address = get_node_address_with_balance(cirrusminer_node)
    response = cirrusminer_node.blockstore.get_last_balance_update_transaction(address=receiving_address)
    if response is not None:
        assert isinstance(response, GetLastBalanceUpdateTransactionModel)
    response = cirrusminer_syncing_node.blockstore.get_last_balance_update_transaction(address=receiving_address)
    if response is not None:
        assert isinstance(response, GetLastBalanceUpdateTransactionModel)
