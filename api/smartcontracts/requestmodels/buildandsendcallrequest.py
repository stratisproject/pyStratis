from typing import Optional, List
from pydantic import Field, SecretStr, validator
from pybitcoin import Model, Outpoint, SmartContractParameter
from pybitcoin.types import Address, Money


class BuildAndSendCallContractTransactionRequest(Model):
    """A BuildAndSendCallContractTransactionRequest."""
    wallet_name: str = Field(alias='walletName')
    account_name: Optional[str] = Field(default='account 0', alias='accountName')
    outpoints: List[Outpoint]
    contract_address: Address = Field(alias='contractAddress')
    method_name: str = Field(alias='methodName')
    amount: Money
    fee_amount: Money = Field(alias='feeAmount')
    password: SecretStr
    gas_price: Money = Field(alias='gasPrice')
    gas_limit: Money = Field(alias='gasLimit')
    sender: Address
    parameters: Optional[List[SmartContractParameter]]

    # noinspection PyMethodParameters
    @validator('fee_amount', always=True)
    def check_fee_too_high(cls, v, values):
        if v > Money(1):
            raise ValueError('Fee should not be more than 1. Check parameters.')
        if v > values['amount']:
            raise ValueError('Fee should not be greater than amount.')
        return v
