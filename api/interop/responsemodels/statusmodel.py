from typing import List, Dict
from pydantic import Field
from pybitcoin import Model
from .conversionrequestmodel import ConversionRequestModel


class StatusModel(Model):
    """A StatusModel."""
    mint_requests: List[ConversionRequestModel] = Field(alias='mintRequests')
    burn_requests: List[ConversionRequestModel] = Field(alias='burnRequests')
    received_votes: Dict[str, List[str]] = Field(alias='receivedVotes')
