from enum import IntEnum


class ContractTransactionItemType(IntEnum):
    """A ContractTransactionItemType."""
    Received = 0
    Send = 1
    Staked = 2
    ContractCall = 3
    ContractCreate = 4
    GasRefund = 5
