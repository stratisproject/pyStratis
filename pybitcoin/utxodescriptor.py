from pydantic import BaseModel, Field
from pybitcoin.types import Money


class UtxoDescriptor(BaseModel):
    """A UtxoDescriptor."""
    transaction_id: str = Field(alias='transactionId')
    index: str
    script_pubkey: str = Field(alias='scriptPubKey')
    amount: Money

    class Config:
        json_encoders = {
            Money: lambda v: str(v),
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super(UtxoDescriptor, self).json(exclude_none=True, by_alias=True)
