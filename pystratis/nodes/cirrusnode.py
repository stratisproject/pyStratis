from typing import Union
from pystratis.core.networks import CirrusMain, CirrusTest, CirrusRegTest
from .basenode import BaseNode
from pystratis.api.balances import Balances
from pystratis.api.collateral import Collateral
from pystratis.api.diagnostic import Diagnostic
from pystratis.api.federation import Federation
from pystratis.api.smartcontracts import SmartContracts
from pystratis.api.smartcontractwallet import SmartContractWallet
from pystratis.api.signalr import SignalR
from pystratis.api.voting import Voting


class CirrusNode(BaseNode):
    """A Cirrus Node."""
    def __init__(self, ipaddr: str = 'http://localhost', blockchainnetwork: Union[CirrusMain, CirrusTest, CirrusRegTest] = CirrusMain()):
        """Initialize a Cirrus node api.

        Args:
            ipaddr (str, optional): The node's ip address. Default='http://localhost'
            blockchainnetwork (CirrusMain, CirrusTest, CirrusRegTest, optional): The node's network. Default=CirrusMain().
        """
        if not isinstance(blockchainnetwork, (CirrusMain, CirrusTest, CirrusRegTest)):
            raise ValueError('Invalid network. Must be one of: [CirrusMain, CirrusTest, CirrusRegTest]')
        super().__init__(name='Cirrus', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)

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
        """The balances route.

        Returns:
            Balances: A Balances instance.
        """
        return self._balances

    @property
    def collateral(self) -> Collateral:
        """The collateral route.

        Returns:
            Collateral: A Collateral instance.
        """
        return self._collateral

    @property
    def diagnostic(self) -> Diagnostic:
        """The diagnostic route.

        Returns:
            Diagnostic: A Diagnostic instance.
        """
        return self._diagnostic

    @property
    def federation(self) -> Federation:
        """The federation route.

        Returns:
            Federation: A Federation instance.
        """
        return self._federation

    @property
    def smart_contracts(self) -> SmartContracts:
        """The smartcontracts route.

        Returns:
            SmartContracts: A SmartContracts instance.
        """
        return self._smart_contracts

    @property
    def smart_contract_wallet(self) -> SmartContractWallet:
        """The smartcontractwallet route.

        Returns:
            SmartContractWallet: A SmartContractWallet instance.
        """
        return self._smart_contract_wallet

    @property
    def signalr(self) -> SignalR:
        """The signalr route.

        Returns:
            SignalR: A SignalR instance.
        """
        return self._signalr

    @property
    def voting(self) -> Voting:
        """The voting route.

        Returns:
            Voting: A Voting instance.
        """
        return self._voting
