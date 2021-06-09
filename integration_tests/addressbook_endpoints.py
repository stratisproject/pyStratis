from typing import List
from nodes import BaseNode
from api.addressbook.requestmodels import *
from pybitcoin.types import Address


def check_addressbook_endpoints(node: BaseNode, addresses: List[Address]) -> None:
    for i in range(len(addresses)):
        assert check_add_address(node, addresses[i], f'Label{i}')
    assert check_get_address_book(node)
    for i in range(len(addresses)):
        assert check_remove_address(node, f'Label{i}')


def check_add_address(node: BaseNode, address: Address, label: str) -> bool:
    node.address_book.add(AddRequest(address=address, label=label))
    return True


def check_remove_address(node: BaseNode, label: str) -> bool:
    node.address_book.remove(RemoveRequest(label=label))
    return True


def check_get_address_book(node: BaseNode) -> bool:
    node.address_book.get(GetRequest(skip=1, take=1))
    return True
