from typing import Optional, List
from pydantic import Field, SecretStr
from pybitcoin import Address, Model, Outpoint, SmartContractParameter
from pybitcoin.types import Money


class BuildCallContractTransactionRequest(Model):
    """A BuildCallContractTransactionRequest."""
    wallet_name: str = Field(alias='walletName')
    account_name: Optional[str] = Field(default='account 0', alias='accountName')
    outpoints: List[Outpoint]
    contract_address: Address = Field(alias='contractAddress')
    method_name: str = Field(alias='methodName')
    amount: Money
    fee_amount: Optional[Money] = Field(alias='feeAmount')
    password: SecretStr
    gas_price: Money = Field(alias='gasPrice')
    gas_limit: Money = Field(alias='gasLimit')
    sender: Address
    parameters: Optional[List[SmartContractParameter]]
