from pybitcoin.networks import BaseNetwork, CirrusMain, CirrusTest, CirrusRegTest
from .basenode import BaseNode
from api.balances import Balances
from api.collateral import Collateral
from api.notifications import Notifications
from api.federation import Federation
from api.smartcontracts import SmartContracts
from api.smartcontractwallet import SmartContractWallet
from api.voting import Voting


class CirrusMinerNode(BaseNode):
    def __init__(self, ipaddr: str = 'http://localhost', blockchainnetwork: BaseNetwork = CirrusMain(), devmode=False):
        if not isinstance(blockchainnetwork, (CirrusMain, CirrusTest, CirrusRegTest)):
            raise ValueError('Invalid network. Must be one of: [CirrusMain, CirrusTest, CirrusRegTest]')
        super(CirrusMinerNode, self).__init__(name='Cirrus', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)

        # API endpoints
        self._balances = Balances(baseuri=self.api_route, network=blockchainnetwork)
        if not devmode:
            self._collateral = Collateral(baseuri=self.api_route, network=blockchainnetwork)
            self._endpoints.extend(self._collateral.endpoints)
            setattr(self.__class__, 'collateral', property(lambda p: self._collateral))
        self._federation = Federation(baseuri=self.api_route, network=blockchainnetwork)
        self._notifications = Notifications(baseuri=self.api_route, network=blockchainnetwork)
        self._smart_contracts = SmartContracts(baseuri=self.api_route, network=blockchainnetwork)
        self._smart_contract_wallet = SmartContractWallet(baseuri=self.api_route, network=blockchainnetwork)
        self._voting = Voting(baseuri=self.api_route, network=blockchainnetwork)

        # Add CirrusMiner specific endpoints to superclass endpoints.
        self._endpoints.extend(self._balances.endpoints)
        self._endpoints.extend(self._federation.endpoints)
        self._endpoints.extend(self._notifications.endpoints)
        self._endpoints.extend(self._smart_contracts.endpoints)
        self._endpoints.extend(self._smart_contract_wallet.endpoints)
        self._endpoints.extend(self._voting.endpoints)
        self._endpoints.sort()

    @property
    def balances(self) -> Balances:
        return self._balances

    @property
    def federation(self) -> Federation:
        return self._federation

    @property
    def notifications(self) -> Notifications:
        return self._notifications

    @property
    def smart_contracts(self) -> SmartContracts:
        return self._smart_contracts

    @property
    def smart_contract_wallet(self) -> SmartContractWallet:
        return self._smart_contract_wallet

    @property
    def voting(self) -> Voting:
        return self._voting
