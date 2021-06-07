from typing import Optional
from pydantic import Field
from pybitcoin import Model


class BannedPeerModel(Model):
    """A BannedPeerModel."""
    endpoint: Optional[str] = Field(alias='EndPoint')
    ban_until: Optional[str] = Field(alias='BanUntil')
    ban_reason: Optional[str] = Field(alias='BanReason')
