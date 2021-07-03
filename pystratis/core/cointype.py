from enum import IntEnum


class CoinType(IntEnum):
    """Enum representing type of coin, as specified in BIP44_.
    Registered cointypes specified in SLIP44_.

    Corresponding type from StratisFullNode's implementation can be found here__.

    Note:
        Coin type for Cirrus mainnet is not a registered coin type (as well as testnets).
        According to SLIP44_, ID 401 belongs to another coin, that has nothing to do with Statis Platform.

    .. _BIP44: 
        https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki

    .. _SLIP44: 
        https://github.com/satoshilabs/slips/blob/master/slip-0044.md

    .. __: 
        https://github.com/stratisproject/StratisFullNode/blob/master/src/Stratis.Bitcoin.Features.Wallet/CoinType.cs#L7
    """
    Bitcoin = 0  # mainnet
    Testnet = 1  # testnet, strax testnet
    CirrusTest = 400  # Cirrus testnet
    Cirrus = 401  # Cirrus mainnet
    Strax = 105105  # Strax mainnet
