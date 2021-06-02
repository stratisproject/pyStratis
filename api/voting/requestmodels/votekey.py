from enum import IntEnum


class VoteKey(IntEnum):
    KickFederationMember = 0
    AddFederationMember = 1
    WhitelistHash = 2
    RemoveHash = 3
