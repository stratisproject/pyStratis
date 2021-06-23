from pybitcoin.types import Address
from pybitcoin import Model


class GetLastBalanceUpdateTransactionRequest(Model):
    """A request model for the blockstore/getlastbalanceupdatetransaction endpoint.

    Args:
        address (Address): An address to query.
    """
    address: Address

