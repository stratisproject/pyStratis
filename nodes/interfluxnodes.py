from .basenode import BaseNode
from pybitcoin.networks import BaseNetwork, CirrusMain, StraxMain


# TODO
class InterfluxStraxNode(BaseNode):
    def __init__(self, ipaddr: str = 'https://localhost', blockchainnetwork: BaseNetwork = StraxMain()):
        super(InterfluxStraxNode, self).__init__(name='InterfluxStrax', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)


class InterfluxCirrusNode(BaseNode):
    def __init__(self, ipaddr: str = 'https://localhost', blockchainnetwork: BaseNetwork = CirrusMain()):
        super(InterfluxCirrusNode, self).__init__(name='InterfluxCirrus', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)
