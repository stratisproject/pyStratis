from typing import Optional, List
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
        return v

    class Config:
        json_encoders = {
            Address: lambda v: str(v),
            bool: lambda v: str(v).lower(),
            SecretStr: lambda v: v.get_secret_value(),
            Money: lambda v: str(v),
            List[Recipient]: lambda v: [x.json() for x in v],
            List[Outpoint]: lambda v: [x.json() for x in v],
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super(BuildTransactionRequest, self).json(exclude_none=True, by_alias=True)
