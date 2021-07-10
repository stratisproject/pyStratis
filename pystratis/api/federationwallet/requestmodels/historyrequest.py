from pydantic import Field, conint
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class HistoryRequest(Model):
    """A request model for the federationwallet/history endpoint.

    Args:
        max_entries_to_return (conint(ge=0)): The maximum number of history entries to return.
    """
    max_entries_to_return: conint(ge=0) = Field(alias='maxEntriesToReturn')
