from typing import Optional
from pydantic import BaseModel, Field, conint
from pystratis.core.types import Address, Money, uint256
from .destinationchain import DestinationChain
from .depositretrievaltype import DepositRetrievalType


class Deposit(BaseModel):
    """Represents a deposit made to a sidechain mutlisig, 
    with the aim of triggering a cross chain transfer.

    Args:
        deposit_id (uint256): The Id (or hash) of the source transaction that originates the fund transfer.
        amount (Money): The amount of the requested fund transfer.
        target_address (Address): The target address, on the target chain, for the fund deposited on the multisig.
        target_chain (DestinationChain, optional): Chain on which STRAX minting or burning should occur.
        block_number (int): The block number where the source deposit has been persisted.
        block_hash (uint256): The hash of the block where the source deposit has been persisted.
        retrieval_type (DepositRetrievalType): Whether the deposit is a "faster" or "normal" deposit.
    Note:
        Learn how to `acquire CRS token using GUI`__.

    .. __: https://academy.stratisplatform.com/Operation%20Guides/Sidechain/AcquiringCRS/cross-chain-transfer.html
    """
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
