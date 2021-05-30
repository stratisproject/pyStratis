from pybitcoin.networks import BaseNetwork
from .addressbook import AddressBook
from .balances import Balances
from .blockstore import BlockStore
from .coldstaking import ColdStaking
from .collateral import Collateral
from .collateralvoting import CollateralVoting
from .connectionmanager import ConnectionManager
from .consensus import Consensus
from .dashboard import Dashboard
from .defaultvoting import DefaultVoting
from .diagnostic import Diagnostic
from .federation import Federation
from .federationgateway import FederationGateway
from .federationwallet import FederationWallet
from .interop import Interop
from .mempool import Mempool
from .mining import Mining
from .multisig import Multisig
from .network import Network
from .node import Node
from .notifications import Notifications
from .rpc import RPC
from .signalr import SignalR
from .smartcontracts import SmartContracts
from .smartcontractwallet import SmartContractWallet
from .staking import Staking
from .voting import Voting
from .wallet import Wallet


class API:
    def __init__(self, ipaddr: str, blockchainnetwork: BaseNetwork):
        self._ipaddr = ipaddr
        self._blockchainnetwork = blockchainnetwork
        self._baseuri = f'http://{ipaddr}:{blockchainnetwork.API_PORT}'
        self._addressbook = AddressBook(baseuri=self._baseuri, network=blockchainnetwork)
        self._balances = Balances(baseuri=self._baseuri, network=blockchainnetwork)
        self._blockstore = BlockStore(baseuri=self._baseuri, network=blockchainnetwork)
        self._coldstaking = ColdStaking(baseuri=self._baseuri, network=blockchainnetwork)
        self._collateral = Collateral(baseuri=self._baseuri, network=blockchainnetwork)
        self._collateralvoting = CollateralVoting(baseuri=self._baseuri, network=blockchainnetwork)
        self._connectionmanager = ConnectionManager(baseuri=self._baseuri, network=blockchainnetwork)
        self._consensus = Consensus(baseuri=self._baseuri, network=blockchainnetwork)
        self._dashboard = Dashboard(baseuri=self._baseuri, network=blockchainnetwork)
        self._defaultvoting = DefaultVoting(baseuri=self._baseuri, network=blockchainnetwork)
        self._diagnostic = Diagnostic(baseuri=self._baseuri, network=blockchainnetwork)
        self._federation = Federation(baseuri=self._baseuri, network=blockchainnetwork)
        self._federationgateway = FederationGateway(baseuri=self._baseuri, network=blockchainnetwork)
        self._federationwallet = FederationWallet(baseuri=self._baseuri, network=blockchainnetwork)
        self._interop = Interop(baseuri=self._baseuri, network=blockchainnetwork)
        self._mempool = Mempool(baseuri=self._baseuri, network=blockchainnetwork)
        self._mining = Mining(baseuri=self._baseuri, network=blockchainnetwork)
        self._multisig = Multisig(baseuri=self._baseuri, network=blockchainnetwork)
        self._network = Network(baseuri=self._baseuri, network=blockchainnetwork)
        self._node = Node(baseuri=self._baseuri, network=blockchainnetwork)
        self._notifications = Notifications(baseuri=self._baseuri, network=blockchainnetwork)
        self._rpc = RPC(baseuri=self._baseuri, network=blockchainnetwork)
        self._signalr = SignalR(baseuri=self._baseuri, network=blockchainnetwork)
        self._smartcontracts = SmartContracts(baseuri=self._baseuri, network=blockchainnetwork)
        self._smartcontractwallet = SmartContractWallet(baseuri=self._baseuri, network=blockchainnetwork)
        self._staking = Staking(baseuri=self._baseuri, network=blockchainnetwork)
        self._voting = Voting(baseuri=self._baseuri, network=blockchainnetwork)
        self._wallet = Wallet(baseuri=self._baseuri, network=blockchainnetwork)

    @property
    def ipaddr(self) -> str:
        return self._ipaddr

    @property
    def baseuri(self) -> str:
        return self._baseuri

    @property
    def addressbook(self) -> AddressBook:
        return self._addressbook

    @property
    def balances(self) -> Balances:
        if self.blockchainnetwork.name in ['Strax', 'InterfluxStrax']:
            raise NotImplementedError('Endpoint not implemented in this network.')
        return self._balances

    @property
    def blockstore(self) -> BlockStore:
        return self._blockstore

    @property
    def blockchainnetwork(self) -> BaseNetwork:
        return self._blockchainnetwork

    @property
    def coldstaking(self) -> ColdStaking:
        if self.blockchainnetwork.name in ['Cirrus', 'InterfluxStrax', 'InterfluxCirrus']:
            raise NotImplementedError('Endpoint not implemented in this network.')
        return self._coldstaking

    @property
    def collateral(self) -> Collateral:
        if self.blockchainnetwork.name in ['Strax']:
            raise NotImplementedError('Endpoint not implemented in this network.')
        return self._collateral

    @property
    def collateralvoting(self) -> CollateralVoting:
        if self.blockchainnetwork.name in ['Strax', 'Cirrus']:
            raise NotImplementedError('Endpoint not implemented in this network.')
        return self._collateralvoting

    @property
    def connectionmanager(self) -> ConnectionManager:
        return self._connectionmanager

    @property
    def consensus(self) -> Consensus:
        return self._consensus

    @property
    def dashboard(self) -> Dashboard:
        return self._dashboard

    @property
    def defaultvoting(self) -> DefaultVoting:
        if self.blockchainnetwork.name in ['Strax', 'Cirrus', 'InterfluxStrax']:
            raise NotImplementedError('Endpoint not implemented in this network.')
        return self._defaultvoting

    @property
    def diagnostic(self) -> Diagnostic:
        if self.blockchainnetwork.name in ['InterfluxStrax', 'InterfluxCirrus']:
            raise NotImplementedError('Endpoint not implemented in this network.')
        return self._diagnostic

    @property
    def federation(self) -> Federation:
        if self.blockchainnetwork.name in ['Strax', 'InterfluxStrax', 'InterfluxCirrus']:
            raise NotImplementedError('Endpoint not implemented in this network.')
        return self._federation

    @property
    def federationgateway(self) -> FederationGateway:
        if self.blockchainnetwork.name in ['Strax', 'Cirrus']:
            raise NotImplementedError('Endpoint not implemented in this network.')
        return self._federationgateway

    @property
    def federationwallet(self) -> FederationWallet:
        if self.blockchainnetwork.name in ['Strax', 'Cirrus']:
            raise NotImplementedError('Endpoint not implemented in this network.')
        return self._federationwallet

    @property
    def interop(self) -> Interop:
        if self.blockchainnetwork.name in ['Strax', 'Cirrus', 'InterfluxStrax']:
            raise NotImplementedError('Endpoint not implemented in this network.')
        return self._interop

    @property
    def mempool(self) -> Mempool:
        return self._mempool

    @property
    def mining(self) -> Mining:
        if self.blockchainnetwork.name in ['InterfluxCirrus', 'Cirrus']:
            raise NotImplementedError('Endpoint not implemented in this network.')
        return self._mining

    @property
    def multisig(self) -> Multisig:
        if self.blockchainnetwork.name in ['Strax', 'Cirrus']:
            raise NotImplementedError('Endpoint not implemented in this network.')
        return self._multisig

    @property
    def network(self) -> Network:
        return self._network

    @property
    def node(self) -> Node:
        return self._node

    @property
    def notifications(self) -> Notifications:
        if self.blockchainnetwork.name in ['Strax', 'Cirrus']:
            raise NotImplementedError('Endpoint not implemented in this network.')
        return self._notifications

    @property
    def rpc(self) -> RPC:
        return self._rpc

    @property
    def signalr(self) -> SignalR:
        if self.blockchainnetwork.name in ['InterfluxStrax', 'InterfluxCirrus']:
            raise NotImplementedError('Endpoint not implemented in this network.')
        return self._signalr

    @property
    def smartcontracts(self) -> SmartContracts:
        if self.blockchainnetwork.name in ['Strax', 'InterfluxStrax']:
            raise NotImplementedError('Endpoint not implemented in this network.')
        return self._smartcontracts

    @property
    def smartcontractwallet(self) -> SmartContractWallet:
        if self.blockchainnetwork.name in ['Strax', 'InterfluxStrax']:
            raise NotImplementedError('Endpoint not implemented in this network.')
        return self._smartcontractwallet

    @property
    def staking(self) -> Staking:
        if self.blockchainnetwork.name in ['Cirrus', 'InterfluxCirrus']:
            raise NotImplementedError('Endpoint not implemented in this network.')
        return self._staking

    @property
    def voting(self) -> Voting:
        if self.blockchainnetwork.name in ['Strax', 'InterfluxStrax', 'InterfluxCirrus']:
            raise NotImplementedError('Endpoint not implemented in this network.')
        return self._voting

    @property
    def wallet(self) -> Wallet:
        return self._wallet
