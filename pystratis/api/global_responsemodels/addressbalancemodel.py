from pydantic import Field
from pystratis.core.types import Address, Money
from pystratis.core import CoinType
from pystratis.api import Model


class AddressBalanceModel(Model):
    """A pydantic model for an address balance."""
    address: Address
    """The address."""
    coin_type: CoinType = Field(alias='coinType')
    """The coin type."""
    amount_confirmed: Money = Field(alias='amountConfirmed')
    """The confirmed amount."""
    amount_unconfirmed: Money = Field(alias='amountUnconfirmed')
    """The unconfirmed amount."""
    spendable_amount: Money = Field(alias='spendableAmount')
    """The spendable amount."""
