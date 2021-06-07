from typing import Optional
from pydantic import Field
from pybitcoin import Model, PubKey


class JoinFederationResponseModel(Model):
    """A JoinFederationResponseModel."""
    miner_public_key: Optional[PubKey] = Field(alias='MinerPublicKey')
