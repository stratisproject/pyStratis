from typing import Optional
from pybitcoin import Model
from pydantic import Field, conint


class UtxoPerTransactionModel(Model):
    """An UtxoPerTransactionModel."""
    utxo_per_transaction: Optional[conint(ge=0)] = Field(alias='UtxoPerTransaction')
    count: Optional[conint(ge=0)] = Field(alias='Count')
