from typing import List, Optional
from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import Address


class LogModel(Model):
    """A LogModel."""
    address: Optional[Address] = Field(alias='Address')
    topics: Optional[List[str]] = Field(alias='Topics')
    data: Optional[str] = Field(alias='Data')
