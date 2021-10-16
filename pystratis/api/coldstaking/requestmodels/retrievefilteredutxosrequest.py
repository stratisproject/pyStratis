from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import hexstr


# noinspection PyUnresolvedReferences
class RetrieveFilteredUTXOsRequest(Model):
    """A request model for the coldstaking/retrieve-filtered-utxos endpoint.

    Args:
        wallet_name (str): The wallet name.
        wallet_password (str): The wallet password.
        wallet_account (str): The wallet account.
        trx_hex (hexstr): The transaction id hex.
        broadcast (bool): If true, broadcast the transaction to the network after being built.
    """
    wallet_name: str = Field(alias='walletName')
    wallet_password: str = Field(alias='walletPassword')
    wallet_account: str = Field(alias='walletAccount')
    trx_hex: hexstr = Field(alias='hex')
    broadcast: bool
