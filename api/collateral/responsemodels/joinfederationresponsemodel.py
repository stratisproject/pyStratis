from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import hexstr


class JoinFederationResponseModel(Model):
    """A JoinFederationResponseModel."""
    miner_public_key: hexstr = Field(alias='MinerPublicKey')
