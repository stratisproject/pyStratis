from typing import List
import requests
from pybitcoin.networks import BaseNetwork
from api.addressbook import AddressBook
from api.blockstore import BlockStore
from api.connectionmanager import ConnectionManager
from api.consensus import Consensus
from api.dashboard import Dashboard
from api.mempool import Mempool
from api.network import Network
from api.node import Node
from api.rpc import RPC
from api.wallet import Wallet


class BaseNode:
    """The core node functionality.

    Strax, Cirrus, and Interflux nodes use different controllers that are added in subclasses.
    """
    def __init__(self, name: str, ipaddr: str, blockchainnetwork: BaseNetwork):
        self._name = name
        self._ipaddr = ipaddr
        self._blockchainnetwork = blockchainnetwork
        self._api_schema_endpoint = '/swagger/v1/swagger.json'

        # API endpoints
        self._addressbook = AddressBook(baseuri=self.api_route, network=blockchainnetwork)
        self._blockstore = BlockStore(baseuri=self.api_route, network=blockchainnetwork)
        self._connection_manager = ConnectionManager(baseuri=self.api_route, network=blockchainnetwork)
        self._consensus = Consensus(baseuri=self.api_route, network=blockchainnetwork)
        self._dashboard = Dashboard(baseuri=self.api_route, network=blockchainnetwork)
        self._mempool = Mempool(baseuri=self.api_route, network=blockchainnetwork)
        self._network = Network(baseuri=self.api_route, network=blockchainnetwork)
        self._node = Node(baseuri=self.api_route, network=blockchainnetwork)
        self._rpc = RPC(baseuri=self.api_route, network=blockchainnetwork)
        self._wallet = Wallet(baseuri=self.api_route, network=blockchainnetwork)

        self._endpoints = [
            *self._addressbook.endpoints,
            *self._blockstore.endpoints,
            *self._connection_manager.endpoints,
            *self._consensus.endpoints,
            *self._dashboard.endpoints,
            *self._mempool.endpoints,
            *self._network.endpoints,
            *self._node.endpoints,
            *self._rpc.endpoints,
            *self._wallet.endpoints,
        ]

    @property
    def name(self) -> str:
        return self._name

    @property
    def ipaddr(self) -> str:
        return self._ipaddr

    @property
    def blockchainnetwork(self) -> BaseNetwork:
        return self._blockchainnetwork

    @property
    def api_route(self) -> str:
        return f'{self.ipaddr}:{self.blockchainnetwork.API_PORT}'

    @property
    def endpoints(self) -> List[str]:
        return self._endpoints

    @property
    def addressbook(self) -> AddressBook:
        return self._addressbook

    @property
    def blockstore(self) -> BlockStore:
        return self._blockstore

    @property
    def connection_manager(self) -> ConnectionManager:
        return self._connection_manager

    @property
    def consensus(self) -> Consensus:
        return self._consensus

    @property
    def dashboard(self) -> Dashboard:
        return self._dashboard

    @property
    def mempool(self) -> Mempool:
        return self._mempool

    @property
    def network(self) -> Network:
        return self._network

    @property
    def node(self) -> Node:
        return self._node

    @property
    def rpc(self) -> RPC:
        return self._rpc

    @property
    def wallet(self) -> Wallet:
        return self._wallet

    def check_all_endpoints_implemented(self) -> bool:
        request_url = f'{self.api_route}{self._api_schema_endpoint}'
        response = requests.get(
            url=request_url,
            params=None,
            headers={'Accept': '*/*', 'Content-Type': 'application/json'},
            timeout=5
        )
        swagger_schema = response.json()
        paths = [key.lower() for key in swagger_schema['paths']]
        if len([x for x in set(self.endpoints) if x not in set(paths)]) != 0:
            print(f'API endpoints not found in swagger json: {[x for x in set(self.endpoints) if x not in set(paths)]}')
        if len([x for x in set(paths) if x not in set(self.endpoints)]) != 0:
            print(f'Swagger paths not mapped by API: {[x for x in set(paths) if x not in set(self.endpoints)]}')
        return set(self.endpoints) == set(paths)
