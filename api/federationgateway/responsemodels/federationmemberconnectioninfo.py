from typing import Optional
from pydantic import Field
from pybitcoin import Model


class FederationMemberConnectionInfo(Model):
    """A FederationMemberConnectionInfo."""
    federation_member_ip: Optional[str] = Field(alias='federationMemberIp')
    is_connected: Optional[bool] = Field(alias='isConnected')
    is_banned: Optional[bool] = Field(alias='isBanned')
