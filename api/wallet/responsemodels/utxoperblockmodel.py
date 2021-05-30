from pybitcoin import Model
from pydantic import Field, conint


class UtxoPerBlockModel(Model):
    """An UtxoPerBlockModel."""
    utxo_per_block: conint(ge=0) = Field(alias='UtxoPerBlock')
    count: conint(ge=0) = Field(alias='Count')
