import json
from typing import List, Union, Optional
from pydantic import Field, validator
from pybitcoin import Model
from pybitcoin.types import Address


class GetAddressesBalancesRequest(Model):
    """A GetAddressesBalancesRequest."""
    addresses: Union[Address, List[Address]]
    min_confirmations: Optional[int] = Field(default=0, alias='minConfirmations')

    # noinspection PyMethodParameters
    @validator('addresses', each_item=True)
    def check_addresses(cls, v):
        if isinstance(v, list):
            for item in v:
                assert isinstance(item, Address)
        else:
            assert isinstance(v, Address)
        return v

    def json(self, *args, **kwargs) -> str:
        data = super(GetAddressesBalancesRequest, self).dict(exclude_none=True, by_alias=True)
        if isinstance(data['addresses'], list):
            data['addresses'] = ','.join([x.json() for x in data['addresses']])
        if isinstance(data['addresses'], Address):
            data['addresses'] = data['addresses'].json()
        return json.dumps(data)
