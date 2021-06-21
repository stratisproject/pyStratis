from typing import Optional, List
from pydantic import Field, conint
from pybitcoin import Model, SmartContractParameter
from pybitcoin.types import Address, Money


class LocalCallContractTransactionRequest(Model):
    """A LocalCallContractTransactionRequest."""
    contract_address: Address = Field(alias='contractAddress')
    method_name: str = Field(alias='methodName')
    amount: Money
    gas_price: conint(ge=100, le=10000) = Field(alias='gasPrice')
    gas_limit: conint(ge=12000, le=250000) = Field(alias='gasLimit')
    sender: Address
    parameters: Optional[List[SmartContractParameter]]
