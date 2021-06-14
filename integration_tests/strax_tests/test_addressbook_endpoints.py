import pytest
from typing import Callable
from nodes import BaseNode
from api.addressbook.requestmodels import *
from api.addressbook.responsemodels import *
from pybitcoin.types import Address


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_add_address(hot_node: BaseNode, random_addresses: Callable):
    addresses = random_addresses(network=hot_node.blockchainnetwork)
    for i in range(len(addresses)):
        response = hot_node.address_book.add(AddRequest(address=addresses[i], label=f'Label{i}'))
        assert isinstance(response, AddressBookEntryModel)
        assert addresses[i] == response.address
        assert f'Label{i}' == response.label


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_remove_address(hot_node: BaseNode, generate_p2pkh_address: Callable):
    address = generate_p2pkh_address(network=hot_node.blockchainnetwork)
    address = Address(address=address, network=hot_node.blockchainnetwork)
    hot_node.address_book.add(AddRequest(address=address, label='AddressToRemove'))

    response = hot_node.address_book.remove(RemoveRequest(label='AddressToRemove'))
    assert isinstance(response, AddressBookEntryModel)
    assert address == response.address
    assert response.label == 'AddressToRemove'


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_address_book(hot_node: BaseNode, random_addresses: Callable):
    addressbookentries = hot_node.address_book(GetRequest())
    if len(addressbookentries) < 2:
        addresses = random_addresses(network=hot_node.blockchainnetwork)
        for i in range(len(addresses)):
            hot_node.address_book.add(AddRequest(address=addresses[i], label=f'NewLabel{i}'))

    response = hot_node.address_book(GetRequest(skip=1, take=1))
    assert len(response) == 1
    for item in response:
        assert isinstance(item, AddressBookEntryModel)
