from typing import List, Optional
from pydantic import Field
from pybitcoin import Model, Deposit, MaturedBlockInfoModel


class MaturedBlockDepositsModel(Model):
    """A MaturedBlockDepositsModel."""
    deposits: Optional[List[Deposit]] = Field(alias='deposits')
    block_info: Optional[MaturedBlockInfoModel] = Field(alias='blockInfo')
