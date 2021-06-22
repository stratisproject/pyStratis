from typing import List, Optional
from pydantic import Field, conint
from pybitcoin import Model, PubKey
from .federationmemberconnectioninfo import FederationMemberConnectionInfo


class FederationMemberInfoModel(Model):
    """A FederationMemberInfoModel."""
    async_loop_state: Optional[str] = Field(alias='asyncLoopState')
    consensus_height: Optional[conint(ge=0)] = Field(alias='consensusHeight')
    ccts_height: Optional[conint(ge=0)] = Field(alias='cctsHeight')
    ccts_next_deposit_height: Optional[conint(ge=0)] = Field(alias='cctsNextDepositHeight')
    ccts_partials: Optional[conint(ge=0)] = Field(alias='cctsPartials')
    ccts_suspended: Optional[conint(ge=0)] = Field(alias='cctsSuspended')
    federation_wallet_active: Optional[bool] = Field(alias='federationWalletActive')
    federation_wallet_height: Optional[conint(ge=0)] = Field(alias='federationWalletHeight')
    node_version: Optional[str] = Field(alias='nodeVersion')
    pubkey: Optional[PubKey] = Field(alias='pubKey')
    federation_connection_state: Optional[str] = Field(alias='federationConnectionState')
    federation_member_connections: Optional[List[FederationMemberConnectionInfo]] = Field(alias='federationMemberConnections')
