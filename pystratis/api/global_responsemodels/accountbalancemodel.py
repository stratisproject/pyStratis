from typing import List, Optional
from pydantic import Field
from pystratis.api.model import Model
from pystratis.core.types import Money
from pystratis.core import CoinType
from .addressmodel import AddressModel


class AccountBalanceModel(Model):
    """A pydantic model for account balance."""
    account_name: str = Field(alias='accountName')
    """The account name."""
    account_hd_path: str = Field(alias='accountHdPath')
    """The account HD path."""
    coin_type: CoinType = Field(alias='coinType')
    """The coin type."""
    amount_confirmed: Money = Field(alias='amountConfirmed')
    """The amount confirmed."""
    amount_unconfirmed: Money = Field(alias='amountUnconfirmed')
    """The amount unconfirmed."""
    spendable_amount: Money = Field(alias='spendableAmount')
    """The spendable amount."""
    addresses: Optional[List[AddressModel]]
    """A list of addresses."""
