from typing import List, Optional
from pydantic import Field
from pystratis.api import Model
from pystratis.core import PubKey
from .federationmemberconnectioninfomodel import FederationMemberConnectionInfoModel


class FederationMemberInfoModel(Model):
    """A pydantic model representing information about the current federation member."""
    async_loop_state: str = Field(alias='asyncLoopState')
    """The async loop state."""
    consensus_height: int = Field(alias='consensusHeight')
    """The current consensus height."""
    ccts_height: int = Field(alias='cctsHeight')
    """The node's CCTS height."""
    ccts_next_deposit_height: int = Field(alias='cctsNextDepositHeight')
    """The next CCTS deposit height."""
    ccts_partials: int = Field(alias='cctsPartials')
    """The number of partial CCTS transactions."""
    ccts_suspended: int = Field(alias='cctsSuspended')
    """The number of suspended CCTS transactions."""
    federation_wallet_active: bool = Field(alias='federationWalletActive')
    """If true, the federation wallet is active."""
    federation_wallet_height: int = Field(alias='federationWalletHeight')
    """The local federation wallet height."""
    node_version: str = Field(alias='nodeVersion')
    """The node version."""
    pubkey: Optional[PubKey] = Field(alias='pubKey')
    """The member's pubkey. Could be None."""
    federation_connection_state: str = Field(alias='federationConnectionState')
    """The federation connection state."""
    federation_member_connections: List[FederationMemberConnectionInfoModel] = Field(alias='federationMemberConnections')
    """A list of connected federation members."""
