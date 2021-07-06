from typing import List
from pydantic import Field
from pystratis.api import Model
from .connectedpeerinfomodel import ConnectedPeerInfoModel


class GetConnectedPeersInfoModel(Model):
    """A pydantic model for connected peer information."""
    peers_by_peer_id: List[ConnectedPeerInfoModel] = Field(alias='peersByPeerId')
    """A list of peers by id."""
    connected_peers: List[ConnectedPeerInfoModel] = Field(alias='connectedPeers')
    """A list of connected peers."""
    connected_peers_not_in_peers_by_peer_id: List[ConnectedPeerInfoModel] = Field(alias='connectedPeersNotInPeersByPeerId')
    """A list of known peer ls not connected to."""
