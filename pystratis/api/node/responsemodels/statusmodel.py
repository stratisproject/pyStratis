from typing import List, Optional
from pydantic import Field
from pystratis.api import Model, FullNodeState
from pystratis.core.types import Money
from .connectedpeermodel import ConnectedPeerModel
from .featuresdatamodel import FeaturesDataModel


class StatusModel(Model):
    """A pydantic model for node status information."""
    agent: str
    """The node's agent string."""
    version: str
    """The node version."""
    external_address: str = Field(alias='externalAddress')
    """The node external address."""
    network: str
    """The network."""
    coin_ticker: str = Field(alias='coinTicker')
    """The ticker string of the current network's coin."""
    process_id: str = Field(alias='processId')
    """The process id of the node."""
    consensus_height: Optional[int] = Field(alias='consensusHeight')
    """The current consensus height."""
    blockstore_height: int = Field(alias='blockStoreHeight')
    """The current blockstore height."""
    best_peer_height: Optional[int] = Field(alias='bestPeerHeight')
    """The highest block height among connected peers."""
    inbound_peers: List[ConnectedPeerModel] = Field(alias='inboundPeers')
    """A list of inbound connected peers."""
    outbound_peers: List[ConnectedPeerModel] = Field(alias='outboundPeers')
    """A list of outbound connected peers."""
    features_data: List[FeaturesDataModel] = Field(alias='featuresData')
    """A list of features active on the node."""
    data_directory_path: str = Field(alias='dataDirectoryPath')
    """The path to the node's data directory."""
    running_time: str = Field(alias='runningTime')
    """The node's current running time."""
    difficulty: Optional[float]
    """The current difficulty, if applicable."""
    protocol_version: int = Field(alias='protocolVersion')
    """The current protocol version."""
    testnet: bool
    """If true, node is on testnet."""
    relay_fee: Money = Field(alias='relayFee')
    """The network transaction relay fee."""
    state: FullNodeState
    """The node state model."""
    in_ibd: bool = Field(alias='inIbd')
    """If true, the node is in IBD state."""
