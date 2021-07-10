from typing import Optional, List
from pydantic import Field, conint
from pystratis.api import Model
from pystratis.core import SmartContractParameter
from pystratis.core.types import Address, Money


# noinspection PyUnresolvedReferences
class LocalCallContractTransactionRequest(Model):
    """A request model for the smartcontracts/local-call endpoint.

    Args:
        contract_address (Address): The smart contract address being called.
        method_name (str): The smart contract method being called.
        amount (Money): The amount being sent.
        gas_price (int): The amount of gas being used in satoshis.
        gas_limit (int): The maximum amount of gas that can be used in satoshis.
        sender (Address): The address of the sending address.
        parameters (List[SmartContractParameters], optional): A list of parameters for the smart contract.
    """
    contract_address: Address = Field(alias='contractAddress')
    method_name: str = Field(alias='methodName')
    amount: Money
    gas_price: conint(ge=100, le=10000) = Field(alias='gasPrice')
    gas_limit: conint(ge=12000, le=250000) = Field(alias='gasLimit')
    sender: Address
    parameters: Optional[List[SmartContractParameter]]
