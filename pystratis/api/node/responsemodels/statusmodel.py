from typing import List, Optional
from pydantic import Field, conint
from pystratis.core import Model, FullNodeState
from pystratis.core.types import Money
from .connectedpeermodel import ConnectedPeerModel
from .featuresdatamodel import FeaturesDataModel


class StatusModel(Model):
    """A StatusModel."""
    agent: Optional[str]
    version: Optional[str]
    external_address: Optional[str] = Field(alias='externalAddress')
    network: Optional[str]
    coin_ticker: Optional[str] = Field(alias='coinTicker')
    process_id: Optional[str] = Field(alias='processId')
    consensus_height: Optional[conint(ge=0)] = Field(alias='consensusHeight')
    blockstore_height: Optional[conint(ge=0)] = Field(alias='blockStoreHeight')
    best_peer_height: Optional[conint(ge=0)] = Field(alias='bestPeerHeight')
    inbound_peers: Optional[List[ConnectedPeerModel]] = Field(alias='inboundPeers')
    outbound_peers: Optional[List[ConnectedPeerModel]] = Field(alias='outboundPeers')
    features_data: Optional[List[FeaturesDataModel]] = Field(alias='featuresData')
    data_directory_path: Optional[str] = Field(alias='dataDirectoryPath')
    running_time: Optional[str] = Field(alias='runningTime')
    difficulty: Optional[float]
    protocol_version: Optional[conint(ge=0)] = Field(alias='protocolVersion')
    testnet: Optional[bool]
    relay_fee: Optional[Money] = Field(alias='relayFee')
    state: Optional[FullNodeState]
    in_ibd: Optional[bool] = Field(alias='inIbd')
