from pydantic import Field
from pystratis.api import Model


class FederationMemberConnectionInfoModel(Model):
    """A pydantic model for federation member connections."""
    federation_member_ip: str = Field(alias='federationMemberIp')
    """The federation member ip."""
    is_connected: bool = Field(alias='isConnected')
    """If true, federation member is connected."""
    is_banned: bool = Field(alias='isBanned')
    """If true, federation member is banned."""
