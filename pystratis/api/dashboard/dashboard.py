from pystratis.api import APIRequest, EndpointRegister, endpoint


class Dashboard(APIRequest, metaclass=EndpointRegister):
    """Implements the dashboard api endpoints."""

    route = '/api/dashboard'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/stats')
    def stats(self, **kwargs) -> str:
        """Gets the dashboard of node stats.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            str: The dashboard text.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return data

    @endpoint(f'{route}/asyncloopsstats')
    def asyncloops_stats(self, **kwargs) -> str:
        """Gets the dashboard of asyncloop stats.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            str: The async loop stats.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return data
