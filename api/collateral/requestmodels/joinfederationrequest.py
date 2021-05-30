from typing import Optional
from pydantic import Field, SecretStr
from pybitcoin import Address, Model


class JoinFederationRequest(Model):
    """A JoinFederationRequest."""
    collateral_address: Address = Field(alias='collateralAddress')
    collateral_wallet_name: str = Field(alias='collateralWalletName')
    collateral_wallet_password: SecretStr = Field(alias='collateralWalletPassword')
    wallet_password: SecretStr = Field(alias='walletPassword')
    wallet_name: str = Field(alias='walletName')
    wallet_account: Optional[str] = Field(default='account 0', alias='walletAccount')
