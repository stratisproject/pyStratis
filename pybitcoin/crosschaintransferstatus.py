from enum import Enum


class CrossChainTransferStatus(str, Enum):
    """Enum representing status of cross chain status.
    
    Corresponding type from StratisFullNode's implementation can be found here__.

    .. __:
        https://github.com/stratisproject/StratisFullNode/blob/master/src/Stratis.Features.FederatedPeg/Interfaces/ICrossChainTransfer.cs#L8
    """
    Suspended = 'Suspended'
    Partial = 'Partial'
    FullySigned = 'FullySigned'
    SeenInBlock = 'SeenInBlock'
    Rejected = 'Rejected'
