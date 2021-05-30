from enum import IntEnum


class CoinType(IntEnum):
    """A CoinYype."""
    Bitcoin = 0  # mainnet
    Testnet = 1  # testnet
    Strax = 105105  # Strax mainnet
