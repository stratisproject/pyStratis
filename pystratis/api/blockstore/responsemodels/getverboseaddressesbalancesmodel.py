from typing import Optional, List
from pydantic import Field, conint
from pystratis.core import Model
from .verboseaddressbalancemodel import VerboseAddressBalanceModel


class GetVerboseAddressesBalancesModel(Model):
    """A GetVerboseAddressesBalancesModel."""
    balances_data: Optional[List[VerboseAddressBalanceModel]] = Field(alias='balancesData')
    consensus_tip_height: Optional[conint(ge=0)] = Field(alias='consensusTipHeight')
    reason: Optional[str]
