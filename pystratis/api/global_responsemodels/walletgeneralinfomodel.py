from typing import Optional
from pydantic import Field, conint
from datetime import datetime
from pystratis.api import Model


class WalletGeneralInfoModel(Model):
    """A model representing general wallet info.

    Args:
        wallet_name (str, optional): The name of the wallet.
        network (str): The name of network this wallet operating on.
        creation_time (str): The time this wallet was created.
        is_decrypted (bool): Is wallet decrypted or not.
        last_block_synced_height (int, optional): The height of the last block that was synced
        chain_tip (int, optional): The total number of blocks.
        is_chain_synced (bool): Whether the chain is synced with the network.
        connected_nodes (int): The total number of nodes that we're connected to.
    """
    wallet_name: Optional[str] = Field(alias='walletName')
    network: str
    creation_time: datetime = Field(alias='creationTime')
    is_decrypted: bool = Field(alias='isDecrypted')
    last_block_synced_height: Optional[conint(ge=0)] = Field(alias='lastBlockSyncedHeight')
    chain_tip: Optional[conint(ge=0)] = Field(alias='chainTip')
    is_chain_synced: bool = Field(alias='isChainSynced')
    connected_nodes: conint(ge=0) = Field(alias='connectedNodes')
