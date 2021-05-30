from enum import IntEnum


class TransactionItemType(IntEnum):
    """ATransactionItemType."""
    Received = 0
    Send = 1
    Staked = 2
    Mined = 3
