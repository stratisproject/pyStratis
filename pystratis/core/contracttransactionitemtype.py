from enum import IntEnum


class ContractTransactionItemType(IntEnum):
    """Enum representing type of contract-related transaction item.
    
    Corresponding type from StratisFullNode's implementation can be found here_.

    .. _here:
        https://github.com/stratisproject/StratisFullNode/blob/master/src/Stratis.Bitcoin.Features.SmartContracts/Wallet/ContractTransactionItemType.cs#L3
    """
    Received = 0
    Send = 1
    Staked = 2
    ContractCall = 3
    ContractCreate = 4
    GasRefund = 5
