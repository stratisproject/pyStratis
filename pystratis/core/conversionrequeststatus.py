from enum import IntEnum


class ConversionRequestStatus(IntEnum):
    """Enum representing status of interop conversion request.
    
    Corresponding type from StratisFullNode's implementation can be found here__.

    .. __:
        https://github.com/stratisproject/StratisFullNode/blob/master/src/Stratis.Features.FederatedPeg/Conversion/ConversionRequest.cs#L11
    """
    Unprocessed = 0
    Submitted = 1
    Processed = 2
    OriginatorNotSubmitted = 3
    OriginatorSubmitted = 4
    VoteFinalised = 5
    NotOriginator = 6
