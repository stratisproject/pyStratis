from pybitcoin import Address, Model


class AddRequest(Model):
    """An AddRequest."""
    address: Address
    label: str
