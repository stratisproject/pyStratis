from pydantic import Field, conint
from pybitcoin import Model


class SetBanRequest(Model):
    """A SetBanRequest."""
    ban_command: str = Field(alias='banCommand')
    ban_duration_seconds: conint(ge=0) = Field('banDurationSeconds')
    peer_address: str = Field(alias='peerAddress')
