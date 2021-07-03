from typing import List, Optional
from pydantic import Field
from pystratis.api import Model
from pystratis.core import Deposit
from pystratis.api.global_responsemodels import MaturedBlockInfoModel


class MaturedBlockDepositsModel(Model):
    """A MaturedBlockDepositsModel."""
    deposits: Optional[List[Deposit]] = Field(alias='deposits')
    block_info: Optional[MaturedBlockInfoModel] = Field(alias='blockInfo')
