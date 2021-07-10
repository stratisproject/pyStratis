from typing import Optional, Union
from pydantic import SecretStr, Field
from pystratis.api import Model
from datetime import datetime


# noinspection PyUnresolvedReferences
class RecoverRequest(Model):
    """A request model for the wallet/recover endpoint.

    Args:
        mnemonic (str): A mnemonic for initializing a wallet.
        password (str): The password for the wallet.
        passphrase (str): The passphrase for the wallet.
        name (str): The name for the wallet.
        creation_date (str, datetime, optional): An estimate of the wallet creation date.
    """
    mnemonic: str
    password: SecretStr
    passphrase: SecretStr
    name: str
    creation_date: Optional[Union[str, datetime]] = Field(default=None, alias='creationDate')
