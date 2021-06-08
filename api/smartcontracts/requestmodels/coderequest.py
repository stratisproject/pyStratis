from pybitcoin import Model
from pybitcoin.types import Address


class CodeRequest(Model):
    """A CodeRequest."""
    address: Address
