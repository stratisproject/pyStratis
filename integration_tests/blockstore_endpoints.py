from typing import List
from nodes import BaseNode
from api.blockstore.requestmodels import *
from pybitcoin.types import Address, uint256


def check_blockstore_endpoints(
        node: BaseNode,
        addresses: List[Address],
        height: int,
        block_hash: uint256) -> None:
    assert check_addressindexer_tip(node)
    assert check_block_json(node, block_hash)
    assert check_block_nojson(node, block_hash)
    bad_block_hash = uint256('fffdf')
    assert check_block_json(node, bad_block_hash)
    assert check_get_addresses_balances_single_address(node, addresses[0])
    assert check_get_verbose_addresses_balances_single_address(node, addresses[0])
    assert check_get_verbose_addresses_balances_multiple_addresses(node, addresses)
    assert check_get_utxoset(node, height)
    assert check_get_last_balance_update_transaction(node, addresses[0])


def check_addressindexer_tip(node: BaseNode) -> bool:
    node.blockstore.addressindexer_tip()
    return True


def check_block_json(node: BaseNode, block_hash: uint256) -> bool:
    request_model = BlockRequest(
        hash=block_hash,
        show_transaction_details=True,
        output_json=True
    )
    node.blockstore.block(request_model=request_model)
    return True


def check_block_nojson(node: BaseNode, block_hash: uint256) -> bool:
    request_model = BlockRequest(
        hash=block_hash,
        show_transaction_details=True,
        output_json=False
    )
    node.blockstore.block(request_model=request_model)
    return True


def check_get_block_count(node: BaseNode) -> bool:
    node.blockstore.get_block_count()
    return True


def check_get_addresses_balances_single_address(node: BaseNode, address: Address) -> bool:
    request_model = GetAddressesBalancesRequest(addresses=address)
    node.blockstore.get_addresses_balances(request_model=request_model)
    return True


def check_get_addresses_balances_multiple_addresses(node: BaseNode, addresses: List[Address]) -> bool:
    request_model = GetAddressesBalancesRequest(addresses=addresses)
    node.blockstore.get_addresses_balances(request_model=request_model)
    return True


def check_get_verbose_addresses_balances_single_address(node: BaseNode, address: Address) -> bool:
    request_model = GetVerboseAddressesBalancesRequest(addresses=address)
    node.blockstore.get_verbose_addresses_balances(request_model=request_model)
    return True


def check_get_verbose_addresses_balances_multiple_addresses(node: BaseNode, addresses: List[Address]) -> bool:
    request_model = GetVerboseAddressesBalancesRequest(addresses=addresses)
    node.blockstore.get_verbose_addresses_balances(request_model=request_model)
    return True


def check_get_utxoset(node: BaseNode, height: int) -> bool:
    request_model = GetUTXOSetRequest(at_block_height=height)
    node.blockstore.get_utxo_set(request_model=request_model)
    return True


def check_get_last_balance_update_transaction(node: BaseNode, address: Address) -> bool:
    request_model = GetLastBalanceUpdateTransactionRequest(address=address)
    node.blockstore.get_last_balance_update_transaction(request_model=request_model)
    return True
