from api import APIRequest, EndpointRegister, endpoint
from api.interop.responsemodels import *
from pybitcoin.types import Address
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
        for i in range(len(data['mintRequests'])):
            data['mintRequests'][i]['destinationAddress'] = Address(
                address=data['mintRequests'][i]['destinationAddress'],
                network=Ethereum()
            )
        for i in range(len(data['burnRequests'])):
            data['burnRequests'][i]['destinationAddress'] = Address(
                address=data['burnRequests'][i]['destinationAddress'],
                network=self._network
            )

        return StatusModel(**data)
