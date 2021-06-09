from .basenode import BaseNode
from pybitcoin.networks import BaseNetwork, CirrusMain, StraxMain
from api.collateral import Collateral
from api.collateralvoting import CollateralVoting
from api.federationgateway import FederationGateway
from api.federationwallet import FederationWallet
from api.mining import Mining
from api.multisig import Multisig
from api.staking import Staking
from api.balances import Balances
from api.federation import Federation
from api.interop import Interop
from api.smartcontracts import SmartContracts
from api.smartcontractwallet import SmartContractWallet
from api.voting import Voting


class InterfluxStraxNode(BaseNode):
    def __init__(self, ipaddr: str = 'https://localhost', blockchainnetwork: BaseNetwork = StraxMain()):
        super(InterfluxStraxNode, self).__init__(name='InterfluxStrax', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)

        # API endpoints
        self._collateral = Collateral(baseuri=ipaddr, network=blockchainnetwork)
        self._collateral_voting = CollateralVoting(baseuri=ipaddr, network=blockchainnetwork)
        self._federation_gateway = FederationGateway(baseuri=ipaddr, network=blockchainnetwork)
        self._federation_wallet = FederationWallet(baseuri=ipaddr, network=blockchainnetwork)
        self._mining = Mining(baseuri=ipaddr, network=blockchainnetwork)
        self._multisig = Multisig(baseuri=ipaddr, network=blockchainnetwork)
        self._staking = Staking(baseuri=ipaddr, network=blockchainnetwork)

        # Add InterfluxStrax specific endpoints to superclass endpoints.
        self._endpoints.extend(self._collateral.endpoints)
        self._endpoints.extend(self._collateral_voting.endpoints)
        self._endpoints.extend(self._federation_gateway.endpoints)
        self._endpoints.extend(self._federation_wallet.endpoints)
        self._endpoints.extend(self._mining.endpoints)
        self._endpoints.extend(self._multisig.endpoints)
        self._endpoints.extend(self._staking.endpoints)
        self._endpoints.sort()

    @property
    def collateral(self) -> Collateral:
        return self._collateral

    @property
    def collateral_voting(self) -> CollateralVoting:
        return self._collateral_voting

    @property
    def federation_gateway(self) -> FederationGateway:
        return self._federation_gateway

    @property
    def federation_wallet(self) -> FederationWallet:
        return self._federation_wallet

    @property
    def mining(self) -> Mining:
        return self._mining

    @property
    def multisig(self) -> Multisig:
        return self._multisig

    @property
    def staking(self) -> Staking:
        return self._staking


class InterfluxCirrusNode(BaseNode):
    def __init__(self, ipaddr: str = 'https://localhost', blockchainnetwork: BaseNetwork = CirrusMain()):
        super(InterfluxCirrusNode, self).__init__(name='InterfluxCirrus', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)

        # API endpoints
        self._balances = Balances(baseuri=ipaddr, network=blockchainnetwork)
        self._collateral = Collateral(baseuri=ipaddr, network=blockchainnetwork)
        self._collateral_voting = CollateralVoting(baseuri=ipaddr, network=blockchainnetwork)
        self._federation = Federation(baseuri=ipaddr, network=blockchainnetwork)
        self._federation_gateway = FederationGateway(baseuri=ipaddr, network=blockchainnetwork)
        self._federation_wallet = FederationWallet(baseuri=ipaddr, network=blockchainnetwork)
        self._interop = Interop(baseuri=ipaddr, network=blockchainnetwork)
        self._multisig = Multisig(baseuri=ipaddr, network=blockchainnetwork)
        self._smart_contracts = SmartContracts(baseuri=ipaddr, network=blockchainnetwork)
        self._smart_contract_wallet = SmartContractWallet(baseuri=ipaddr, network=blockchainnetwork)
        self._voting = Voting(baseuri=ipaddr, network=blockchainnetwork)

        # Add InterfluxCirrus specific endpoints to superclass endpoints.
        self._endpoints.extend(self._balances.endpoints)
        self._endpoints.extend(self._collateral.endpoints)
        self._endpoints.extend(self._collateral_voting.endpoints)
        self._endpoints.extend(self._federation.endpoints)
        self._endpoints.extend(self._federation_gateway.endpoints)
        self._endpoints.extend(self._federation_wallet.endpoints)
        self._endpoints.extend(self._interop.endpoints)
        self._endpoints.extend(self._multisig.endpoints)
        self._endpoints.extend(self._smart_contracts.endpoints)
        self._endpoints.extend(self._smart_contract_wallet.endpoints)
        self._endpoints.extend(self._voting.endpoints)
        self._endpoints.sort()

    @property
    def balances(self) -> Balances:
        return self._balances

    @property
    def collateral(self) -> Collateral:
        return self._collateral

    @property
    def collateral_voting(self) -> CollateralVoting:
        return self._collateral_voting

    @property
    def federation(self) -> Federation:
        return self._federation

    @property
    def federation_gateway(self) -> FederationGateway:
        return self._federation_gateway

    @property
    def federation_wallet(self) -> FederationWallet:
        return self._federation_wallet

    @property
    def interop(self) -> Interop:
        return self._interop

    @property
    def multisig(self) -> Multisig:
        return self._multisig

    @property
    def smart_contracts(self) -> SmartContracts:
        return self._smart_contracts

    @property
    def smart_contract_wallet(self) -> SmartContractWallet:
        return self._smart_contract_wallet

    @property
    def voting(self) -> Voting:
        return self._voting
