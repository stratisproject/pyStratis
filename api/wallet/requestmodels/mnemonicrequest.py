from pydantic import Field, conint
from pybitcoin import Model


class MnemonicRequest(Model):
    """A MnemonicRequest."""
    language: str
    word_count: conint(ge=0) = Field(alias='wordCount')
