from typing import Optional
from pydantic import BaseModel, Field, conint
from pybitcoin.types import Address, Money, uint256
from .destinationchain import DestinationChain
from .depositretrievaltype import DepositRetrievalType


class Deposit(BaseModel):
    """A Deposit."""
    deposit_id: uint256 = Field(alias='id')
    amount: Money
    target_address: Address = Field(alias='targetAddress')
    target_chain: Optional[DestinationChain] = Field(alias='targetChain')
    block_number: conint(ge=0) = Field(alias='blockNumber')
    block_hash: uint256 = Field(alias='blockHash')
    retrieval_type: DepositRetrievalType = Field(alias='retrievalType')

    class Config:
        json_encoders = {
            Money: lambda v: v.to_coin_unit(),
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
