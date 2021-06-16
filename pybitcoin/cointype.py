from enum import IntEnum


class CoinType(IntEnum):
    """A CoinYype."""
    Bitcoin = 0  # mainnet
    Testnet = 1  # testnet, strax testnet
    CirrusTest = 400  # Cirrus testnet
    Cirrus = 401  # Cirrus mainnet
    Strax = 105105  # Strax mainnet
