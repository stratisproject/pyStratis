from enum import Enum


class TransactionItemType(str, Enum):
    """A TransactionItemType."""
    Received = 'received'
    Send = 'send'
    Staked = 'staked'
    Mined = 'mined'
