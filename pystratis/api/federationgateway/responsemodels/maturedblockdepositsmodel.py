from typing import List
from pydantic import Field
from pystratis.api import Model
from pystratis.core import Deposit
from pystratis.api.global_responsemodels import MaturedBlockInfoModel


class MaturedBlockDepositsModel(Model):
    """A pydantic model for matured block deposits."""
    deposits: List[Deposit] = Field(alias='deposits')
    """A list of deposits."""
    block_info: MaturedBlockInfoModel = Field(alias='blockInfo')
    """Matured block information model."""
