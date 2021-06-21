from typing import List
from pydantic import Field, BaseModel
from pybitcoin.types import uint256
from .transactionoutputmodel import TransactionOutputModel


class WalletSendTransactionModel(BaseModel):
    """A WalletSendTransactionModel."""
    transaction_id: uint256 = Field(alias='transactionId')
    outputs: List[TransactionOutputModel]

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
