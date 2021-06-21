from typing import List, Optional
from pybitcoin import Model
from pybitcoin.types import Address


class LogModel(Model):
    """A LogModel."""
    address: Optional[Address]
    topics: Optional[List[str]]
    data: Optional[str]
    log: Optional[dict]
