from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.interop.responsemodels import *
from pystratis.core.types import Address, Money, uint256
from pystratis.core.networks import Ethereum
from pystratis.core import PubKey


class Interop(APIRequest, metaclass=EndpointRegister):
    """Implements the interop api endpoints."""

    route = '/api/interop'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/status')
    def status(self, **kwargs) -> StatusModel:
        """Gets the current interop status.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            StatusModel: The status of the interoperability service.

        Raises:
            APIError: Error thrown by node API. See message for details.
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
            for key in data['receivedVotes']:
                values = [PubKey(x) for x in data['receivedVotes'][key]]
                received_votes[uint256(key)] = values
        data['receivedVotes'] = received_votes
        return StatusModel(**data)
