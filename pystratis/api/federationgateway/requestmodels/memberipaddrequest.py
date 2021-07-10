from pystratis.api import Model
from pydantic import Field


# noinspection PyUnresolvedReferences
class MemberIPAddRequest(Model):
    """A request model for the federationgateway/member/ip/add endpoint.

    Args:
        ipaddr (str): The endpoint.
    """
    ipaddr: str = Field(alias='endpoint')
