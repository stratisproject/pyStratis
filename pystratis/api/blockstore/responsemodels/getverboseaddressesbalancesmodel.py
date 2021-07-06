from typing import List, Optional
from pydantic import Field
from pystratis.api import Model
from .verboseaddressbalancemodel import VerboseAddressBalanceModel


class GetVerboseAddressesBalancesModel(Model):
    """A pydantic model representing verbose address balance information."""
    balances_data: List[VerboseAddressBalanceModel] = Field(alias='balancesData')
    """A list of verbose address balance data for the given addresses."""
    consensus_tip_height: int = Field(alias='consensusTipHeight')
    """The current consensus tip height."""
    reason: Optional[str]
    """If query failed, a reason is given."""
