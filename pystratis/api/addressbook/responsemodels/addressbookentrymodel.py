from pystratis.api import Model
from pystratis.core.types import Address


class AddressBookEntryModel(Model):
    """A pydantic model representing an address book entry."""
    address: Address
    """An address validated for the current network."""
    label: str
    """A label for the given address."""

    def __eq__(self, other) -> bool:
        if self.address == other.address and self.label == other.label:
            return True
        return False
