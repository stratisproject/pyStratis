from typing import Optional
from pydantic import Field
from datetime import datetime
from pystratis.api import Model


class WalletGeneralInfoModel(Model):
    """A model representing general wallet info."""
    wallet_name: Optional[str] = Field(alias='walletName')
    """The name of the wallet. Will be None for multisig."""
    network: str
    """The name of the network the wallet is operating on."""
    creation_time: datetime = Field(alias='creationTime')
    """The datetime of wallet creation """
    is_decrypted: bool = Field(alias='isDecrypted')
    """If true, wallet is decrypted."""
    last_block_synced_height: int = Field(alias='lastBlockSyncedHeight')
    """The height of last block synced by wallet."""
    chain_tip: int = Field(alias='chainTip')
    """The height off the chain tip."""
    is_chain_synced: bool = Field(alias='isChainSynced')
    """If true, chain is synced."""
    connected_nodes: int = Field(alias='connectedNodes')
    """The number of connected nodes."""
