from typing import Optional
from pydantic import Field, SecretStr
from pybitcoin import Address, Model


class ConsolidateRequest(Model):
    """A ConsolidateRequest."""
    wallet_password: SecretStr = Field(alias='walletPassword')
    wallet_name: str = Field(alias='walletName')
    wallet_account: Optional[str] = Field(default='account 0', alias='walletAccount')
    destination_address: Address = Field(alias='destinationAddress')
    utxo_value_threshold: Optional[str] = Field(default='0', alias='utxoValueThreshold')
    broadcast: Optional[bool] = False
