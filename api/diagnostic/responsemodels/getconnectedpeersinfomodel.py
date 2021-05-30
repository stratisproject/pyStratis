from typing import List
from pydantic import Field
from pybitcoin import Model
from .connectedpeerinfomodel import ConnectedPeerInfoModel


class GetConnectedPeersInfoModel(Model):
    """A GetConnectedPeersInfoModel."""
    peers_by_peer_id: List[ConnectedPeerInfoModel] = Field(alias='peersByPeerId')
    connected_peers: List[ConnectedPeerInfoModel] = Field(alias='connectedPeers')
    connected_peers_not_in_peers_by_peer_id: List[ConnectedPeerInfoModel] = Field(alias='connectedPeersNotInPeersByPeerId')
