from api import APIRequest, EndpointRegister, endpoint
from api.interop.responsemodels import *


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

        return StatusModel(**data)
