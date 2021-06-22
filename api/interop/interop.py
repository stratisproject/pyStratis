from api import APIRequest, EndpointRegister, endpoint
from api.interop.responsemodels import *
from pybitcoin.types import Address, Money, uint256
from pybitcoin.networks import Ethereum
from pybitcoin import PubKey


class Interop(APIRequest, metaclass=EndpointRegister):
    route = '/api/interop'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
        if data['mintRequests'] is not None:
            for i in range(len(data['mintRequests'])):
                data['mintRequests'][i]['amount'] = Money.from_satoshi_units(data['mintRequests'][i]['amount'])
                data['mintRequests'][i]['destinationAddress'] = Address(
                    address=data['mintRequests'][i]['destinationAddress'],
                    network=Ethereum()
                )
        if data['burnRequests'] is not None:
            for i in range(len(data['burnRequests'])):
                data['burnRequests'][i]['amount'] = Money.from_satoshi_units(data['burnRequests'][i]['amount'])
                data['burnRequests'][i]['destinationAddress'] = Address(
                    address=data['burnRequests'][i]['destinationAddress'],
                    network=self._network
                )
        received_votes = {}
        if data['receivedVotes'] is not None:
            for key in data['receivedVotes'].keys():
                values = [PubKey(x) for x in data['receivedVotes'][key]]
                received_votes[uint256(key)] = values
        data['receivedVotes'] = received_votes

        return StatusModel(**data)
