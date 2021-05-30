from typing import List
from pydantic import Field, BaseModel
from .transactionoutputmodel import TransactionOutputModel


class WalletSendTransactionModel(BaseModel):
    """A WalletSendTransactionModel."""
    transaction_id: str = Field(alias='transactionId')
    outputs: List[TransactionOutputModel]

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super(WalletSendTransactionModel, self).json(exclude_none=True, by_alias=True)
