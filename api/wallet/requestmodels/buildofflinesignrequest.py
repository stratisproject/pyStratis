from typing import Optional, List
from pydantic import Field, validator
from pybitcoin import Model, Outpoint, Recipient
from pybitcoin.types import Address, Money


class BuildOfflineSignRequest(Model):
    """A BuildOfflineSignRequest."""
    fee_amount: Money = Field(alias='feeAmount')
    wallet_name: str = Field(alias='walletName')
    account_name: Optional[str] = Field(default='account 0', alias='accountName')
    outpoints: List[Outpoint]
    recipients: List[Recipient]
    op_return_data: Optional[str] = Field(alias='opReturnData')
    op_return_amount: Optional[Money] = Field(alias='opReturnAmount')
    fee_type: Optional[str] = Field(alias='feeType')
    allow_unconfirmed: Optional[bool] = Field(default=False, alias='allowUnconfirmed')
    shuffle_outputs: Optional[bool] = Field(default=False, alias='shuffleOutputs')
    change_address: Optional[Address] = Field(alias='changeAddress')

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
        if v is not None and values['fee_amount'] is not None:
            raise ValueError('Both fee_type and fee_amount cannot be set.')
        return v

    # noinspection PyMethodParameters,PyUnusedLocal
    @validator('fee_amount', always=True)
    def check_fee_too_high(cls, v, values):
        if v is not None:
            if v > Money(1):
                raise ValueError('Fee should not be more than 1. Check parameters.')
        return v
