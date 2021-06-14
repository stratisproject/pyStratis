import pytest
from typing import Callable
from nodes import BaseNode
from api.addressbook.requestmodels import *
from api.addressbook.responsemodels import *
from pybitcoin.types import Address


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_add_address(strax_hot_node: BaseNode, random_addresses: Callable):
    addresses = random_addresses(network=strax_hot_node.blockchainnetwork)
    for i in range(len(addresses)):
        response = strax_hot_node.address_book.add(AddRequest(address=addresses[i], label=f'Label{i}'))
        assert isinstance(response, AddressBookEntryModel)
        assert addresses[i] == response.address
        assert f'Label{i}' == response.label


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_remove_address(strax_hot_node: BaseNode, generate_p2pkh_address: Callable):
    address = generate_p2pkh_address(network=strax_hot_node.blockchainnetwork)
    address = Address(address=address, network=strax_hot_node.blockchainnetwork)
    strax_hot_node.address_book.add(AddRequest(address=address, label='AddressToRemove'))

    response = strax_hot_node.address_book.remove(RemoveRequest(label='AddressToRemove'))
    assert isinstance(response, AddressBookEntryModel)
    assert address == response.address
    assert response.label == 'AddressToRemove'


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_address_book(strax_hot_node: BaseNode, random_addresses: Callable):
    addressbookentries = strax_hot_node.address_book(GetRequest())
    if len(addressbookentries) < 2:
        addresses = random_addresses(network=strax_hot_node.blockchainnetwork)
        for i in range(len(addresses)):
            strax_hot_node.address_book.add(AddRequest(address=addresses[i], label=f'NewLabel{i}'))

    response = strax_hot_node.address_book(GetRequest(skip=1, take=1))
    assert len(response) == 1
    for item in response:
        assert isinstance(item, AddressBookEntryModel)
