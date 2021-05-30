from typing import List, Union, Optional
from pydantic import Field
from pybitcoin import Address, Model


class GetAddressesBalancesRequest(Model):
    """AGetAddressesBalancesRequest."""
    addresses: Union[Address, List[Address]]
    min_confirmations: Optional[int] = Field(default=0, alias='minConfirmations')
