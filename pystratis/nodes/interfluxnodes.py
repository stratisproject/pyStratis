from typing import Union
from .basenode import BaseNode
from pystratis.core.networks import CirrusMain, CirrusTest, CirrusRegTest, StraxTest, StraxRegTest, StraxMain
from pystratis.api.collateral import Collateral
from pystratis.api.collateralvoting import CollateralVoting
from pystratis.api.federationgateway import FederationGateway
from pystratis.api.federationwallet import FederationWallet
from pystratis.api.mining import Mining
from pystratis.api.multisig import Multisig
from pystratis.api.notifications import Notifications
from pystratis.api.staking import Staking
from pystratis.api.balances import Balances
from pystratis.api.federation import Federation
from pystratis.api.interop import Interop
from pystratis.api.smartcontracts import SmartContracts
from pystratis.api.smartcontractwallet import SmartContractWallet
from pystratis.api.voting import Voting


class InterfluxStraxNode(BaseNode):
    """A Interflux Strax Node."""
    def __init__(self, ipaddr: str = 'http://localhost', blockchainnetwork: Union[StraxTest, StraxRegTest, StraxMain] = StraxMain()):
        """Initialize a InterfluxStrax node api.

        Args:
            ipaddr (str, optional): The node's ip address. Default='http://localhost'
            blockchainnetwork (StraxTest, StraxRegTest, StraxMain, optional): The node's network. Default=StraxMain().
        """
        if not isinstance(blockchainnetwork, (StraxMain, StraxTest, StraxRegTest)):
            raise ValueError('Invalid network. Must be one of: [StraxMain, StraxTest, StraxRegTest]')
        super().__init__(name='InterfluxStrax', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)

        # API endpoints
        self._collateral = Collateral(baseuri=self.api_route, network=blockchainnetwork)
        self._collateral_voting = CollateralVoting(baseuri=self.api_route, network=blockchainnetwork)
        self._federation_gateway = FederationGateway(baseuri=self.api_route, network=blockchainnetwork)
        self._federation_wallet = FederationWallet(baseuri=self.api_route, network=blockchainnetwork)
        self._mining = Mining(baseuri=self.api_route, network=blockchainnetwork)
        self._multisig = Multisig(baseuri=self.api_route, network=blockchainnetwork)
        self._notifications = Notifications(baseuri=self.api_route, network=blockchainnetwork)
        self._staking = Staking(baseuri=self.api_route, network=blockchainnetwork)

        # Add InterfluxStrax specific endpoints to superclass endpoints.
        self._endpoints.extend(self._collateral.endpoints)
        self._endpoints.extend(self._collateral_voting.endpoints)
        self._endpoints.extend(self._federation_gateway.endpoints)
        self._endpoints.extend(self._federation_wallet.endpoints)
        self._endpoints.extend(self._mining.endpoints)
        self._endpoints.extend(self._multisig.endpoints)
        self._endpoints.extend(self._notifications.endpoints)
        self._endpoints.extend(self._staking.endpoints)
        self._endpoints.sort()

    @property
    def collateral(self) -> Collateral:
        """The collateral route.

        Returns:
            Collateral: A Collateral instance.
        """
        return self._collateral

    @property
    def collateral_voting(self) -> CollateralVoting:
        """The collateralvoting route.

        Returns:
            CollateralVoting: A CollateralVoting instance.
        """
        return self._collateral_voting

    @property
    def federation_gateway(self) -> FederationGateway:
        """The federationgateway route.

        Returns:
            FederationGateway: A FederationGateway instance.
        """
        return self._federation_gateway

    @property
    def federation_wallet(self) -> FederationWallet:
        """The federationwallet route.

        Returns:
            FederationWallet: A FederationWallet instance.
        """
        return self._federation_wallet

    @property
    def mining(self) -> Mining:
        """The mining route.

        Returns:
            Mining: A Mining instance.
        """
        return self._mining

    @property
    def multisig(self) -> Multisig:
        """The multisig route.

        Returns:
            Multisig: A Multisig instance.
        """
        return self._multisig

    @property
    def notifications(self) -> Notifications:
        """The notifications route.

        Returns:
            Notifications: A Notificiations instance.
        """
        return self._notifications

    @property
    def staking(self) -> Staking:
        """The staking route."

        Returns:
            Staking: A Staking instance.
        """
        return self._staking


class InterfluxCirrusNode(BaseNode):
    """An Interflux Cirrus node."""
    def __init__(self, ipaddr: str = 'http://localhost', blockchainnetwork: Union[CirrusMain, CirrusTest, CirrusRegTest] = CirrusMain()):
        """Initialize an Interflux Cirrus node api.

        Args:
            ipaddr (str, optional): The node's ip address. Default='http://localhost'
            blockchainnetwork (CirrusMain, CirrusTest, CirrusRegTest, optional): The node's network. Default=CirrusMain().
        """
        if not isinstance(blockchainnetwork, (CirrusMain, CirrusTest, CirrusRegTest)):
            raise ValueError('Invalid network. Must be one of: [CirrusMain, CirrusTest, CirrusRegTest]')
        super().__init__(name='InterfluxCirrus', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)

        # API endpoints
        self._balances = Balances(baseuri=self.api_route, network=blockchainnetwork)
        self._collateral = Collateral(baseuri=self.api_route, network=blockchainnetwork)
        self._collateral_voting = CollateralVoting(baseuri=self.api_route, network=blockchainnetwork)
        self._federation = Federation(baseuri=self.api_route, network=blockchainnetwork)
        self._federation_gateway = FederationGateway(baseuri=self.api_route, network=blockchainnetwork)
        self._federation_wallet = FederationWallet(baseuri=self.api_route, network=blockchainnetwork)
        self._interop = Interop(baseuri=self.api_route, network=blockchainnetwork)
        self._multisig = Multisig(baseuri=self.api_route, network=blockchainnetwork)
        self._notifications = Notifications(baseuri=self.api_route, network=blockchainnetwork)
        self._smart_contracts = SmartContracts(baseuri=self.api_route, network=blockchainnetwork)
        self._smart_contract_wallet = SmartContractWallet(baseuri=self.api_route, network=blockchainnetwork)
        self._voting = Voting(baseuri=self.api_route, network=blockchainnetwork)

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
        self._endpoints.extend(self._notifications.endpoints)
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
    def collateral_voting(self) -> CollateralVoting:
        """The collateralvoting route.

        Returns:
            CollateralVoting: A CollateralVoting instance.
        """
        return self._collateral_voting

    @property
    def federation(self) -> Federation:
        """The federation route.

        Returns:
            Federation: A Federation instance.
        """
        return self._federation

    @property
    def federation_gateway(self) -> FederationGateway:
        """The federationgateway route.

        Returns:
            FederationGateway: A FederationGateway instance.
        """
        return self._federation_gateway

    @property
    def federation_wallet(self) -> FederationWallet:
        """The federationwallet route.

        Returns:
            FederationWallet: A FederationWallet instance.
        """
        return self._federation_wallet

    @property
    def interop(self) -> Interop:
        """The interop route.


        Returns:
            Interop: An Interop instance.
        """
        return self._interop

    @property
    def multisig(self) -> Multisig:
        """The multisig route.

        Returns:
            Multisig: A Multisig instance.
        """
        return self._multisig

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
    def notifications(self) -> Notifications:
        """The notifications route.

        Returns:
            Notifications: A Notifications instance.
        """
        return self._notifications

    @property
    def voting(self) -> Voting:
        """The voting route.

        Returns:
            Voting: A Voting instance.
        """
        return self._voting
