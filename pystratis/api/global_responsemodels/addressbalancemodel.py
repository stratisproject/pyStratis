from pydantic import Field
from pystratis.core.types import Address, Money
from pystratis.core import CoinType
from pystratis.api import Model


class AddressBalanceModel(Model):
    """An AddressBalanceModel."""
    address: Address
    coin_type: CoinType = Field(alias='coinType')
    amount_confirmed: Money = Field(alias='amountConfirmed')
    amount_unconfirmed: Money = Field(alias='amountUnconfirmed')
    spendable_amount: Money = Field(alias='spendableAmount')
