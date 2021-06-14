import pytest
from nodes import BaseNode
from api.node.requestmodels import *
from api.node.responsemodels import *
from pybitcoin import LogRule
from pybitcoin.types import uint256, hexstr, Money


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_status(hot_node: BaseNode):
    response = hot_node.node.status()
    assert isinstance(response, StatusModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_blockheader(hot_node: BaseNode):
    block_hash = hot_node.consensus.get_best_blockhash()
    request_model = GetBlockHeaderRequest(hash=block_hash, is_json_format=True)
    response = hot_node.node.get_blockheader(request_model)
    assert isinstance(response, BlockHeaderModel)
    if response.previous_blockhash is not None:
        assert isinstance(response.previous_blockhash, uint256)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_raw_transaction(hot_node: BaseNode):
    from api.wallet.requestmodels import SpendableTransactionsRequest
    request_model = SpendableTransactionsRequest(wallet_name='Test', account_name='account 0', min_confirmations=10)
    spendable_transactions = hot_node.wallet.spendable_transactions(request_model)
    spendable_transactions = [x for x in spendable_transactions.transactions]
    for spendable_transaction in spendable_transactions:
        request_model = GetRawTransactionRequest(trxid=spendable_transaction.transaction_id, verbose=True)
        response = hot_node.node.get_raw_transaction(request_model)
        assert isinstance(response, TransactionModel)

        request_model = GetRawTransactionRequest(trxid=spendable_transaction.transaction_id, verbose=False)
        response = hot_node.node.get_raw_transaction(request_model)
        assert isinstance(response, hexstr)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_decode_raw_transaction(hot_node: BaseNode):
    from api.wallet.requestmodels import SpendableTransactionsRequest
    request_model = SpendableTransactionsRequest(wallet_name='Test', account_name='account 0', min_confirmations=10)
    spendable_transactions = hot_node.wallet.spendable_transactions(request_model)
    spendable_transactions = [x for x in spendable_transactions.transactions]
    for spendable_transaction in spendable_transactions:
        request_model = GetRawTransactionRequest(trxid=spendable_transaction.transaction_id, verbose=False)
        raw_transaction = hot_node.node.get_raw_transaction(request_model)
        request_model = DecodeRawTransactionRequest(raw_hex=raw_transaction)
        response = hot_node.node.decode_raw_transaction(request_model)
        assert isinstance(response, TransactionModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_validate_address(hot_node: BaseNode, generate_p2pkh_address):
    address = generate_p2pkh_address(network=hot_node.blockchainnetwork)
    request_model = ValidateAddressRequest(address=address)
    response = hot_node.node.validate_address(request_model)
    assert isinstance(response, ValidateAddressModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_txout(hot_node: BaseNode):
    from api.wallet.requestmodels import SpendableTransactionsRequest
    request_model = SpendableTransactionsRequest(wallet_name='Test', account_name='account 0', min_confirmations=10)
    spendable_transactions = hot_node.wallet.spendable_transactions(request_model)
    spendable_transactions = [x for x in spendable_transactions.transactions]
    for spendable_transaction in spendable_transactions:
        request_model = GetTxOutRequest(trxid=spendable_transaction.transaction_id, vout=spendable_transaction.index, include_mempool=False)
        response = hot_node.node.get_txout(request_model)
        assert isinstance(response, GetTxOutModel)
        assert isinstance(response.best_block, uint256)
        assert isinstance(response.value, Money)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_txout_proof(hot_node: BaseNode):
    from api.wallet.requestmodels import SpendableTransactionsRequest
    request_model = SpendableTransactionsRequest(wallet_name='Test', account_name='account 0', min_confirmations=10)
    spendable_transactions = hot_node.wallet.spendable_transactions(request_model)
    spendable_transactions = [x for x in spendable_transactions.transactions]
    for spendable_transaction in spendable_transactions:
        request_model = GetRawTransactionRequest(trxid=spendable_transaction.transaction_id, verbose=True)
        raw_transaction = hot_node.node.get_raw_transaction(request_model)
        request_model = GetTxOutProofRequest(txids=[spendable_transaction.transaction_id], blockhash=raw_transaction.blockhash)
        response = hot_node.node.get_txout_proof(request_model)
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
def test_log_levels(hot_node: BaseNode):
    request_model = LogRulesRequest(log_rules=[LogRule(rule_name='Stratis.*', log_level='Debug')])
    hot_node.node.log_levels(request_model)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_log_rules(hot_node: BaseNode):
    response = hot_node.node.log_rules()
    assert isinstance(response, list)
    for logrule in response:
        assert isinstance(logrule, LogRulesModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_async_loops(hot_node: BaseNode):
    response = hot_node.node.async_loops()
    assert isinstance(response, list)
    for asyncloop in response:
        assert isinstance(asyncloop, AsyncLoopsModel)
