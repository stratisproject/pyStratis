from typing import Union
from pystratis.core.networks import CirrusMain, CirrusTest, CirrusRegTest, StraxMain, StraxTest, StraxRegTest
from .basenode import BaseNode
from pystratis.api.balances import Balances
from pystratis.api.collateral import Collateral
from pystratis.api.notifications import Notifications
from pystratis.api.federation import Federation
from pystratis.api.smartcontracts import SmartContracts
from pystratis.api.smartcontractwallet import SmartContractWallet
from pystratis.api.voting import Voting


class CirrusMinerNode(BaseNode):
    """A CirrusMiner Node."""
    def __init__(self,
                 name: str = 'CirrusMiner',
                 ipaddr: str = 'http://localhost',
                 blockchainnetwork: Union[CirrusMain, CirrusTest, CirrusRegTest, StraxMain, StraxTest, StraxRegTest] = None, devmode=False):
        """Initialize a standard masternode node api.

        Args:
            name (str): The name of the node.
            ipaddr (str, optional: The node's ip address. Default='http://localhost'
            blockchainnetwork (CirrusMain, CirrusTest, CirrusRegTest, StraxMain, StraxTest, StraxRegTest, optional: The node's network. Default=None.
            devmode (bool): Activate devmode, for testing only. Default=False.
        """
        if not isinstance(blockchainnetwork, (CirrusMain, CirrusTest, CirrusRegTest, StraxMain, StraxTest, StraxRegTest)):
            raise ValueError('Invalid network. Must be one of: [CirrusMain, CirrusTest, CirrusRegTest, StraxMain, StraxTest, StraxRegTest]')
        super().__init__(name=name, ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)
        self._devmode = devmode

        # API endpoints
        self._balances = Balances(baseuri=self.api_route, network=blockchainnetwork)
        if not devmode:
            self._collateral = Collateral(baseuri=self.api_route, network=blockchainnetwork)
            self._endpoints.extend(self._collateral.endpoints)
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
    def collateral(self) -> Collateral:
        """The collateral route. Not available in devmode.

        Returns:
            Collateral: A Collateral instance.
        """
        if self._devmode:
            raise NotImplementedError('Not implemented in devmode cirrus miner node.')
        return self._collateral

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


class StraxMasterNode(CirrusMinerNode):
    """The Strax member of the masternode pair."""
    def __init__(self, ipaddr: str = 'http://localhost', blockchainnetwork: Union[StraxMain, StraxTest, StraxRegTest] = StraxMain()):
        super().__init__(name='StraxMasternode', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)


class CirrusMasterNode(CirrusMinerNode):
    """The Cirrus member of the masternode pair."""
    def __init__(self, ipaddr: str = 'http://localhost', blockchainnetwork: Union[CirrusMain, CirrusTest, CirrusRegTest] = CirrusMain()):
        super().__init__(name='CirrusMasternode', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)
