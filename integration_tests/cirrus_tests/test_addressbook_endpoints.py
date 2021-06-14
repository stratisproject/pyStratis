import pytest
from typing import Callable
from nodes import BaseNode
from api.addressbook.requestmodels import *
from api.addressbook.responsemodels import *
from pybitcoin.types import Address


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_add_address(cirrus_hot_node: BaseNode, random_addresses: Callable):
    addresses = random_addresses(network=cirrus_hot_node.blockchainnetwork)
    for i in range(len(addresses)):
        response = cirrus_hot_node.address_book.add(AddRequest(address=addresses[i], label=f'Label{i}'))
        assert isinstance(response, AddressBookEntryModel)
        assert addresses[i] == response.address
        assert f'Label{i}' == response.label


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_remove_address(cirrus_hot_node: BaseNode, generate_p2pkh_address: Callable):
    address = generate_p2pkh_address(network=cirrus_hot_node.blockchainnetwork)
    address = Address(address=address, network=cirrus_hot_node.blockchainnetwork)
    cirrus_hot_node.address_book.add(AddRequest(address=address, label='AddressToRemove'))

    response = cirrus_hot_node.address_book.remove(RemoveRequest(label='AddressToRemove'))
    assert isinstance(response, AddressBookEntryModel)
    assert address == response.address
    assert response.label == 'AddressToRemove'


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_address_book(cirrus_hot_node: BaseNode, random_addresses: Callable):
    addressbookentries = cirrus_hot_node.address_book(GetRequest())
    if len(addressbookentries) < 2:
        addresses = random_addresses(network=cirrus_hot_node.blockchainnetwork)
        for i in range(len(addresses)):
            cirrus_hot_node.address_book.add(AddRequest(address=addresses[i], label=f'NewLabel{i}'))

    response = cirrus_hot_node.address_book(GetRequest(skip=1, take=1))
    assert len(response) == 1
    for item in response:
        assert isinstance(item, AddressBookEntryModel)
