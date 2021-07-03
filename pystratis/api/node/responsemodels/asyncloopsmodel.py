from typing import Optional
from pydantic import Field
from pystratis.core import Model


class AsyncLoopsModel(Model):
    """An AsyncLoopsModel."""
    loop_name: Optional[str] = Field(alias='loopName')
    status: Optional[str]
