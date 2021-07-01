import pytest
from pytest_mock import MockerFixture
from api.addressbook import AddressBook
from pybitcoin.types import Address
from pybitcoin.networks import StraxMain, CirrusMain


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths']]
    for endpoint in paths:
        if AddressBook.route + '/' in endpoint:
            assert endpoint in AddressBook.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths']]
    for endpoint in paths:
        if AddressBook.route + '/' in endpoint:
            assert endpoint in AddressBook.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths']]
    for endpoint in paths:
        if AddressBook.route + '/' in endpoint:
            assert endpoint in AddressBook.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths']]
    for endpoint in paths:
        if AddressBook.route + '/' in endpoint:
            assert endpoint in AddressBook.endpoints


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_add_address_p2pkh(mocker: MockerFixture, network, addressbookentry_p2pkh, generate_p2pkh_address):
    data = addressbookentry_p2pkh(network)
    mocker.patch.object(AddressBook, 'post', return_value=data)
    addressbook = AddressBook(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = addressbook.add(address=data['address'], label=data['label'])

    assert response.address == data['address']
    assert response.label == data['label']
    # noinspection PyUnresolvedReferences
    addressbook.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_add_address_p2sh(mocker: MockerFixture, network, addressbookentry_p2sh, generate_p2sh_address):
    data = addressbookentry_p2sh(network)
    mocker.patch.object(AddressBook, 'post', return_value=data)
    addressbook = AddressBook(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = addressbook.add(address=data['address'], label=data['label'])

    assert response.address == data['address']
    assert response.label == data['label']
    # noinspection PyUnresolvedReferences
    addressbook.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_add_address_p2wpkh(mocker: MockerFixture, addressbookentry_p2wpkh, network, generate_p2wpkh_address):
    data = addressbookentry_p2wpkh(network)
    mocker.patch.object(AddressBook, 'post', return_value=data)
    addressbook = AddressBook(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = addressbook.add(address=data['address'], label=data['label'])

    assert response.address == data['address']
    assert response.label == data['label']
    # noinspection PyUnresolvedReferences
    addressbook.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_add_address_p2wsh(mocker: MockerFixture, network, addressbookentry_p2wsh, generate_p2wsh_address):
    data = addressbookentry_p2wsh(network)
    mocker.patch.object(AddressBook, 'post', return_value=data)
    addressbook = AddressBook(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = addressbook.add(address=data['address'], label=data['label'])

    assert response.address == data['address']
    assert response.label == data['label']
    # noinspection PyUnresolvedReferences
    addressbook.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_remove_address(mocker: MockerFixture, network, addressbookentry_p2pkh):
    data = addressbookentry_p2pkh(network)
    mocker.patch.object(AddressBook, 'delete', return_value=data)
    addressbook = AddressBook(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = addressbook.remove(label=data['label'])

    assert response.address == data['address']
    assert response.label == data['label']
    # noinspection PyUnresolvedReferences
    addressbook.delete.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_addressbook_full_p2pkh(mocker: MockerFixture, network, fulladdressbook_p2pkh):
    data = fulladdressbook_p2pkh(network)
    mocker.patch.object(AddressBook, 'get', return_value=data)
    addressbook = AddressBook(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = addressbook()

    assert len(response) == 5
    for i in range(len(response)):
        assert response[i].address == data['addresses'][i]['address']
        assert response[i].label == data['addresses'][i]['label']
    # noinspection PyUnresolvedReferences
    addressbook.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_addressbook_full_p2sh(mocker: MockerFixture, network, fulladdressbook_p2sh):
    data = fulladdressbook_p2sh(network)
    mocker.patch.object(AddressBook, 'get', return_value=data)
    addressbook = AddressBook(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = addressbook()

    assert len(response) == 5
    for i in range(len(response)):
        assert response[i].address == data['addresses'][i]['address']
        assert response[i].label == data['addresses'][i]['label']
    # noinspection PyUnresolvedReferences
    addressbook.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_addressbook_full_p2wpkh(mocker: MockerFixture, network, fulladdressbook_p2wpkh):
    data = fulladdressbook_p2wpkh(network)
    mocker.patch.object(AddressBook, 'get', return_value=data)
    addressbook = AddressBook(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = addressbook()

    assert len(response) == 5
    for i in range(len(response)):
        assert response[i].address == data['addresses'][i]['address']
        assert response[i].label == data['addresses'][i]['label']
    # noinspection PyUnresolvedReferences
    addressbook.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_addressbook_full_p2wsh(mocker: MockerFixture, network, fulladdressbook_p2wsh):
    data = fulladdressbook_p2wsh(network)
    mocker.patch.object(AddressBook, 'get', return_value=data)
    addressbook = AddressBook(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = addressbook()

    assert len(response) == 5
    for i in range(len(response)):
        assert response[i].address == data['addresses'][i]['address']
        assert response[i].label == data['addresses'][i]['label']
    # noinspection PyUnresolvedReferences
    addressbook.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_addressbook_paginated_p2pkh(mocker: MockerFixture, network, partialaddressbook_p2pkh):
    data = partialaddressbook_p2pkh(network)
    mocker.patch.object(AddressBook, 'get', return_value=data)
    addressbook = AddressBook(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = addressbook(skip=2, take=2)

    assert len(response) == 2
    for i in range(len(response)):
        assert response[i].address == data['addresses'][i]['address']
        assert response[i].label == data['addresses'][i]['label']
    # noinspection PyUnresolvedReferences
    addressbook.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_addressbook_paginated_p2sh(mocker: MockerFixture, network, partialaddressbook_p2sh):
    data = partialaddressbook_p2sh(network)
    mocker.patch.object(AddressBook, 'get', return_value=data)
    addressbook = AddressBook(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = addressbook(skip=2, take=2)

    assert len(response) == 2
    for i in range(len(response)):
        assert response[i].address == data['addresses'][i]['address']
        assert response[i].label == data['addresses'][i]['label']
    # noinspection PyUnresolvedReferences
    addressbook.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_addressbook_paginated_p2wpkh(mocker: MockerFixture, network, partialaddressbook_p2wpkh):
    data = partialaddressbook_p2wpkh(network)
    mocker.patch.object(AddressBook, 'get', return_value=data)
    addressbook = AddressBook(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = addressbook(skip=2, take=2)

    assert len(response) == 2
    for i in range(len(response)):
        assert response[i].address == data['addresses'][i]['address']
        assert response[i].label == data['addresses'][i]['label']
    # noinspection PyUnresolvedReferences
    addressbook.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_addressbook_paginated_p2wsh(mocker: MockerFixture, network, partialaddressbook_p2wsh):
    data = partialaddressbook_p2wsh(network)
    mocker.patch.object(AddressBook, 'get', return_value=data)
    addressbook = AddressBook(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = addressbook(skip=2, take=2)

    assert len(response) == 2
    for i in range(len(response)):
        assert response[i].address == data['addresses'][i]['address']
        assert response[i].label == data['addresses'][i]['label']
    # noinspection PyUnresolvedReferences
    addressbook.get.assert_called_once()
