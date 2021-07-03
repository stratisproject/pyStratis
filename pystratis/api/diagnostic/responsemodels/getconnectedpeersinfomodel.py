from typing import List, Optional
from pydantic import Field
from pystratis.core import Model
from .connectedpeerinfomodel import ConnectedPeerInfoModel


class GetConnectedPeersInfoModel(Model):
    """A GetConnectedPeersInfoModel."""
    peers_by_peer_id: Optional[List[ConnectedPeerInfoModel]] = Field(alias='peersByPeerId')
    connected_peers: Optional[List[ConnectedPeerInfoModel]] = Field(alias='connectedPeers')
    connected_peers_not_in_peers_by_peer_id: Optional[List[ConnectedPeerInfoModel]] = Field(alias='connectedPeersNotInPeersByPeerId')
