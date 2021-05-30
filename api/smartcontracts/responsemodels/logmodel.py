from typing import List
from pydantic import Field
from pybitcoin import Model, Address


class LogModel(Model):
    """A LogModel."""
    address: Address = Field(alias='Address')
    topics: List[str] = Field(alias='Topics')
    data: str = Field(alias='Data')
