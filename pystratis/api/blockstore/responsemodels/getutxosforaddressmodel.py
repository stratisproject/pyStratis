from typing import List
from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import Money
from .utxomodel import UTXOModel


class GetUTXOsForAddressModel(Model):
    """A pydantic model representing unspent transaction outputs (utxos) and balance for a given address."""
    balance: Money
    """The address balance."""
    utxos: List[UTXOModel]
    """A list of utxos for the given address."""
