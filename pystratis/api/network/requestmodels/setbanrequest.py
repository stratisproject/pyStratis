from pydantic import Field, conint, validator
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class SetBanRequest(Model):
    """A request model for the network/setban endpoint.

    Args:
        ban_command (str): Allowed commands [add, remove].
        ban_duration_seconds (conint(ge=0)): The ban duration in seconds.
        peer_address (str): The peer address to ban/unban.
    """
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
