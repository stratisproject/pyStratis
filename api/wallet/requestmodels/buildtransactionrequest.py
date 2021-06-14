from typing import Optional, List
import json
from pydantic import Field, SecretStr, validator
from pybitcoin import Model, Outpoint, Recipient
from pybitcoin.types import Address, Money


class BuildTransactionRequest(Model):
    """A BuildTransactionRequest."""
    fee_amount: Optional[Money] = Field(alias='feeAmount')
    password: SecretStr
    segwit_change_address: Optional[bool] = Field(default=False, alias='segwitChangeAddress')
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

    def json(self, *args, **kwargs) -> str:
        data = super(BuildTransactionRequest, self).dict(exclude_none=True, by_alias=True)
        data['password'] = data['password'].get_secret_value()
        for i in range(len(data['outpoints'])):
            data['outpoints'][i]['transactionId'] = str(data['outpoints'][i]['transactionId'])
        for i in range(len(data['recipients'])):
            if 'destinationAddress' in data['recipients'][i] and data['recipients'][i]['destinationAddress'] is not None:
                data['recipients'][i]['destinationAddress'] = str(data['recipients'][i]['destinationAddress'])
            if 'destinationScript' in data['recipients'][i] and data['recipients'][i]['destinationScript'] is not None:
                data['recipients'][i]['destinationScript'] = str(data['recipients'][i]['destinationScript'])
            data['recipients'][i]['amount'] = data['recipients'][i]['amount'].to_coin_unit()
        if 'opReturnAmount' in data and data['opReturnAmount'] is not None:
            data['opReturnAmount'] = data['opReturnAmount'].to_coin_unit()
        if 'changeAddress' in data and data['changeAddress'] is not None:
            data['changeAddress'] = str(data['changeAddress'])
        if 'feeAmount' in data and data['feeAmount'] is not None:
            data['feeAmount'] = data['feeAmount'].to_coin_unit()

        return json.dumps(data)
