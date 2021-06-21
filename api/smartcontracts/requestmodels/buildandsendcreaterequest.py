from typing import Optional, List
from pydantic import Field, SecretStr, validator, conint
from pybitcoin import Model, Outpoint, SmartContractParameter
from pybitcoin.types import Address, Money, hexstr


class BuildAndSendCreateContractTransactionRequest(Model):
    """A BuildAndSendCreateContractTransactionRequest."""
    wallet_name: str = Field(alias='walletName')
    account_name: Optional[str] = Field(default='account 0', alias='accountName')
    outpoints: Optional[List[Outpoint]]
    amount: Money
    fee_amount: Money = Field(alias='feeAmount')
    password: SecretStr
    contract_code: hexstr = Field(alias='contractCode')
    gas_price: conint(ge=100, le=10000) = Field(alias='gasPrice')
    gas_limit: conint(ge=12000, le=250000) = Field(alias='gasLimit')
    sender: Address
    parameters: Optional[List[SmartContractParameter]]

    # noinspection PyMethodParameters,PyUnusedLocal
    @validator('fee_amount', always=True)
    def check_fee_too_high(cls, v, values):
        if v > Money(1):
            raise ValueError('Fee should not be more than 1. Check parameters.')
        return v
