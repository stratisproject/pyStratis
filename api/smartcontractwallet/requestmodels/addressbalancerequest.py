from pybitcoin import Address, Model


class AddressBalanceRequest(Model):
    """An AddressBalanceRequest."""
    address: Address
