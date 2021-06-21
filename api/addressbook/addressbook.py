from typing import List
from api import APIRequest, EndpointRegister, endpoint
from api.addressbook.responsemodels import *
from api.addressbook.requestmodels import *
from pybitcoin.types import Address


class AddressBook(APIRequest, metaclass=EndpointRegister):
    """Implements the stratis addressbook api endpoints."""
    route = '/api/addressbook'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/address')
    def add(self, request_model: AddRequest, **kwargs) -> AddressBookEntryModel:
        """Adds an address with label to the address book.

        Args:
            request_model: An AddRequest model.

        Returns:
            AddressBookEntryModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        data['address'] = Address(address=data['address'], network=self._network)
        return AddressBookEntryModel(**data)

    @endpoint(f'{route}/address')
    def remove(self, request_model: RemoveRequest, **kwargs) -> AddressBookEntryModel:
        """Removes an address with the given label from the address book.

        Args:
            request_model: A RemoveRequest model.

        Returns:
            AddressBookEntryModel

        Raises:
            APIError
        """
        data = self.delete(request_model, **kwargs)

        data['address'] = Address(address=data['address'], network=self._network)
        return AddressBookEntryModel(**data)

    @endpoint(f'{route}')
    def __call__(self, request_model: GetRequest = GetRequest(), **kwargs) -> List[AddressBookEntryModel]:
        """Retrieves the address book with option to implement pagination.

        If neither skip or take arguments are specified, returns the entire address book.

        Args:
            request_model: An GetRequest model.

        Returns:
            List[AddressBookEntryModel]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        addressbook = [
            AddressBookEntryModel(
                address=Address(address=item['address'], network=self._network),
                label=item['label']
            ) for item in data['addresses']]
        return addressbook
