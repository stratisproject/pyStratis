import pytest
from nodes import CirrusMinerNode
from api.addressbook.responsemodels import *
from pybitcoin.types import Address


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_add_address(cirrusminer_node: CirrusMinerNode, cirrusminer_syncing_node: CirrusMinerNode, random_addresses):
    addresses = random_addresses(network=cirrusminer_node.blockchainnetwork)
    for i in range(len(addresses)):
        response = cirrusminer_node.address_book.add(address=addresses[i], label=f'Label{i}')
        assert isinstance(response, AddressBookEntryModel)
        assert addresses[i] == response.address
        assert f'Label{i}' == response.label


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_remove_address(cirrusminer_node: CirrusMinerNode, cirrusminer_syncing_node: CirrusMinerNode,  generate_p2pkh_address):
    address = generate_p2pkh_address(network=cirrusminer_node.blockchainnetwork)
    cirrusminer_node.address_book.add(address=address, label='AddressToRemove')

    response = cirrusminer_node.address_book.remove(label='AddressToRemove')
    assert isinstance(response, AddressBookEntryModel)
    assert address == response.address
    assert response.label == 'AddressToRemove'


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_address_book(cirrusminer_node: CirrusMinerNode, random_addresses):
    addressbookentries = cirrusminer_node.address_book()
    if len(addressbookentries) < 2:
        addresses = random_addresses(network=cirrusminer_node.blockchainnetwork)
        for i in range(len(addresses)):
            cirrusminer_node.address_book.add(address=addresses[i], label=f'NewLabel{i}')

    response = cirrusminer_node.address_book(skip=1, take=1)
    assert len(response) == 1
    for item in response:
        assert isinstance(item, AddressBookEntryModel)
