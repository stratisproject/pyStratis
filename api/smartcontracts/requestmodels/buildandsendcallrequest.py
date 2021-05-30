from typing import Optional, List
from pydantic import Field, SecretStr
from pybitcoin import Address, Model, Outpoint
from pybitcoin.types import Money


class BuildAndSendCallContractTransactionRequest(Model):
    """A BuildAndSendCallContractTransactionRequest."""
    wallet_name: str = Field(alias='walletName')
    account_name: Optional[str] = Field(default='account 0', alias='accountName')
    outpoints: List[Outpoint]
    contract_address: Address = Field(alias='contractAddress')
    method_name: str = Field(alias='methodName')
    amount: Money
    fee_amount: Optional[Money] = Field(alias='feeAmount')
    password: SecretStr
    gas_price: Money = Field(alias='gasPrice')
    gas_limit: Money
    sender: Address
    parameters: Optional[List[str]]
