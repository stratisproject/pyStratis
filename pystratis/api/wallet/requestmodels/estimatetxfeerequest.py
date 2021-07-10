from typing import Optional, List
from pydantic import Field, validator
from pystratis.api import Model
from pystratis.core import Outpoint, Recipient
from pystratis.core.types import Address, Money


# noinspection PyUnresolvedReferences
class EstimateTxFeeRequest(Model):
    """A request model for the wallet/estimate-txfee endpoint.

    Args:
        wallet_name (str): The wallet name.
        account_name (str, optional): The account name. Default='account 0'.
        outpoints (List[Outpoint]): A list of outpoints to include in the transaction.
        recipients (List[Recipient]): A list of recipients with amounts.
        op_return_data (str, optional): The OP_RETURN data.
        op_return_amount (Money, optional): The amount to burn in OP_RETURN.
        fee_type (str, optional): The fee type. Allowed [low, medium, high]
        allow_unconfirmed (bool, optional): If True, includes unconfirmed outputs. Default=False.
        shuffle_outputs (bool, optional): If True, shuffle outputs. Default=False.
        change_address (Address, optional): Specify a change address. If not set, a new change address is used.
    """
    wallet_name: str = Field(alias='walletName')
    account_name: Optional[str] = Field(default='account 0', alias='accountName')
    outpoints: List[Outpoint]
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
        return v
