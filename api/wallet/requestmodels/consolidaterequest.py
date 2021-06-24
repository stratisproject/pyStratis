from typing import Optional
from pydantic import Field, SecretStr, conint
from pybitcoin import Model
from pybitcoin.types import Address


class ConsolidateRequest(Model):
    """A request model for the wallet/consolidate endpoint.

    Args:
        wallet_password: SecretStr = Field(alias='walletPassword')
        wallet_name: str = Field(alias='walletName')
        wallet_account: Optional[str] = Field(default='account 0', alias='walletAccount')
        destination_address: Address = Field(alias='destinationAddress')
        utxo_value_threshold_in_satoshis: conint(ge=1_0000_0000) = Field(default=1_0000_0000, alias='utxoValueThreshold')
        broadcast: Optional[bool] = False
    """
    wallet_password: SecretStr = Field(alias='walletPassword')
    wallet_name: str = Field(alias='walletName')
    wallet_account: Optional[str] = Field(default='account 0', alias='walletAccount')
    destination_address: Address = Field(alias='destinationAddress')
    utxo_value_threshold_in_satoshis: conint(ge=1_0000_0000) = Field(default=1_0000_0000, alias='utxoValueThreshold')
    broadcast: Optional[bool] = False
