from typing import Optional, List
from pydantic import Field, SecretStr, validator, conint
from pystratis.api import Model
from pystratis.core import Outpoint, SmartContractParameter
from pystratis.core.types import Address, Money


# noinspection PyUnresolvedReferences
class BuildAndSendCallContractTransactionRequest(Model):
    """A request model for the smartcontracts/build-and-send-call endpoint.

    Args:
        wallet_name (str): The wallet name.
        account_name (str, optional): The wallet name. Default='account 0'
        outpoints (List[Outpoint], optional): A list of the outpoints used to construct the transactation.
        contract_address (Address): The smart contract address being called.
        method_name (str): The method name being called.
        amount (Money, optional): The amount being sent.
        fee_amount (Money): The fee amount.
        password (SecretStr): The password.
        gas_price (int): The amount of gas being used in satoshis.
        gas_limit (int): The maximum amount of gas that can be used in satoshis.
        sender (Address): The address of the sending address.
        parameters (List[SmartContractParameters], optional): A list of parameters for the smart contract.
    """
    wallet_name: str = Field(alias='walletName')
    account_name: Optional[str] = Field(default='account 0', alias='accountName')
    outpoints: Optional[List[Outpoint]]
    contract_address: Address = Field(alias='contractAddress')
    method_name: str = Field(alias='methodName')
    amount: Money
    fee_amount: Money = Field(alias='feeAmount')
    password: SecretStr
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
