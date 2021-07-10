from pydantic import SecretStr, Field, conint
from pystratis.api import Model
from pystratis.core.types import Money


# noinspection PyUnresolvedReferences
class SplitCoinsRequest(Model):
    """A request model for the wallet/splitcoins endpoint.

    Args:
        wallet_name (str): The wallet name.
        account_name (str, optional): The account name. Default='account 0'.
        wallet_password (str): The wallet password.
        total_amount_to_split (Money): The total amount to split.
        utxos_count (conint(ge=2)): The number of utxos to create. (Must be greater than 2).
    """
    wallet_name: str = Field(alias='walletName')
    account_name: str = Field(default='account 0', alias='accountName')
    wallet_password: SecretStr = Field(alias='walletPassword')
    total_amount_to_split: Money = Field(alias='totalAmountToSplit')
    utxos_count: conint(ge=2) = Field(alias='utxosCount')
