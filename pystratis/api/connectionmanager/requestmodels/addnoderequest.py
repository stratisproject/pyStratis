from pydantic import validator, Field
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class AddNodeRequest(Model):
    """A request model for the connectionmanager/addnode endpoint.

    Args:
        ipaddr (str): The endpoint.
        command (str): Allowed commands [add, remove, onetry]
    """
    ipaddr: str = Field(alias='endpoint')
    command: str

    # noinspection PyMethodParameters,PyUnusedLocal
    @validator('command')
    def validate_command(cls, v, values):
        allowed = [
            'add',
            'remove',
            'onetry'
        ]
        if v not in allowed:
            raise ValueError(f'Invalid command. Must be: {allowed}')
        return v
