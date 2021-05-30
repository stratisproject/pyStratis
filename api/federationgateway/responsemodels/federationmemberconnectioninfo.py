from pydantic import Field
from pybitcoin import Model


class FederationMemberConnectionInfo(Model):
    """A FederationMemberConnectionInfo."""
    federation_member_ip: str = Field(alias='federationMemberIp')
    is_connected: bool = Field(alias='isConnected')
    is_banned: bool = Field(alias='isBanned')
