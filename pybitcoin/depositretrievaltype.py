from enum import IntEnum


class DepositRetrievalType(IntEnum):
    """A DepositRetrievalType."""
    Small = 0
    Normal = 1
    Large = 2
    Distribution = 3
    ConversionSmall = 4,
    ConversionNormal = 5
    ConversionLarge = 6
