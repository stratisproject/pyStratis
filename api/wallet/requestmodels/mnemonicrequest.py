from pydantic import Field, conint
from pybitcoin import Model


class MnemonicRequest(Model):
    """A MnemonicRequest."""
    language: str = Field(default='English')
    word_count: conint(ge=0) = Field(default=12, alias='wordCount')
