from typing import Optional, List
from pydantic import Field, SecretStr
from pybitcoin import Model, Outpoint, SmartContractParameter
from pybitcoin.types import Address, Money


class BuildAndSendCreateContractTransactionRequest(Model):
    """A BuildAndSendCreateContractTransactionRequest."""
    wallet_name: str = Field(alias='walletName')
    account_name: Optional[str] = Field(default='account 0', alias='accountName')
    outpoints: List[Outpoint]
    amount: Money
    fee_amount: Optional[Money] = Field(alias='feeAmount')
    password: SecretStr
    contract_code: str = Field(alias='contractCode')
    gas_price: Money = Field(alias='gasPrice')
    gas_limit: Money = Field(alias='gasLimit')
    sender: Address
    parameters: Optional[List[SmartContractParameter]]

