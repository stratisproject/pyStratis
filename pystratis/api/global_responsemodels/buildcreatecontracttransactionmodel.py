from typing import Optional
from pydantic import Field
from pystratis.core.types import Address
from .buildcontracttransactionmodel import BuildContractTransactionModel


class BuildCreateContractTransactionModel(BuildContractTransactionModel):
    """A BuildCreateContractTransactionModel."""
    new_contract_address: Optional[Address] = Field(alias='newContractAddress')
