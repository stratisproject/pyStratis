from pybitcoin.networks import BaseNetwork, CirrusMain, CirrusTest, CirrusRegTest
from .basenode import BaseNode
from api.balances import Balances
from api.collateral import Collateral
from api.diagnostic import Diagnostic
from api.federation import Federation
from api.smartcontracts import SmartContracts
from api.smartcontractwallet import SmartContractWallet
from api.signalr import SignalR
from api.voting import Voting


class CirrusNode(BaseNode):
    def __init__(self, ipaddr: str = 'http://localhost', blockchainnetwork: BaseNetwork = CirrusMain()):
        if not isinstance(blockchainnetwork, (CirrusMain, CirrusTest, CirrusRegTest)):
            raise ValueError('Invalid network. Must be one of: [CirrusMain, CirrusTest, CirrusRegTest]')
        super(CirrusNode, self).__init__(name='Cirrus', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)

        # API endpoints
        self._balances = Balances(baseuri=self.api_route, network=blockchainnetwork)
        self._collateral = Collateral(baseuri=self.api_route, network=blockchainnetwork)
        self._diagnostic = Diagnostic(baseuri=self.api_route, network=blockchainnetwork)
        self._federation = Federation(baseuri=self.api_route, network=blockchainnetwork)
        self._smart_contracts = SmartContracts(baseuri=self.api_route, network=blockchainnetwork)
        self._smart_contract_wallet = SmartContractWallet(baseuri=self.api_route, network=blockchainnetwork)
        self._signalr = SignalR(baseuri=self.api_route, network=blockchainnetwork)
        self._voting = Voting(baseuri=self.api_route, network=blockchainnetwork)

        # Add Cirrus specific endpoints to superclass endpoints.
        self._endpoints.extend(self._balances.endpoints)
        self._endpoints.extend(self._collateral.endpoints)
        self._endpoints.extend(self._diagnostic.endpoints)
        self._endpoints.extend(self._federation.endpoints)
        self._endpoints.extend(self._smart_contracts.endpoints)
        self._endpoints.extend(self._smart_contract_wallet.endpoints)
        self._endpoints.extend(self._signalr.endpoints)
        self._endpoints.extend(self._voting.endpoints)
        self._endpoints.sort()

    @property
    def balances(self) -> Balances:
        return self._balances

    @property
    def collateral(self) -> Collateral:
        return self._collateral

    @property
    def diagnostic(self) -> Diagnostic:
        return self._diagnostic

    @property
    def federation(self) -> Federation:
        return self._federation

    @property
    def smart_contracts(self) -> SmartContracts:
        return self._smart_contracts

    @property
    def smart_contract_wallet(self) -> SmartContractWallet:
        return self._smart_contract_wallet

    @property
    def signalr(self) -> SignalR:
        return self._signalr

    @property
    def voting(self) -> Voting:
        return self._voting
