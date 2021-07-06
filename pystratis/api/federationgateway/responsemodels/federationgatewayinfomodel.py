from typing import List, Optional
from pydantic import Field
from pystratis.api import Model
from pystratis.core import PubKey
from pystratis.core.types import Address


class FederationGatewayInfoModel(Model):
    """A pydantic model representing information on the federation gateway."""
    active: bool
    """True if federation gateway is active."""
    mainchain: bool
    """True if called on mainchain node."""
    endpoints: List[str]
    """A list of federation endpoints."""
    multisig_pubkey: PubKey = Field(alias='multisigPubKey')
    """The multisig pubkey."""
    federation_multisig_pubkeys: List[PubKey] = Field(alias='federationMultisigPubKeys')
    """A list of federation multisig pubkeys."""
    mining_pubkey: PubKey = Field(default='', alias='miningPubKey')
    """The mining pubkey."""
    federation_mining_pubkeys: Optional[List[PubKey]] = Field(default=[], alias='federationMiningPubKeys')
    """The federation mining pubkeys. Only active if federation mining is active."""
    multisig_address: Address = Field(alias='multisigAddress')
    """The multisig address."""
    multisig_redeem_script: Optional[str] = Field(alias='multisigRedeemScript')
    """The multisig redeem script."""
    multisig_redeem_script_payment_script: Optional[str] = Field(alias='multisigRedeemScriptPaymentScript')
    """The multisig redeem script payment script."""
    min_conf_small_deposits: int = Field(alias='minconfsmalldeposits')
    """The minimum confirmations for small deposits."""
    min_conf_normal_deposits: int = Field(alias='minconfnormaldeposits')
    """The minimum confirmations for normal deposits."""
    min_conf_large_deposits: int = Field(alias='minconflargedeposits')
    """The minimum confirmations for large deposits."""
    min_conf_distribution_deposits: int = Field(alias='minconfdistributiondeposits')
    """The minimum confirmations for distribution deposits."""
