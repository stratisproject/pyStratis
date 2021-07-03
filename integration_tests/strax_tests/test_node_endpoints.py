import pytest
from pystratis.nodes import BaseNode
from pystratis.api import LogRule
from pystratis.core.types import uint256, hexstr, Money
from pystratis.api.node.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_status(strax_hot_node: BaseNode):
    response = strax_hot_node.node.status()
    assert isinstance(response, StatusModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_blockheader(strax_hot_node: BaseNode):
    block_hash = strax_hot_node.consensus.get_best_blockhash()
    response = strax_hot_node.node.get_blockheader(block_hash=block_hash, is_json_format=True)
    assert isinstance(response, BlockHeaderModel)
    if response.previous_blockhash is not None:
        assert isinstance(response.previous_blockhash, uint256)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_raw_transaction(strax_hot_node: BaseNode):
    spendable_transactions = strax_hot_node.wallet.spendable_transactions(
        wallet_name='Test', account_name='account 0', min_confirmations=2
    )
    spendable_transactions = [x for x in spendable_transactions.transactions]
    for spendable_transaction in spendable_transactions:
        response = strax_hot_node.node.get_raw_transaction(trxid=spendable_transaction.transaction_id, verbose=True)
        assert isinstance(response, TransactionModel)

        response = strax_hot_node.node.get_raw_transaction(trxid=spendable_transaction.transaction_id, verbose=False)
        assert isinstance(response, hexstr)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_decode_raw_transaction(strax_hot_node: BaseNode):
    spendable_transactions = strax_hot_node.wallet.spendable_transactions(
        wallet_name='Test', account_name='account 0', min_confirmations=2
    )
    spendable_transactions = [x for x in spendable_transactions.transactions]
    for spendable_transaction in spendable_transactions:
        raw_transaction = strax_hot_node.node.get_raw_transaction(trxid=spendable_transaction.transaction_id, verbose=False)
        response = strax_hot_node.node.decode_raw_transaction(raw_hex=raw_transaction)
        assert isinstance(response, TransactionModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_validate_address(strax_hot_node: BaseNode, generate_p2pkh_address):
    address = generate_p2pkh_address(network=strax_hot_node.blockchainnetwork)
    response = strax_hot_node.node.validate_address(address=address)
    assert isinstance(response, ValidateAddressModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_txout(strax_hot_node: BaseNode):
    spendable_transactions = strax_hot_node.wallet.spendable_transactions(
        wallet_name='Test', account_name='account 0', min_confirmations=2
    )
    spendable_transactions = [x for x in spendable_transactions.transactions]
    for spendable_transaction in spendable_transactions:
        response = strax_hot_node.node.get_txout(
            trxid=spendable_transaction.transaction_id, vout=spendable_transaction.index, include_mempool=False
        )
        assert isinstance(response, GetTxOutModel)
        assert isinstance(response.best_block, uint256)
        assert isinstance(response.value, Money)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_txout_proof(strax_hot_node: BaseNode):
    spendable_transactions = strax_hot_node.wallet.spendable_transactions(wallet_name='Test', account_name='account 0', min_confirmations=2)
    spendable_transactions = [x for x in spendable_transactions.transactions]
    for spendable_transaction in spendable_transactions:
        raw_transaction = strax_hot_node.node.get_raw_transaction(trxid=spendable_transaction.transaction_id, verbose=True)
        response = strax_hot_node.node.get_txout_proof(
            txids=[spendable_transaction.transaction_id], block_hash=raw_transaction.blockhash
        )
        assert isinstance(response, hexstr)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_shutdown():
    # Used at the end of the integration tests
    pass


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_stop():
    # Used at the end of the integration tests
    pass


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_log_levels(strax_hot_node: BaseNode):
    strax_hot_node.node.log_levels(log_rules=[LogRule(rule_name='Stratis.*', log_level='Debug', filename='filename')])


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_log_rules(strax_hot_node: BaseNode):
    response = strax_hot_node.node.log_rules()
    assert isinstance(response, list)
    for logrule in response:
        assert isinstance(logrule, LogRulesModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_async_loops(strax_hot_node: BaseNode):
    response = strax_hot_node.node.async_loops()
    assert isinstance(response, list)
    for asyncloop in response:
        assert isinstance(asyncloop, AsyncLoopsModel)
