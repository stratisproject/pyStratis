from typing import Optional
from pydantic import Field
from pystratis.api import Model
from pystratis.core import PubKey


class JoinFederationResponseModel(Model):
    """A JoinFederationResponseModel."""
    miner_public_key: Optional[PubKey] = Field(alias='MinerPublicKey')
