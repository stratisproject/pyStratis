from typing import List
from pydantic import Field, conint
from pybitcoin import Address, Model, PubKey
from pybitcoin.types import hexstr


class FederationGatewayInfoModel(Model):
    """A FederationGatewayInfoModel."""
    active: bool
    mainchain: bool
    endpoints: List[str]
    multisig_pubkey: PubKey = Field(alias='multisigPubKey')
    federation_multisig_pubkeys: List[PubKey] = Field(alias='federationMultisigPubKeys')
    mining_pubkey: PubKey = Field(default='', alias='miningPubKey')
    federation_mining_pubkeys: List[PubKey] = Field(default=[], alias='federationMiningPubKeys')
    multisig_address: Address = Field(alias='multisigAddress')
    multisig_redeem_script: str = Field(alias='multisigRedeemScript')
    multisig_redeem_script_payment_script: str = Field(alias='multisigRedeemScriptPaymentScript')
    min_conf_small_deposits: conint(ge=0) = Field(alias='minconfsmalldeposits')
    min_conf_normal_deposits: conint(ge=0) = Field(alias='minconfnormaldeposits')
    min_conf_large_deposits: conint(ge=0) = Field(alias='minconflargedeposits')
    min_conf_distribution_deposits: conint(ge=0) = Field(alias='minconfdistributiondeposits')
