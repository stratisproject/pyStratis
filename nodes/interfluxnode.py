from pybitcoin.networks import BaseNetwork, CirrusMain, StraxMain, CirrusTest, StraxTest, StraxRegTest, CirrusRegTest
from .basenode import BaseNode


# TODO
class InterfluxStraxNode(BaseNode):
    def __init__(self, ipaddr: str = 'https://localhost', blockchainnetwork: BaseNetwork = StraxMain()):
        super(InterfluxStraxNode, self).__init__(name='InterfluxStrax', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)


class InterfluxCirrusNode(BaseNode):
    def __init__(self, ipaddr: str = 'https://localhost', blockchainnetwork: BaseNetwork = CirrusMain()):
        super(InterfluxCirrusNode, self).__init__(name='InterfluxCirrus', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)


class InterfluxStraxTestNode(BaseNode):
    def __init__(self, ipaddr: str = 'https://localhost', blockchainnetwork: BaseNetwork = StraxTest()):
        super(InterfluxStraxTestNode, self).__init__(name='InterfluxStraxTest', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)


class InterfluxCirrusTestNode(BaseNode):
    def __init__(self, ipaddr: str = 'https://localhost', blockchainnetwork: BaseNetwork = CirrusTest()):
        super(InterfluxCirrusTestNode, self).__init__(name='InterfluxCirrusTest', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)


class InterfluxStraxRegTestNode(BaseNode):
    def __init__(self, ipaddr: str = 'https://localhost', blockchainnetwork: BaseNetwork = StraxRegTest()):
        super(InterfluxStraxRegTestNode, self).__init__(name='InterfluxStraxRegTest', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)


class InterfluxCirrusRegTestNode(BaseNode):
    def __init__(self, ipaddr: str = 'https://localhost', blockchainnetwork: BaseNetwork = CirrusRegTest()):
        super(InterfluxCirrusRegTestNode, self).__init__(name='InterfluxCirrusRegTest', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)
