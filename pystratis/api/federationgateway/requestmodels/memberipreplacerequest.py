from pystratis.api import Model
from pydantic import Field


# noinspection PyUnresolvedReferences
class MemberIPReplaceRequest(Model):
    """A request model for the federationgateway/member/ip/replace endpoint.

    Args:
        endpointtouse (str): The new endpoint.
        endpoint (str): The endpoint being replaced.
    """
    ipaddrtouse: str = Field(alias='endpointtouse')
    ipaddr: str = Field(alias='endpoint')
