from pybitcoin.networks import BaseNetwork, StraxMain, StraxTest, StraxRegTest
from .basenode import BaseNode


# TODO
class StraxNode(BaseNode):
    def __init__(self, ipaddr: str = 'https://localhost', blockchainnetwork: BaseNetwork = StraxMain()):
        super(StraxNode, self).__init__(name='Strax', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)


class StraxTestNode(BaseNode):
    def __init__(self, ipaddr: str = 'https://localhost', blockchainnetwork: BaseNetwork = StraxTest()):
        super(StraxTestNode, self).__init__(name='StraxTest', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)


class StraxRegTestNode(BaseNode):
    def __init__(self, ipaddr: str = 'https://localhost', blockchainnetwork: BaseNetwork = StraxRegTest()):
        super(StraxRegTestNode, self).__init__(name='StraxRegTest', ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)
