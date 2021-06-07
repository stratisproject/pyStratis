from typing import Optional
from pybitcoin import Address, Model


class AddressBookEntryModel(Model):
    """An AddressBookEntryModel."""
    address: Optional[Address]
    label: Optional[str]

    def __eq__(self, other) -> bool:
        if self.address == other.address and self.label == other.label:
            return True
        return False
