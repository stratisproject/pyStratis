from pydantic import BaseModel, Field


class RemovedTransactionModel(BaseModel):
    """A RemovedTransactionModel."""
    transaction_id: str = Field(alias='transactionId')
    creation_time: str = Field(alias='creationTime')

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super(RemovedTransactionModel, self).json(exclude_none=True, by_alias=True)
