from typing import Union, List
from pystratis.api.addressbook.responsemodels import *
from pystratis.api.addressbook.requestmodels import *
from pystratis.core.types import Address
from pystratis.api import APIRequest, EndpointRegister, endpoint


class AddressBook(APIRequest, metaclass=EndpointRegister):
    """Implements the addressbook api endpoints."""

    route = '/api/addressbook'

    def __init__(self, **kwargs):
        """Implements the stratis addressbook api endpoints."""
        super().__init__(**kwargs)

    @endpoint(f'{route}/address')
    def add(self,
            address: Union[str, Address],
            label: str,
            **kwargs) -> AddressBookEntryModel:
        """Adds an entry to the address book.

        Args:
            address (str, Address): The address to add to the address book.
            label (str): The address label.

        Returns:
            AddressBookEntryModel: The address book entry.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(address, str):
            address = Address(address=address, network=self._network)
        request_model = AddRequest(address=address, label=label)
        data = self.post(request_model, **kwargs)
        data['address'] = Address(address=data['address'], network=self._network)
        return AddressBookEntryModel(**data)

    @endpoint(f'{route}/address')
    def remove(self, label: str, **kwargs) -> AddressBookEntryModel:
        """Removes an entry from the address book.

        Args:
            label (str): The label to remove.

        Returns:
            AddressBookEntryModel: The address book entry.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = RemoveRequest(label=label)
        data = self.delete(request_model, **kwargs)
        data['address'] = Address(address=data['address'], network=self._network)
        return AddressBookEntryModel(**data)

    @endpoint(f'{route}')
    def __call__(self, skip: int = None, take: int = None, **kwargs) -> List[AddressBookEntryModel]:
        """Gets the address book entries with option to implement pagination.

        Args:
            skip (int, optional): The number of entries to skip.
            take (int, optional): The maximum number of entries to take.

        Returns:
            List[AddressBookEntryModel]: A list of address book entries.

        Raises:
            APIError: Error thrown by node API. See message for details.

        Note:
            If neither skip or take arguments are specified, returns the entire address book.
            An address book can be accessed from a wallet, but it is a standalone feature, which is not attached to any wallet.
        """
        request_model = GetRequest(skip=skip, take=take)
        data = self.get(request_model, **kwargs)
        addressbook = [
            AddressBookEntryModel(
                address=Address(address=item['address'], network=self._network), label=item['label']
            ) for item in data['addresses']]
        return addressbook
