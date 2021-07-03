from typing import Optional
from pystratis.api import Model
from pydantic import Field, conint


class UtxoPerTransactionModel(Model):
    """An UtxoPerTransactionModel."""
    utxo_per_transaction: Optional[conint(ge=0)] = Field(alias='utxoPerTransaction')
    count: Optional[conint(ge=0)] = Field(alias='Count')
