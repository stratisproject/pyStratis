import json
from typing import List, Union, Optional
from pydantic import Field
from pybitcoin import Address, Model


class GetAddressesBalancesRequest(Model):
    """A GetAddressesBalancesRequest."""
    addresses: Union[List[Address], Address]
    min_confirmations: Optional[int] = Field(default=0, alias='minConfirmations')

    def json(self, *args, **kwargs) -> str:
        data = super(Model, self).dict(exclude_none=True, by_alias=True)
        if isinstance(data['addresses'], list):
            data['addresses'] = ','.join([x.json() for x in data['addresses']])
        if isinstance(data['addresses'], Address):
            data['addresses'] = data['addresses'].json()
        return json.dumps(data)
