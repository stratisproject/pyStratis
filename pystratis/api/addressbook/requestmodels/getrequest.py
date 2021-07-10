from typing import Optional
from pydantic import conint
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class GetRequest(Model):
    """A request model for the addressbook endpoint.

    Args:
        skip (conint(ge=0), optional): The number of items to skip.
        take (conint(ge=0), optional): The number of items to take.

    Notes:
        If skip and take are not provided, the entire addressbook is returned.
    """
    skip: Optional[conint(ge=0)]
    take: Optional[conint(ge=0)]
