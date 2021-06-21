from pydantic import BaseModel, Field
from pybitcoin.types import uint256


class RemovedTransactionModel(BaseModel):
    """A RemovedTransactionModel."""
    transaction_id: uint256 = Field(alias='transactionId')
    creation_time: str = Field(alias='creationTime')

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
