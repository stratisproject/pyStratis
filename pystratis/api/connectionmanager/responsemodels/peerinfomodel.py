from typing import Optional
from pydantic import Field
from pystratis.api import Model


class PeerInfoModel(Model):
    """A pydantic model with power information.."""
    peer_id: int = Field(alias='id')
    """The peer id."""
    addr: str
    """The peer address."""
    addrlocal: str
    """The local peer address."""
    services: str
    """Peer services."""
    relaytxes: bool
    """Relay transactions."""
    lastsend: int
    """Last send."""
    lastrecv: int
    """Last received."""
    bytessent: int
    """Bytes sent."""
    bytesrecv: int
    """Bytes received."""
    conntime: int
    """Connection time in seconds."""
    timeoffset: int
    """The peer time offset in seconds."""
    pingtime: int
    """The ping time in ms."""
    minping: int
    """The minimum ping time."""
    pingwait: int
    """The point wait time."""
    version: int
    """The peer version"""
    subver: str
    """The peer subversion."""
    inbound: bool
    """Inbound connected peer."""
    addnode: bool
    """If true, peer was connected by addnode."""
    starting_height: int = Field(alias='startingheight')
    """Connection starting height."""
    banscore: int
    """The peer's ban score."""
    synced_headers: int
    """The number of synced headers."""
    synced_blocks: int
    """The number of synced blocks."""
    whitelisted: bool
    """If true, peer is whitelisted."""
    inflight: Optional[bool]
    """Inflight peer."""
    bytessent_per_msg: Optional[int]
    """Bytes sent per message."""
    bytesrecv_per_msg: Optional[int]
    """Bytes received per message."""
