from typing import List
from pydantic import Field
from pystratis.api import Model
from pystratis.core import WalletSecret


# noinspection PyUnresolvedReferences
class StartMultiStakingRequest(Model):
    """A request model for the staking/startmultistaking endpoint.

    Args:
        wallet_credentials (List[WalletSecret]): A list of wallet credentials to launch staking of multiple wallets with one command.
    """
    wallet_credentials: List[WalletSecret] = Field(alias='walletCredentials')
