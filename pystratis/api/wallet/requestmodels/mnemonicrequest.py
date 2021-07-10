from pydantic import Field, conint
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class MnemonicRequest(Model):
    """A request model for the wallet/mnemonic endpoint.

    Args:
        language (str): A language used to generate mnemonic.
        word_count (conint(ge=0)): Count of words needs to be generated.
    """
    language: str = Field(default='English')
    word_count: conint(ge=0) = Field(default=12, alias='wordCount')
