from pystratis.api import Model
from pystratis.core.types import Address


# noinspection PyUnresolvedReferences
class AddRequest(Model):
    """A request model for the addressbook/address endpoint.

    Args:
        address (Address): The address to add to the address book.
        label (str): A label for the address.
    """
    address: Address
    label: str
