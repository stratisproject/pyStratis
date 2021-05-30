from pybitcoin import Model
from pydantic import Field, conint


class UtxoPerTransactionModel(Model):
    """An UtxoPerTransactionModel."""
    utxo_per_transaction: conint(ge=0) = Field(alias='UtxoPerTransaction')
    count: conint(ge=0) = Field(alias='Count')
