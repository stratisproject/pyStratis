from enum import IntEnum


class DestinationChain(IntEnum):
    """Chains supported by InterFlux integration.
    Symbols are defined according to the `SLIP44 specification`__.
    
    .. __: https://github.com/satoshilabs/slips/blob/master/slip-0044.md
    """
    STRAX = 0
    ETH = 1
    BNB = 2
    ETC = 3
    AVAX = 4
    ADA = 5
