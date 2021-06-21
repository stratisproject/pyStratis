from pydantic import BaseModel, Field, conint
from pybitcoin.types import Address, Money, uint256
from .destinationchain import DestinationChain
from .depositretrievaltype import DepositRetrievalType


class Deposit(BaseModel):
    """A Deposit."""
    deposit_id: uint256 = Field(alias='id')
    amount: Money
    target_address: Address = Field(alias='TargetAddress')
    target_chain: DestinationChain = Field(alias='TargetChain')
    block_number: conint(ge=0) = Field(alias='BlockNumber')
    block_hash: uint256 = Field(alias='BlockHash')
    retrieval_type: DepositRetrievalType = Field(alias='RetrievalType')

    class Config:
        json_encoders = {
            Money: lambda v: v.to_coin_unit(),
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
