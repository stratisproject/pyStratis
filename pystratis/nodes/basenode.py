from typing import List
import requests
from requests.exceptions import ConnectionError
from pystratis.core.networks import BaseNetwork
from pystratis.api.addressbook import AddressBook
from pystratis.api.blockstore import BlockStore
from pystratis.api.connectionmanager import ConnectionManager
from pystratis.api.consensus import Consensus
from pystratis.api.dashboard import Dashboard
from pystratis.api.mempool import Mempool
from pystratis.api.network import Network
from pystratis.api.node import Node
from pystratis.api.rpc import RPC
from pystratis.api.wallet import Wallet


class BaseNode:
    """The core node functionality.

    Strax, Cirrus, and Interflux nodes use different controllers that are added in subclasses.
    """
    def __init__(self, name: str, ipaddr: str, blockchainnetwork: BaseNetwork):
        """A Node base class.

        Args:
            name (str): The name of the node.
            ipaddr (str): The node's ip address.
            blockchainnetwork (StraxMain, StraxTest, StraxRegTest, CirrusMain, CirrusTest, CirrusRegTest): The node's network.
        """
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

    def stop_node(self) -> bool:
        """Convenience method for stopping node."""
        try:
            self.node.stop()
        except ConnectionError:
            # Thrown if trying to stop a node that is already stopped.
            pass
        return True

    @property
    def name(self) -> str:
        """The node's name.

        Returns:
            str: The node name.
        """
        return self._name

    @property
    def ipaddr(self) -> str:
        """The node's ip address.

        Returns:
            str: The specified ip address of the node.
        """
        return self._ipaddr

    @property
    def blockchainnetwork(self) -> BaseNetwork:
        """The node's network type.

        Returns:
            BaseNetwork: The node's network.
        """
        return self._blockchainnetwork

    @property
    def api_route(self) -> str:
        """The node's api route.

        Returns:
            str: The api uri.
        """
        return f'{self.ipaddr}:{self.blockchainnetwork.API_PORT}'

    @property
    def endpoints(self) -> List[str]:
        """The list of endpoints active for the node.

        Returns:
            List[str]: A list of endpoints active in the node API.
        """
        return self._endpoints

    @property
    def addressbook(self) -> AddressBook:
        """The addressbook route.

        Returns:
            AddressBook: An addressbook instance.
        """
        return self._addressbook

    @property
    def blockstore(self) -> BlockStore:
        """The blockstore route.

        Returns:
            BlockStore: A BlockStore instance.
        """
        return self._blockstore

    @property
    def connection_manager(self) -> ConnectionManager:
        """The connectionmanager route.

        Returns:
            ConnectionManager: A ConnectionManager instance.
        """
        return self._connection_manager

    @property
    def consensus(self) -> Consensus:
        """The consensus route.

        Returns:
            Consensus: A Consensus instance.
        """
        return self._consensus

    @property
    def dashboard(self) -> Dashboard:
        """The dashboard route.

        Returns:
            Dashboard: A Dashboard instance.
        """
        return self._dashboard

    @property
    def mempool(self) -> Mempool:
        """The mempool route.

        Returns:
            Mempool: A Mempool instance.
        """
        return self._mempool

    @property
    def network(self) -> Network:
        """The netowrk route.

        Returns:
            Network: A Network instance.
        """
        return self._network

    @property
    def node(self) -> Node:
        """The node route.

        Returns:
            Node: A Node instance.
        """
        return self._node

    @property
    def rpc(self) -> RPC:
        """The RPC route.

        Returns:
            RPC: A RPC instance.
        """
        return self._rpc

    @property
    def wallet(self) -> Wallet:
        """The wallet route.

        Returns:
            Wallet: A Wallet instance.
        """
        return self._wallet

    def check_all_endpoints_implemented(self) -> bool:
        """Queries a running node's swagger schema and compares the pystratis implemented endpoints with those defined by the swagger schema.

        Returns:
            bool: True if all endpoints are implemented, otherwise False.
        """
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
