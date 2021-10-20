from pydantic import Field
from typing import Optional, List
from pystratis.api import Model
from pystratis.core.types import Money
from .utxomodel import UTXOModel


class GetUTXOModel(Model):
    """A pydantic model for the unity3d getuxtosforaddress endpoint."""
    balance: Money = Field(alias='balanceSat')
    """The balance in Money units."""
    utxos: List[UTXOModel] = Field(alias='utxOs')
    """The list of utxos."""
    reason: Optional[str]
    """The message, if failed."""
