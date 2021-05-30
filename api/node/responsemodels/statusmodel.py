from typing import List
from pydantic import Field, conint
from pybitcoin import Model
from pybitcoin.types import Money
from .connectedpeermodel import ConnectedPeerModel
from .featuresdatamodel import FeaturesDataModel


class StatusModel(Model):
    """A StatusModel."""
    agent: str
    version: str
    external_address: str = Field(alias='externalAddress')
    network: str
    coin_ticker: str = Field(alias='coinTicker')
    process_id: str = Field(alias='processId')
    consensus_height: conint(ge=0) = Field(alias='consensusHeight')
    blockstore_height: conint(ge=0) = Field(alias='blockStoreHeight')
    best_peer_height: conint(ge=0) = Field(alias='bestPeerheight')
    inbound_peers: List[ConnectedPeerModel] = Field(alias='inboundPeers')
    outbound_peers: List[ConnectedPeerModel] = Field(alias='outboundPeers')
    features_data: List[FeaturesDataModel] = Field(alias='featuresData')
    data_directory_path: str = Field(alias='dataDirectoryPath')
    running_time: str = Field(alias='runningTime')
    difficulty: float
    protocol_version: conint(ge=0) = Field(alias='protocolVersion')
    testnet: bool
    relay_fee: Money = Field(alias='relayFee')
    state: str
