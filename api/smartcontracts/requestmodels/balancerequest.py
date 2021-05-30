from pybitcoin import Address, Model


class BalanceRequest(Model):
    """A BalanceRequest."""
    address: Address
