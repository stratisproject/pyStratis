from pybitcoin.networks import BaseNetwork, StraxMain
from .basenode import BaseNode


# TODO
class StraxNode(BaseNode):
    def __init__(self, ipaddr: str = 'https://localhost', blockchainnetwork: BaseNetwork = StraxMain()):
        super(StraxNode, self).__init__(name='Strax', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)
