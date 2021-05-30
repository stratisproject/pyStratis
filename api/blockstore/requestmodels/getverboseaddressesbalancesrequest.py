from typing import List, Union
from pybitcoin import Address, Model


class GetVerboseAddressesBalancesRequest(Model):
    """A GetVerboseAddressesBalancesRequest."""
    addresses: Union[Address, List[Address]]
