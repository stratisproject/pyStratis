from typing import List, Optional
from pystratis.api import Model
from pystratis.core.types import Address


class LogModel(Model):
    """A LogModel."""
    address: Optional[Address]
    topics: Optional[List[str]]
    data: Optional[str]
    log: Optional[dict]
