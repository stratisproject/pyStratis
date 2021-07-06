from pydantic import Field
from pystratis.core.types import Address
from .buildcontracttransactionmodel import BuildContractTransactionModel


class BuildCreateContractTransactionModel(BuildContractTransactionModel):
    """A pydantic model for a create smart contact transaction."""
    new_contract_address: Address = Field(alias='newContractAddress')
    """The new address associated with the smart contract."""
