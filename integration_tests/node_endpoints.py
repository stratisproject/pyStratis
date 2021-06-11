from typing import List
from nodes import BaseNode
from api.node.requestmodels import *
from api.wallet.responsemodels import SpendableTransactionModel
from pybitcoin.types import uint256, hexstr
from pybitcoin import LogRule


def check_node_endpoints(
        node: BaseNode,
        block_hash: uint256,
        spendable_transactions: List[SpendableTransactionModel],
        address_string: str,
        log_rules: List[LogRule]) -> None:
    trxids = [x.transaction_id for x in spendable_transactions]
    assert check_status(node)
    assert check_get_blockheader(node, block_hash)
    assert check_get_raw_transaction(node, trxids[0])
    for trxid in trxids:
        raw_transaction = node.node.get_raw_transaction(
            request_model=GetRawTransactionRequest(trxid=trxid, verbose=False)
        )
        assert check_decode_raw_transaction(node, raw_transaction)
    assert check_validate_address(node, address_string)
    assert check_get_txout(node, trxids[0])
    assert check_get_txout_proof(node, trxids)
    assert check_log_levels(node, log_rules)
    assert check_log_rules(node)
    assert check_async_loops(node)
    assert check_shutdown()
    assert check_stop()


def check_status(node: BaseNode) -> bool:
    node.node.status()
    return True


def check_get_blockheader(node: BaseNode, block_hash: uint256) -> bool:
    request_model = GetBlockHeaderRequest(hash=block_hash, is_json_format=True)
    node.node.get_blockheader(request_model)
    return True


def check_get_raw_transaction(node: BaseNode, trxid: uint256) -> bool:
    request_model = GetRawTransactionRequest(trxid=trxid, verbose=True)
    node.node.get_raw_transaction(request_model)
    request_model = GetRawTransactionRequest(trxid=trxid, verbose=False)
    node.node.get_raw_transaction(request_model)
    return True


def check_decode_raw_transaction(node: BaseNode, raw_transaction: hexstr) -> bool:
    request_model = DecodeRawTransactionRequest(raw_hex=raw_transaction)
    node.node.decode_raw_transaction(request_model)
    return True


def check_validate_address(node: BaseNode, address: str) -> bool:
    request_model = ValidateAddressRequest(address=address)
    node.node.validate_address(request_model)
    return True


def check_get_txout(node: BaseNode, trxid: uint256) -> bool:
    request_model = GetTxOutRequest(trxid=trxid, vout=0, include_mempool=False)
    node.node.get_txout(request_model)
    return True


def check_get_txout_proof(node: BaseNode, txids: List[uint256]) -> bool:
    for txid in txids:
        request_model = GetRawTransactionRequest(trxid=txid, verbose=True)
        raw_transaction = node.node.get_raw_transaction(request_model)
        request_model = GetTxOutProofRequest(txids=[txid], blockhash=raw_transaction.blockhash)
        node.node.get_txout_proof(request_model)
    return True


def check_shutdown() -> bool:
    # Used at the end of the integration tests
    return True


def check_stop() -> bool:
    # Used at the end of the integration tests
    return True


def check_log_levels(node: BaseNode, log_rules: List[LogRule]) -> bool:
    request_model = LogRulesRequest(log_rules=log_rules)
    node.node.log_levels(request_model)
    return True


def check_log_rules(node: BaseNode) -> bool:
    node.node.log_rules()
    return True


def check_async_loops(node: BaseNode) -> bool:
    node.node.async_loops()
    return True
