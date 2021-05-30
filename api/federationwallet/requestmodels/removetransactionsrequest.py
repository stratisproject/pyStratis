from typing import Optional
from pydantic import Field
from pybitcoin import Model


class RemoveTransactionsRequest(Model):
    """A RemoveTransactionsRequest."""
    resync: Optional[bool] = Field(default=True, alias='ReSync')
