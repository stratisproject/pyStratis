from pybitcoin.networks import BaseNetwork, CirrusMain, CirrusTest, CirrusRegTest
from .basenode import BaseNode


# TODO
class CirrusNode(BaseNode):
    def __init__(self, ipaddr: str = 'https://localhost', blockchainnetwork: BaseNetwork = CirrusMain()):
        super(CirrusNode, self).__init__(name='Cirrus', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)


class CirrusTestNode(BaseNode):
    def __init__(self, ipaddr: str = 'https://localhost', blockchainnetwork: BaseNetwork = CirrusTest()):
        super(CirrusTestNode, self).__init__(name='CirrusTest', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)


class CirrusRegTestNode(BaseNode):
    def __init__(self, ipaddr: str = 'https://localhost', blockchainnetwork: BaseNetwork = CirrusRegTest()):
        super(CirrusRegTestNode, self).__init__(name='CirrusRegTest', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)
