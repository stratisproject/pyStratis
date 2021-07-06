from pydantic import Field
from pystratis.api import Model
from pystratis.core import PubKey


class JoinFederationResponseModel(Model):
    """A pydantic model for the join federation response."""
    miner_public_key: PubKey = Field(alias='MinerPublicKey')
    """The miner public key for a new federation member, if successful."""
