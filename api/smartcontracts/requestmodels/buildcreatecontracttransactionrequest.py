from typing import Optional, List
import json
from pydantic import Field, SecretStr
from pybitcoin import Address, Model, Outpoint
from pybitcoin.types import Money


class BuildCreateContractTransactionRequest(Model):
    """A BuildCreateContractTransactionRequest."""
    wallet_name: str = Field(alias='walletName')
    account_name: Optional[str] = Field(default='account 0', alias='accountName')
    outpoints: List[Outpoint]
    amount: Money
    fee_amount: Optional[Money] = Field(alias='feeAmount')
    password: SecretStr
    contract_code: str = Field(alias='contractCode')
    gas_price: Money = Field(alias='gasPrice')
    gas_limit: Money
    sender: Address
    parameters: Optional[List[str]]

    def json(self, *args, **kwargs) -> str:
        data = {
            'walletName': self.wallet_name,
            'accountName': self.account_name,
            'outpoints': [x.json() for x in self.outpoints],
            'amount': self.amount,
            'password': self.password.get_secret_value(),
            'contractCode': self.contract_code,
            'gasPrice': self.gas_price,
            'gasLimit': self.gas_limit,
            'sender': str(self.sender),
        }
        if self.fee_amount is not None:
            data['feeAmount'] = self.fee_amount
        if self.parameters is not None:
            data['parameters'] = self.parameters
        return json.dumps(data)
