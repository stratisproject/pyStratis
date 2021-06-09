from pybitcoin.networks import BaseNetwork, CirrusMain
from .basenode import BaseNode
from api.balances import Balances
from api.collateral import Collateral
from api.diagnostic import Diagnostic
from api.federation import Federation
from api.smartcontracts import SmartContracts
from api.smartcontractwallet import SmartContractWallet


class CirrusNode(BaseNode):
    def __init__(self, ipaddr: str = 'https://localhost', blockchainnetwork: BaseNetwork = CirrusMain()):
        super(CirrusNode, self).__init__(name='Cirrus', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)

        # API endpoints
        self._balances = Balances(baseuri=ipaddr, network=blockchainnetwork)
        self._collateral = Collateral(baseuri=ipaddr, network=blockchainnetwork)
        self._diagnostic = Diagnostic(baseuri=ipaddr, network=blockchainnetwork)
        self._federation = Federation(baseuri=ipaddr, network=blockchainnetwork)
        self._smart_contracts = SmartContracts(baseuri=ipaddr, network=blockchainnetwork)
        self._smart_contract_wallet = SmartContractWallet(baseuri=ipaddr, network=blockchainnetwork)

        # Add Cirrus specific endpoints to superclass endpoints.
        self._endpoints.extend(self._balances.endpoints)
        self._endpoints.extend(self._collateral.endpoints)
        self._endpoints.extend(self._diagnostic.endpoints)
        self._endpoints.extend(self._federation.endpoints)
        self._endpoints.extend(self._smart_contracts.endpoints)
        self._endpoints.extend(self._smart_contract_wallet.endpoints)
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
