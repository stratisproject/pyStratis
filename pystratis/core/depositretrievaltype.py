from enum import IntEnum


class DepositRetrievalType(IntEnum):
    """Represents type of deposit retrival.

    Small deposits are processed after `IFederatedPegSettings.MinimumConfirmationsSmallDeposits`_ confirmations (blocks).

    Normal deposits are processed after `IFederatedPegSettings.MinimumConfirmationsNormalDeposits`_ confirmations (blocks).

    Large deposits are only processed after the height has increased past max 
    re-org (`IFederatedPegSettings.MinimumConfirmationsLargeDeposits`_) confirmations (blocks).

    Conversion deposits are processed after similar intervals to the above, according to their size.

    Reward distribution deposits are only processed after the height 
    has increased past max re-org (`IFederatedPegSettings.MinimumConfirmationsDistributionDeposits`_) 
    confirmations (blocks).

    .. _IFederatedPegSettings.MinimumConfirmationsSmallDeposits:
        https://github.com/stratisproject/StratisFullNode/blob/master/src/Stratis.Features.FederatedPeg/Interfaces/IFederatedPegSettings.cs#L69
    .. _IFederatedPegSettings.MinimumConfirmationsNormalDeposits:
        https://github.com/stratisproject/StratisFullNode/blob/master/src/Stratis.Features.FederatedPeg/Interfaces/IFederatedPegSettings.cs#L77
    .. _IFederatedPegSettings.MinimumConfirmationsLargeDeposits: 
        https://github.com/stratisproject/StratisFullNode/blob/master/src/Stratis.Features.FederatedPeg/Interfaces/IFederatedPegSettings.cs#L85
    .. _IFederatedPegSettings.MinimumConfirmationsDistributionDeposits: 
        https://github.com/stratisproject/StratisFullNode/blob/master/src/Stratis.Features.FederatedPeg/Interfaces/IFederatedPegSettings.cs#L87
    """
    Small = 0
    Normal = 1
    Large = 2
    Distribution = 3
    ConversionSmall = 4,
    ConversionNormal = 5
    ConversionLarge = 6
