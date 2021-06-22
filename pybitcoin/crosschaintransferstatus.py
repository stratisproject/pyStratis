from enum import Enum


class CrossChainTransferStatus(str, Enum):
    Suspended = 'Suspended'
    Partial = 'Partial'
    FullySigned = 'FullySigned'
    SeenInBlock = 'SeenInBlock'
    Rejected = 'Rejected'
