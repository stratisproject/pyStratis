from typing import Optional
from pydantic import Field, conint
from pybitcoin import Model
from pybitcoin.types import hexstr


class ExtPubRecoveryRequest(Model):
    """An ExtPubRecoveryRequest."""
    ext_pubkey: hexstr = Field(alias='extPubKey')
    account_index: conint(ge=0) = Field(alias='accountIndex')
    name: str
    creation_date: Optional[str] = Field(default=None, alias='creationDate')
