from typing import Optional
from pydantic import conint
from pybitcoin import Model


class GetRequest(Model):
    """A GetRequest."""
    skip: Optional[conint(ge=0)]
    take: Optional[conint(ge=0)]
