from pystratis.core.networks import BaseNetwork, StraxMain, StraxTest, StraxRegTest
from .basenode import BaseNode
from pystratis.api.coldstaking import ColdStaking
from pystratis.api.diagnostic import Diagnostic
from pystratis.api.mining import Mining
from pystratis.api.signalr import SignalR
from pystratis.api.staking import Staking


class StraxNode(BaseNode):
    def __init__(self, ipaddr: str = 'http://localhost', blockchainnetwork: BaseNetwork = StraxMain()):
        if not isinstance(blockchainnetwork, (StraxMain, StraxTest, StraxRegTest)):
            raise ValueError('Invalid network. Must be one of: [StraxMain, StraxTest, StraxRegTest]')
        super().__init__(name='Strax', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)

        # API endpoints
        self._coldstaking = ColdStaking(baseuri=self.api_route, network=blockchainnetwork)
        self._diagnostic = Diagnostic(baseuri=self.api_route, network=blockchainnetwork)
        self._mining = Mining(baseuri=self.api_route, network=blockchainnetwork)
        self._signalr = SignalR(baseuri=self.api_route, network=blockchainnetwork)
        self._staking = Staking(baseuri=self.api_route, network=blockchainnetwork)

        # Add Strax specific endpoints to superclass endpoints.
        self._endpoints.extend(self._coldstaking.endpoints)
        self._endpoints.extend(self._diagnostic.endpoints)
        self._endpoints.extend(self._mining.endpoints)
        self._endpoints.extend(self._signalr.endpoints)
        self._endpoints.extend(self._staking.endpoints)
        self._endpoints.sort()

    @property
    def coldstaking(self) -> ColdStaking:
        return self._coldstaking

    @property
    def diagnostic(self) -> Diagnostic:
        return self._diagnostic

    @property
    def mining(self) -> Mining:
        return self._mining

    @property
    def signalr(self) -> SignalR:
        return self._signalr

    @property
    def staking(self) -> Staking:
        return self._staking
