from typing import Optional, List
from pydantic import Field, SecretStr, validator
from pybitcoin import Model, Outpoint, SmartContractParameter
from pybitcoin.types import Address, Money


class BuildCreateContractTransactionRequest(Model):
    """A BuildCreateContractTransactionRequest."""
    wallet_name: str = Field(alias='walletName')
    account_name: Optional[str] = Field(default='account 0', alias='accountName')
    outpoints: List[Outpoint]
    amount: Money
    fee_amount: Money = Field(alias='feeAmount')
    password: SecretStr
    contract_code: str = Field(alias='contractCode')
    gas_price: Money = Field(alias='gasPrice')
    gas_limit: Money = Field(alias='gasLimit')
    sender: Address
    parameters: Optional[List[SmartContractParameter]]

    # noinspection PyMethodParameters
    @validator('fee_amount', always=True)
    def check_fee_too_high(cls, v, values):
        if v is not None:
            if v > Money(1):
                raise ValueError('Fee should not be more than 1. Check parameters.')
            if v > values['amount']:
                raise ValueError('Fee should not be greater than amount.')
        return v
