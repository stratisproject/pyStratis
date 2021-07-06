from typing import List, Optional
from pystratis.api import Model
from pystratis.core.types import Address


class LogModel(Model):
    """A pydantic model of a smart contact log."""
    address: Address
    """The smart contact address."""
    topics: Optional[List[str]]
    """A list of topics."""
    data: Optional[str]
    """Log data."""
    log: Optional[dict]
    """Log dict object response."""
