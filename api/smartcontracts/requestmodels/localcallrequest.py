from typing import Optional, List
from pydantic import Field
from pybitcoin import Model, SmartContractParameter
from pybitcoin.types import Address, Money


class LocalCallContractTransactionRequest(Model):
    """A LocalCallContractTransactionRequest."""
    contract_address: Address = Field(alias='contractAddress')
    method_name: str = Field(alias='methodName')
    amount: Money
    gas_price: Money = Field(alias='gasPrice')
    gas_limit: Money = Field(alias='gasLimit')
    sender: Address
    parameters: Optional[List[SmartContractParameter]]
