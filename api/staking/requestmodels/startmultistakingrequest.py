from typing import List
from pydantic import Field
from pybitcoin import Model, WalletSecret


class StartMultiStakingRequest(Model):
    """A StartMultiStakingRequest."""
    wallet_credentials: List[WalletSecret] = Field(alias='walletCredentials')
