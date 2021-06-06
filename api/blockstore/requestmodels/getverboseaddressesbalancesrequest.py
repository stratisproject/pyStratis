import json
from typing import List, Union
from pybitcoin import Address, Model


class GetVerboseAddressesBalancesRequest(Model):
    """A GetVerboseAddressesBalancesRequest."""
    addresses: Union[List[Address], Address]

    def json(self, *args, **kwargs) -> str:
        data = super(Model, self).dict(exclude_none=True, by_alias=True)
        if isinstance(data['addresses'], list):
            data['addresses'] = ','.join([x.json() for x in data['addresses']])
        if isinstance(data['addresses'], Address):
            data['addresses'] = data['addresses'].json()
        return json.dumps(data)
