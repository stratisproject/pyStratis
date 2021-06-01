from typing import Optional
from pydantic import Field, conint
from pybitcoin import Model, ExtPubKey


class ExtPubRecoveryRequest(Model):
    """An ExtPubRecoveryRequest."""
    extpubkey: ExtPubKey = Field(alias='extPubKey')
    account_index: conint(ge=0) = Field(alias='accountIndex')
    name: str
    creation_date: Optional[str] = Field(default=None, alias='creationDate')
