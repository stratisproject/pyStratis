from typing import List, Optional
from pydantic import Field
from pystratis.api.model import Model
from pystratis.core.types import Money
from pystratis.core import CoinType
from .addressmodel import AddressModel


class AccountBalanceModel(Model):
    """An AccountBalanceModel"""
    account_name: Optional[str] = Field(alias='accountName')
    account_hd_path: Optional[str] = Field(alias='accountHdPath')
    coin_type: CoinType = Field(alias='coinType')
    amount_confirmed: Money = Field(alias='amountConfirmed')
    amount_unconfirmed: Money = Field(alias='amountUnconfirmed')
    spendable_amount: Optional[Money] = Field(alias='spendableAmount')
    addresses: Optional[List[AddressModel]]
