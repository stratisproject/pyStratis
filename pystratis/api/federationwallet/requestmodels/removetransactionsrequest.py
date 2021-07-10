from typing import Optional
from pydantic import Field
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class RemoveTransactionsRequest(Model):
    """A request model for the federationwallet/remove-transactions endpoint.

    Args:
        resync (bool, optional): A flag to resync the wallet after transactions are removed. Default=True.
    """
    resync: Optional[bool] = Field(default=True, alias='ReSync')
