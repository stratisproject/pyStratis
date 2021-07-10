from typing import Optional
from pydantic import Field, validator
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class MaxBalanceRequest(Model):
    """A request model for the wallet/maxbalance endpoint.

    Args:
        wallet_name (str): The wallet name.
        account_name (str, optional): The account name. Default='account 0'.
        fee_type (str): The fee type. Allowed [low, medium, high]
        allow_unconfirmed (bool, optional): If True, allow unconfirmed utxo in request. Default=False.
    """
    wallet_name: str = Field(alias='WalletName')
    account_name: Optional[str] = Field(default='account 0', alias='AccountName')
    fee_type: str = Field(alias='FeeType')
    allow_unconfirmed: Optional[bool] = Field(default=False, alias='AllowUnconfirmed')

    # noinspection PyMethodParameters,PyUnusedLocal
    @validator('fee_type')
    def validate_fee_type(cls, v, values):
        allowed = [
            'low',
            'medium',
            'high'
        ]
        if v is not None and v not in allowed:
            raise ValueError(f'Invalid command. Must be: {allowed}')
        return v
