from typing import List
from pydantic import Field
from pybitcoin import Model, Deposit, MaturedBlockInfoModel


class MaturedBlockDepositsModel(Model):
    """A MaturedBlockDepositsModel."""
    deposits: List[Deposit] = Field(alias='Deposits')
    block_info: MaturedBlockInfoModel = Field(alias='BlockInfo')
