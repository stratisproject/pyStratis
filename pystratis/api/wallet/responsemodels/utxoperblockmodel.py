from typing import Optional
from pystratis.core import Model
from pydantic import Field, conint


class UtxoPerBlockModel(Model):
    """An UtxoPerBlockModel."""
    utxo_per_block: Optional[conint(ge=0)] = Field(alias='utxoPerBlock')
    count: Optional[conint(ge=0)] = Field(alias='Count')
