from typing import Optional
from pydantic import conint, Field
from pybitcoin import Model


class PeerInfoModel(Model):
    """A PeerInfoModel."""
    peer_id: conint(ge=0) = Field(alias='id')
    addr: str
    addrlocal: str
    services: str
    relaytxes: bool
    lastsend: conint(ge=0)
    lastrecv: conint(ge=0)
    bytessent: conint(ge=0)
    bytesrecv: conint(ge=0)
    conntime: conint(ge=0)
    timeoffset: conint(ge=0)
    pingtime: conint(ge=0)
    minping: conint(ge=0)
    pingwait: conint(ge=0)
    version: conint(ge=0)
    subver: str
    inbound: bool
    addnode: bool
    starting_height: conint(ge=0) = Field(alias='startingheight')
    banscore: conint(ge=0)
    synced_headers: conint(ge=0)
    synced_blocks: conint(ge=0)
    whitelisted: bool
    inflight: Optional[bool]
    bytessent_per_msg: Optional[conint(ge=0)]
    bytesrecv_per_msg: Optional[conint(ge=0)]
