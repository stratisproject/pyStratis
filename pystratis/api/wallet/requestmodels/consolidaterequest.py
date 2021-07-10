from typing import Optional
from pydantic import Field, SecretStr, conint
from pystratis.api import Model
from pystratis.core.types import Address


# noinspection PyUnresolvedReferences
class ConsolidateRequest(Model):
    """A request model for the wallet/consolidate endpoint.

    Args:
        wallet_password (str): The wallet password.
        wallet_name (str): The wallet name.
        wallet_account (str, optional): The account name. Default='account 0'.
        destination_address (Address): The destination address.
        utxo_value_threshold_in_satoshis (conint(ge=1_0000_0000)): The threshold where amounts below this amount will be consolidated.
        broadcast (bool, optional): If True, broadcast consolidation transaction. Default=False.
    """
    wallet_password: SecretStr = Field(alias='walletPassword')
    wallet_name: str = Field(alias='walletName')
    wallet_account: Optional[str] = Field(default='account 0', alias='walletAccount')
    destination_address: Address = Field(alias='destinationAddress')
    utxo_value_threshold_in_satoshis: conint(ge=1_0000_0000) = Field(default=1_0000_0000, alias='utxoValueThreshold')
    broadcast: Optional[bool] = False
