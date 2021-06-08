from pybitcoin import Model
from pybitcoin.types import Address


class AddressBalanceRequest(Model):
    """An AddressBalanceRequest."""
    address: Address
