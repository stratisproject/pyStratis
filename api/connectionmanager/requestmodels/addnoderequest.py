from pydantic import validator
from pybitcoin import Model


class AddNodeRequest(Model):
    """An AddNodeRequest."""
    endpoint: str
    command: str

    # noinspection PyMethodParameters,PyUnusedLocal
    @validator('command')
    def validate_vote_type(cls, v, values):
        allowed_methods = [
            'add',
            'remove',
            'onetry'
        ]
        if v not in allowed_methods:
            raise ValueError(f'Invalid command. Must be: {allowed_methods}')
        return v
