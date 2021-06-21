from api import APIRequest, EndpointRegister, endpoint


class Dashboard(APIRequest, metaclass=EndpointRegister):
    route = '/api/dashboard'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/stats')
    def stats(self, **kwargs) -> str:
        """Gets the dashboard of node stats.

        Args:
            **kwargs:

        Returns:
            str

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return data

    @endpoint(f'{route}/asyncloopsstats')
    def asyncloops_stats(self, **kwargs) -> str:
        """Gets the dashboard of asyncloop stats.

        Args:
            **kwargs:

        Returns:
            str

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return data
