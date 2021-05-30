from pydantic import Field
from pybitcoin import Model


class GeneralInfoRequest(Model):
    """A GeneralInfoRequest."""
    name: str = Field(alias='Name')
