import pytest
from nodes import CirrusNode, CirrusMinerNode
from api.addressbook.requestmodels import *
from api.addressbook.responsemodels import *
from pybitcoin.types import Address


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_add_address(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode, random_addresses):
    addresses = random_addresses(network=cirrusminer_node.blockchainnetwork)
    for i in range(len(addresses)):
        response = cirrusminer_node.address_book.add(AddRequest(address=addresses[i], label=f'Label{i}'))
        assert isinstance(response, AddressBookEntryModel)
        assert addresses[i] == response.address
        assert f'Label{i}' == response.label

        response = cirrus_syncing_node.address_book.add(AddRequest(address=addresses[i], label=f'Label{i}'))
        assert isinstance(response, AddressBookEntryModel)
        assert addresses[i] == response.address
        assert f'Label{i}' == response.label


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_remove_address(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode,  generate_p2pkh_address):
    address = generate_p2pkh_address(network=cirrusminer_node.blockchainnetwork)
    address = Address(address=address, network=cirrusminer_node.blockchainnetwork)
    cirrusminer_node.address_book.add(AddRequest(address=address, label='AddressToRemove'))
    cirrus_syncing_node.address_book.add(AddRequest(address=address, label='AddressToRemove'))

    response = cirrusminer_node.address_book.remove(RemoveRequest(label='AddressToRemove'))
    assert isinstance(response, AddressBookEntryModel)
    assert address == response.address
    assert response.label == 'AddressToRemove'

    response = cirrus_syncing_node.address_book.remove(RemoveRequest(label='AddressToRemove'))
    assert isinstance(response, AddressBookEntryModel)
    assert address == response.address
    assert response.label == 'AddressToRemove'


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_address_book(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode, random_addresses):
    addressbookentries = cirrusminer_node.address_book(GetRequest())
    if len(addressbookentries) < 2:
        addresses = random_addresses(network=cirrusminer_node.blockchainnetwork)
        for i in range(len(addresses)):
            cirrusminer_node.address_book.add(AddRequest(address=addresses[i], label=f'NewLabel{i}'))
            cirrus_syncing_node.address_book.add(AddRequest(address=addresses[i], label=f'NewLabel{i}'))

    response = cirrusminer_node.address_book(GetRequest(skip=1, take=1))
    assert len(response) == 1
    for item in response:
        assert isinstance(item, AddressBookEntryModel)

    response = cirrus_syncing_node.address_book(GetRequest(skip=1, take=1))
    assert len(response) == 1
    for item in response:
        assert isinstance(item, AddressBookEntryModel)
