from enum import IntEnum


class ConversionRequestStatus(IntEnum):
    Unprocessed = 0
    Submitted = 1
    Processed = 2
    OriginatorNotSubmitted = 3
    OriginatorSubmitted = 4
    VoteFinalised = 5
    NotOriginator = 6
