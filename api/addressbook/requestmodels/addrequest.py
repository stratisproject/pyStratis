from pybitcoin import Model
from pybitcoin.types import Address


class AddRequest(Model):
    """An AddRequest."""
    address: Address
    label: str
