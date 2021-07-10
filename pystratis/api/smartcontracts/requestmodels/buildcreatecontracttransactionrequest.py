from typing import Optional, List
from pydantic import Field, SecretStr, validator, conint
from pystratis.api import Model
from pystratis.core import Outpoint, SmartContractParameter
from pystratis.core.types import Address, Money, hexstr


# noinspection PyUnresolvedReferences
class BuildCreateContractTransactionRequest(Model):
    """A request model for the smartcontracts/build-create endpoint.

    Args:
        wallet_name (str): The wallet name.
        account_name (str, optional): The wallet name. Default='account 0'
        outpoints (List[Outpoint], optional): A list of the outpoints used to construct the transactation.
        amount (Money, optional): The amount being sent.
        fee_amount (Money): The fee amount.
        password (SecretStr): The password.
        contract_code (hexstr): The smart contract code hexstring.
        gas_price (int): The amount of gas being used in satoshis.
        gas_limit (int): The maximum amount of gas that can be used in satoshis.
        sender (Address): The address of the sending address.
        parameters (List[SmartContractParameters], optional): A list of parameters for the smart contract.
    """
    wallet_name: str = Field(alias='walletName')
    account_name: Optional[str] = Field(default='account 0', alias='accountName')
    outpoints: Optional[List[Outpoint]]
    amount: Optional[Money]
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
        if v is not None:
            if v > Money(1):
                raise ValueError('Fee should not be more than 1. Check parameters.')
        return v
