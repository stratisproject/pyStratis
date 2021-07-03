from typing import Optional
from pydantic import conint, Field
from pystratis.api import Model


class PeerInfoModel(Model):
    """A PeerInfoModel."""
    peer_id: Optional[conint(ge=0)] = Field(alias='id')
    addr: Optional[str]
    addrlocal: Optional[str]
    services: Optional[str]
    relaytxes: Optional[bool]
    lastsend: Optional[conint(ge=0)]
    lastrecv: Optional[conint(ge=0)]
    bytessent: Optional[conint(ge=0)]
    bytesrecv: Optional[conint(ge=0)]
    conntime: Optional[conint(ge=0)]
    timeoffset: Optional[conint(ge=0)]
    pingtime: Optional[conint(ge=0)]
    minping: Optional[conint(ge=0)]
    pingwait: Optional[conint(ge=0)]
    version: Optional[conint(ge=0)]
    subver: Optional[str]
    inbound: Optional[bool]
    addnode: Optional[bool]
    starting_height: Optional[conint(ge=0)] = Field(alias='startingheight')
    banscore: Optional[conint(ge=0)]
    synced_headers: Optional[conint(ge=0)]
    synced_blocks: Optional[conint(ge=0)]
    whitelisted: Optional[bool]
    inflight: Optional[bool]
    bytessent_per_msg: Optional[conint(ge=0)]
    bytesrecv_per_msg: Optional[conint(ge=0)]
