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
    assert check_block(node, block_hash)
    assert check_get_addresses_balances(node, addresses)
    assert check_get_verbose_addresses_balances(node, addresses)
    assert check_get_utxoset(node, height)
    assert check_get_last_balance_update_transaction(node, addresses[0])


def check_addressindexer_tip(node: BaseNode) -> bool:
    node.blockstore.addressindexer_tip()
    return True


def check_block(node: BaseNode, block_hash: uint256) -> bool:
    # Request json output with maximum details.
    request_model = BlockRequest(
        hash=block_hash,
        show_transaction_details=True,
        output_json=True
    )
    node.blockstore.block(request_model=request_model)

    # Request hex output.
    request_model = BlockRequest(
        hash=block_hash,
        show_transaction_details=True,
        output_json=False
    )
    node.blockstore.block(request_model=request_model)

    # Request a hash that doesn't exist.
    bad_block_hash = uint256('fffdf')
    request_model = BlockRequest(
        hash=bad_block_hash,
        show_transaction_details=True,
        output_json=False
    )
    node.blockstore.block(request_model=request_model)
    return True


def check_get_block_count(node: BaseNode) -> bool:
    node.blockstore.get_block_count()
    return True


def check_get_addresses_balances(node: BaseNode, addresses: List[Address]) -> bool:
    request_model = GetAddressesBalancesRequest(addresses=addresses[0])
    node.blockstore.get_addresses_balances(request_model=request_model)
    request_model = GetAddressesBalancesRequest(addresses=addresses)
    node.blockstore.get_addresses_balances(request_model=request_model)
    return True


def check_get_verbose_addresses_balances(node: BaseNode, addresses: List[Address]) -> bool:
    request_model = GetVerboseAddressesBalancesRequest(addresses=addresses[0])
    node.blockstore.get_verbose_addresses_balances(request_model=request_model)
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
