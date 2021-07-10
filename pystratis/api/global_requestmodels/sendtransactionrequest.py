from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import hexstr


# noinspection PyUnresolvedReferences
class SendTransactionRequest(Model):
    """A request model for multiple api endpoints.

    Args:
        transaction_hex (hexstr): The hexified transaction.
    """
    transaction_hex: hexstr = Field(alias='hex')
