from pybitcoin import Address
from pybitcoin import Model


class AddRequest(Model):
    """An AddRequest."""
    label: str
    address: Address
