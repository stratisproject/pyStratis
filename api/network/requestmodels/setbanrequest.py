from pydantic import Field, conint, validator
from pybitcoin import Model


class SetBanRequest(Model):
    """A SetBanRequest."""
    ban_command: str = Field(alias='banCommand')
    ban_duration_seconds: conint(ge=0) = Field(alias='banDurationSeconds')
    peer_address: str = Field(alias='peerAddress')

    # noinspection PyMethodParameters,PyUnusedLocal
    @validator('ban_command')
    def validate_ban_command(cls, v, values):
        allowed = [
            'add',
            'remove'
        ]
        if v not in allowed:
            raise ValueError(f'Invalid ban command. Must be: {allowed}')
        return v
