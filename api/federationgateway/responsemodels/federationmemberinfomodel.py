from typing import List
from pydantic import Field, conint
from pybitcoin import Model
from .federationmemberconnectioninfo import FederationMemberConnectionInfo


class FederationMemberInfoModel(Model):
    """A FederationMemberInfoModel."""
    async_loop_state: str = Field(alias='asyncLoopState')
    consensus_height: conint(ge=0) = Field(alias='consensusHeight')
    ccts_height: conint(ge=0) = Field(alias='cctsHeight')
    ccts_next_deposit_height: conint(ge=0) = Field(alias='cctsNextDepositHeight')
    ccts_partials: conint(ge=0) = Field(alias='cctsPartials')
    ccts_suspended: conint(ge=0) = Field(alias='cctsSuspended')
    federation_wallet_active: bool = Field(alias='federationWalletActive')
    federation_wallet_height: conint(ge=0) = Field(alias='federationWalletHeight')
    node_version: str = Field(alias='nodeVersion')
    pubkey: str = Field(alias='pubKey')
    federation_connection_state: str = Field(alias='federationConnectionState')
    federation_member_connections: List[FederationMemberConnectionInfo] = Field(alias='FederationMemberConnections')
