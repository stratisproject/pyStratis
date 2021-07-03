from typing import List, Dict, Optional
from pydantic import Field
from pystratis.api import Model
from pystratis.core import PubKey
from pystratis.core.types import uint256
from .conversionrequestmodel import ConversionRequestModel


class StatusModel(Model):
    """A StatusModel."""
    mint_requests: Optional[List[ConversionRequestModel]] = Field(alias='mintRequests')
    burn_requests: Optional[List[ConversionRequestModel]] = Field(alias='burnRequests')
    received_votes: Optional[Dict[uint256, List[PubKey]]] = Field(alias='receivedVotes')
