from typing import Optional
from pydantic import Field, SecretStr
from pystratis.api import Model
from pystratis.core.types import Address


# noinspection PyUnresolvedReferences
class JoinFederationRequest(Model):
    """A request model for the collateral/joinfederation endpoint.

    Args:
        collateral_address (Address): The collateral address.
        collateral_wallet_name (str): The collateral wallet name.
        collateral_wallet_password (SecretStr): The collateral wallet password.
        wallet_password (SecretStr): The wallet password.
        wallet_name (str): The wallet name.
        wallet_account (str, optional):  The wallet account. Default='account 0'.
    """
    collateral_address: Address = Field(alias='collateralAddress')
    collateral_wallet_name: str = Field(alias='collateralWalletName')
    collateral_wallet_password: SecretStr = Field(alias='collateralWalletPassword')
    wallet_password: SecretStr = Field(alias='walletPassword')
    wallet_name: str = Field(alias='walletName')
    wallet_account: Optional[str] = Field(default='account 0', alias='walletAccount')
