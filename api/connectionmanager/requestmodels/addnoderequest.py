from pydantic import validator
from pybitcoin import Model


class AddNodeRequest(Model):
    """A request model for the connectionmanager/addnode endpoint.

    Args:
        endpoint (str): The endpoint.
        command (str): Allowed commands [add, remove, onetry]
    """
    endpoint: str
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
