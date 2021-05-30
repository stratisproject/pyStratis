from pydantic import SecretStr, Field, conint
from pybitcoin import Model
from pybitcoin.types import Money


class SplitCoinsRequest(Model):
    """A SplitCoinsRequest."""
    wallet_name: str = Field(alias='walletName')
    account_name: str = Field(default='account 0', alias='accountName')
    wallet_password: SecretStr = Field(alias='walletPassword')
    total_amount_to_split: Money
    utxos_count: conint(ge=0)
