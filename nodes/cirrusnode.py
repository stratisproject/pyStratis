from pybitcoin.networks import BaseNetwork, CirrusMain
from .basenode import BaseNode


# TODO
class CirrusNode(BaseNode):
    def __init__(self, ipaddr: str = 'https://localhost', blockchainnetwork: BaseNetwork = CirrusMain()):
        super(CirrusNode, self).__init__(name='Cirrus', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)

