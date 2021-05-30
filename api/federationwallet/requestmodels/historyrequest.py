from pydantic import Field, conint
from pybitcoin import Model


class HistoryRequest(Model):
    """A HistoryRequest."""
    max_entries_to_return: conint(ge=0) = Field(alias='maxEntriesToReturn')
