from api import APIRequest, EndpointRegister, endpoint
from api.interop.responsemodels import *
from pybitcoin import Address
from pybitcoin.networks import Ethereum


class Interop(APIRequest, metaclass=EndpointRegister):
    route = '/api/interop'

    def __init__(self, **kwargs):
        super(Interop, self).__init__(**kwargs)

    @endpoint(f'{route}/status')
    def status(self, **kwargs) -> StatusModel:
        """Gets the current interop status.

        Args:
            **kwargs:

        Returns:
            StatusModel

        Raises:
            APIError
        """
        data = self.get(**kwargs)
        new_data = {
            'mintRequests': [],
            'burnRequests': [],
            'receivedVotes': {}
        }
        for item in data['mintRequests']:
            item['destinationAddress'] = Address(address=item['destinationAddress'], network=Ethereum())
            new_data['mintRequests'].append(item)
        for item in data['burnRequests']:
            item['destinationAddress'] = Address(address=item['destinationAddress'], network=self._network)
            new_data['burnRequests'].append(item)
        new_data['receivedVotes'] = data['receivedVotes']

        return StatusModel(**new_data)
