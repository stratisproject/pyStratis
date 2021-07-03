from enum import IntEnum


class SmartContractParameterType(IntEnum):
    """Defines (de-)serialization rule for smart contract parameters.

    Notes:
        Learn more about contract's parameters serialization from `Stratis Academy`__.

    .. __: https://academy.stratisplatform.com/Architecture%20Reference/SmartContracts/working-with-contracts.html#parameter-serialization
    """
    Boolean = 1
    Byte = 2
    Char = 3
    String = 4
    UInt32 = 5
    Int32 = 6
    UInt64 = 7
    Int64 = 8
    Address = 9
    ByteArray = 10
    UInt128 = 11
    UInt256 = 12
