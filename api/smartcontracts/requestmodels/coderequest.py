from pybitcoin import Address, Model


class CodeRequest(Model):
    """A CodeRequest."""
    address: Address
