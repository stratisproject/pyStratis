from pydantic import BaseModel, Field, conint
from pybitcoin.types import Money
from .destinationchain import DestinationChain
from .depositretrievaltype import DepositRetrievalType


class Deposit(BaseModel):
    """A Deposit."""
    deposit_id: str = Field(alias='id')
    amount: Money
    target_address: str = Field(alias='TargetAddress')
    target_chain: DestinationChain = Field(alias='TargetChain')
    block_number: conint(ge=0) = Field(alias='BlockNumber')
    block_hash: str = Field(alias='BlockHash')
    retrieval_type: DepositRetrievalType = Field(alias='RetrievalType')

    class Config:
        json_encoders = {
            Money: lambda v: str(v),
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super(Deposit, self).json(exclude_none=True, by_alias=True)
