from pydantic import validator
from pybitcoin import Model


class AddNodeRequest(Model):
    """An AddNodeRequest."""
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
