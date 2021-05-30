from pydantic import Field
from pybitcoin import Model


class AsyncLoopsModel(Model):
    """An AsyncLoopsModel."""
    loop_name: str = Field(alias='loopName')
    status: str
