from pydantic import Field
from pystratis.api import Model


class AsyncLoopsModel(Model):
    """A pydantic model for async loops."""
    loop_name: str = Field(alias='loopName')
    """The loop name."""
    status: str
    """The loop status."""
