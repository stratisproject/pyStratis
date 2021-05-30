from pybitcoin.networks import BaseNetwork
from api import APIRequest


class BaseNode:
    """A base node description"""
    def __init__(self, name: str, ipaddr: str, blockchainnetwork: BaseNetwork):
        self._name = name
        self._ipaddr = ipaddr
        self._blockchainnetwork = blockchainnetwork
        self._api = APIRequest(baseuri=ipaddr, network=blockchainnetwork)
        self._api_schema_endpoint = '/swagger/v1/swagger.json'

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
    def api(self) -> APIRequest:
        return self._api
