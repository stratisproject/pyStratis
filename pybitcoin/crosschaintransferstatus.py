from enum import Enum


class CrossChainTransferStatus(str, Enum):
    Suspended = 'U'
    Partial = 'P'
    FullySigned = 'F'
    SeenInBlock = 'S'
    Rejected = 'R'
