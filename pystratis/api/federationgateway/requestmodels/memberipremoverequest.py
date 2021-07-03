from pystratis.api import Model
from pydantic import Field


class MemberIPRemoveRequest(Model):
    """A request model for the federationgateway/member/ip/remove endpoint.

    Args:
        ipaddr (str): The endpoint.
    """
    ipaddr: str = Field(alias='endpoint')
