from typing import Union
from pystratis.core.networks import CirrusMain, CirrusTest, CirrusRegTest
from .basenode import BaseNode
from pystratis.api.balances import Balances
from pystratis.api.collateral import Collateral
from pystratis.api.notifications import Notifications
from pystratis.api.federation import Federation
from pystratis.api.smartcontracts import SmartContracts
from pystratis.api.smartcontractwallet import SmartContractWallet
from pystratis.api.voting import Voting


class CirrusMinerNode(BaseNode):
    """A Cirrus Mining Node."""
    def __init__(self, ipaddr: str = 'http://localhost', blockchainnetwork: Union[CirrusMain, CirrusTest, CirrusRegTest] = CirrusMain(), devmode=False):
        """Initialize a Cirrus mining node api.

        Args:
            ipaddr (str, optional: The node's ip address. Default='http://localhost'
            blockchainnetwork (CirrusMain, CirrusTest, CirrusRegTest, optional: The node's network. Default=CirrusMain().
            devmode (bool): Activate devmode, for testing only. Default=False.
        """
        if not isinstance(blockchainnetwork, (CirrusMain, CirrusTest, CirrusRegTest)):
            raise ValueError('Invalid network. Must be one of: [CirrusMain, CirrusTest, CirrusRegTest]')
        super().__init__(name='Cirrus', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)

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
        """The balances route.

        Returns:
            Balances: A Balances instance
        """
        return self._balances

    @property
    def federation(self) -> Federation:
        """The federation route.

        Returns:
            Federation: A Federation instance.
        """
        return self._federation

    @property
    def notifications(self) -> Notifications:
        """The notifications route.

        Return:
            Notifications: A Notifications instance.
        """
        return self._notifications

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
    def voting(self) -> Voting:
        """The voting route.

        Returns:
            Voting: A Voting instance.
        """
        return self._voting
