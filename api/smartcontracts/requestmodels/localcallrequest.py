from typing import Optional, List
from pydantic import Field
from pybitcoin import Address, Model
from pybitcoin.types import Money


class LocalCallContractTransactionRequest(Model):
    """A LocalCallContractTransactionRequest."""
    contract_address: Address = Field(alias='contractAddress')
    method_name: str = Field(alias='methodName')
    amount: Money
    gas_price: Money = Field(alias='gasPrice')
    gas_limit: Money
    sender: Address
    parameters: Optional[List[str]]
