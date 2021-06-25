from enum import IntEnum


class ConversionRequestType(IntEnum):
    """Enum representing type of interop conversion request.
    
    Corresponding type from StratisFullNode's implementation can be found here__.

    .. __:
        https://github.com/stratisproject/StratisFullNode/blob/master/src/Stratis.Features.FederatedPeg/Conversion/ConversionRequest.cs#L5
    """
    Mint = 0
    Burn = 1
