from pydantic import Field
from pybitcoin import Model, PubKey


class JoinFederationResponseModel(Model):
    """A JoinFederationResponseModel."""
    miner_public_key: PubKey = Field(alias='MinerPublicKey')
