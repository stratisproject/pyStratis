from typing import List, Optional
from pydantic import Field
from pystratis.api.model import Model
from pystratis.core.types import Money
from pystratis.core import CoinType
from .addressmodel import AddressModel


class AccountBalanceModel(Model):
    """A pydantic model for account balance."""
    account_name: Optional[str] = Field(alias='accountName')
    """The account name. Will be None for multisig."""
    account_hd_path: Optional[str] = Field(alias='accountHdPath')
    """The account HD path. Will be None for multisig."""
    coin_type: CoinType = Field(alias='coinType')
    """The coin type."""
    amount_confirmed: Money = Field(alias='amountConfirmed')
    """The amount confirmed."""
    amount_unconfirmed: Money = Field(alias='amountUnconfirmed')
    """The amount unconfirmed."""
    spendable_amount: Optional[Money] = Field(alias='spendableAmount')
    """The spendable amount. Will be None for multisig."""
    addresses: Optional[List[AddressModel]]
    """A list of addresses."""
