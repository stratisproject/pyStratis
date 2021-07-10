from typing import Optional, Union
from pydantic import Field, conint
from pystratis.api import Model
from pystratis.core import ExtPubKey
from datetime import datetime


# noinspection PyUnresolvedReferences
class ExtPubRecoveryRequest(Model):
    """A request model for the wallet/recover-via-extpubkey endpoint.

    Args:
        extpubkey (ExtPubKey): The extpubkey for the recovered wallet.
        account_index (conint(ge=0)): The account index.
        name (str): The wallet name.
        creation_date (str, datetime, optional): An estimate of the wallet creation date.
    """
    extpubkey: ExtPubKey = Field(alias='extPubKey')
    account_index: conint(ge=0) = Field(alias='accountIndex')
    name: str
    creation_date: Optional[Union[datetime, str]] = Field(default=None, alias='creationDate')
