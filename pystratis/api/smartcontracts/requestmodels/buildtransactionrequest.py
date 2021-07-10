from typing import Optional, List
from pydantic import Field, SecretStr, validator
from pystratis.api import Model
from pystratis.core import Outpoint, Recipient
from pystratis.core.types import Address, Money


# noinspection PyUnresolvedReferences
class BuildTransactionRequest(Model):
    """A request model for the smartcontracts/build-transaction endpoint.

    Args:
        sender (Address): The sender address.
        fee_amount (Money, optional): The fee amount.
        password (SecretStr): The password.
        segwit_change_address (bool, optional): If the change address is a segwit address. Default=False.
        wallet_name (str): The wallet name.
        account_name (str, optional): The account name. Default='account 0'.
        outpoints (List[Outpoint]): A list of the outpoints used to construct the transactation.
        recipients (List[Recipient]): A list of the recipients, including amounts, for the transaction.
        op_return_data (str, optional): OP_RETURN data to include with the transaction.
        op_return_amount (Money, optional): Amount to burn in the OP_RETURN transaction.
        fee_type (str, optional): low, medium, or high.
        allow_unconfirmed (bool, optional): If True, allow unconfirmed transactions in the estimation. Default=False
        shuffle_outputs (bool, optional): If True, shuffles outputs. Default=False.
        change_address (Address, optional): Sends output sum less amount sent to recipients to this designated change address, if provided.

    Notes:
         Both fee_type and fee_amount cannot be set.
    """
    sender: Address
    fee_amount: Optional[Money] = Field(alias='feeAmount')
    password: SecretStr
    segwit_change_address: Optional[bool] = Field(default=False, alias='segwitChangeAddress')
    wallet_name: str = Field(alias='walletName')
    account_name: Optional[str] = Field(default='account 0', alias='accountName')
    outpoints: Optional[List[Outpoint]]
    recipients: List[Recipient]
    op_return_data: Optional[str] = Field(alias='opReturnData')
    op_return_amount: Optional[Money] = Field(alias='opReturnAmount')
    fee_type: Optional[str] = Field(alias='feeType')
    allow_unconfirmed: Optional[bool] = Field(default=False, alias='allowUnconfirmed')
    shuffle_outputs: Optional[bool] = Field(default=False, alias='shuffleOutputs')
    change_address: Optional[Address] = Field(alias='changeAddress')

    # noinspection PyMethodParameters,PyUnusedLocal
    @validator('fee_type')
    def validate_fee_type(cls, v, values):
        allowed = [
            'low',
            'medium',
            'high'
        ]
        if v is not None and v not in allowed:
            raise ValueError(f'Invalid command. Must be: {allowed}')
        if v is not None and values['fee_amount'] is not None:
            raise ValueError('Both fee_type and fee_amount cannot be set.')
        return v

    # noinspection PyMethodParameters,PyUnusedLocal
    @validator('fee_amount', always=True)
    def check_fee_too_high(cls, v, values):
        if v is not None:
            if v > Money(1):
                raise ValueError('Fee should not be more than 1. Check parameters.')
        return v
