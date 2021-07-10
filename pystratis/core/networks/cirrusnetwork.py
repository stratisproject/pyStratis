from typing import Optional
from pydantic import StrictBytes, Field
from .basenetwork import BaseNetwork


# noinspection PyUnresolvedReferences
class CirrusMain(BaseNetwork):
    """Describes the CirrusMain network.

    Args:
        DEFAULT_PORT (int, optional): The network communication port. Default=16179.
        RPC_PORT (int, optional): The rpc port, if active. Default=16175.
        API_PORT (int, optional): The API port. Default=37223.
        SIGNALR_PORT (int, optional): The SignalR port. Default=38823.
    """
    name: str = Field(default='CirrusMain')
    PUBKEY_ADDRESS: StrictBytes = Field(default=bytes([28]))
    SCRIPT_ADDRESS: StrictBytes = Field(default=bytes([88]))
    SECRET_KEY: StrictBytes = Field(default=bytes([239]))
    ENCRYPTED_SECRET_KEY_NO_EC: StrictBytes = Field(default=bytes([0x01, 0x42]))
    ENCRYPTED_SECRET_KEY_EC: StrictBytes = Field(default=bytes([0x01, 0x43]))
    EXT_PUBLIC_KEY: StrictBytes = Field(default=bytes([0x04, 0x35, 0x87, 0xCF]))
    EXT_SECRET_KEY: StrictBytes = Field(default=bytes([0x04, 0x35, 0x83, 0x94]))
    PASSPHRASE_CODE: StrictBytes = Field(default=bytes([0x2C, 0xE9, 0xB3, 0xE1, 0xFF, 0x39, 0xE2]))
    CONFIRMATION_CODE: StrictBytes = Field(default=bytes([0x64, 0x3B, 0xF6, 0xA8, 0x9A]))
    STEALTH_ADDRESS: StrictBytes = Field(default=bytes([0x2B]))
    ASSET_ID: StrictBytes = Field(default=bytes([115]))
    COLORED_ADDRESS: StrictBytes = Field(default=bytes([0x13]))
    BECH32_HRP = 'tb'
    DEFAULT_PORT: Optional[int] = Field(default=16179)
    RPC_PORT: Optional[int] = Field(default=16175)
    API_PORT: Optional[int] = Field(default=37223)
    SIGNALR_PORT: Optional[int] = Field(default=38823)


# noinspection PyUnresolvedReferences
class CirrusTest(BaseNetwork):
    """Describes the CirrusTest network.

    Args:
        DEFAULT_PORT (int, optional): The network communication port. Default=26179.
        RPC_PORT (int, optional): The rpc port, if active. Default=26175.
        API_PORT (int, optional): The API port. Default=38223.
        SIGNALR_PORT (int, optional): The SignalR port. Default=39823.
    """
    name: str = Field(default='CirrusTest')
    PUBKEY_ADDRESS: StrictBytes = Field(default=bytes([127]))
    SCRIPT_ADDRESS: StrictBytes = Field(default=bytes([137]))
    SECRET_KEY: StrictBytes = Field(default=bytes([239]))
    ENCRYPTED_SECRET_KEY_NO_EC: StrictBytes = Field(default=bytes([0x01, 0x42]))
    ENCRYPTED_SECRET_KEY_EC: StrictBytes = Field(default=bytes([0x01, 0x43]))
    EXT_PUBLIC_KEY: StrictBytes = Field(default=bytes([0x04, 0x35, 0x87, 0xCF]))
    EXT_SECRET_KEY: StrictBytes = Field(default=bytes([0x04, 0x35, 0x83, 0x94]))
    PASSPHRASE_CODE: StrictBytes = Field(default=bytes([0x2C, 0xE9, 0xB3, 0xE1, 0xFF, 0x39, 0xE2]))
    CONFIRMATION_CODE: StrictBytes = Field(default=bytes([0x64, 0x3B, 0xF6, 0xA8, 0x9A]))
    STEALTH_ADDRESS: StrictBytes = Field(default=bytes([0x2B]))
    ASSET_ID: StrictBytes = Field(default=bytes([115]))
    COLORED_ADDRESS: StrictBytes = Field(default=bytes([0x13]))
    BECH32_HRP = 'tb'
    DEFAULT_PORT: Optional[int] = Field(default=26179)
    RPC_PORT: Optional[int] = Field(default=26175)
    API_PORT: Optional[int] = Field(default=38223)
    SIGNALR_PORT: Optional[int] = Field(default=39823)


# noinspection PyUnresolvedReferences
class CirrusRegTest(BaseNetwork):
    """Describes the CirrusRegTest network.

    Args:
        DEFAULT_PORT (int, optional): The network communication port. Default=26179.
        RPC_PORT (int, optional): The rpc port, if active. Default=26175.
        API_PORT (int, optional): The API port. Default=38223.
        SIGNALR_PORT (int, optional): The SignalR port. Default=39823.
    """
    name: str = Field(default='CirrusRegTest')
    PUBKEY_ADDRESS: StrictBytes = Field(default=bytes([55]))
    SCRIPT_ADDRESS: StrictBytes = Field(default=bytes([117]))
    SECRET_KEY: StrictBytes = Field(default=bytes([239]))
    ENCRYPTED_SECRET_KEY_NO_EC: StrictBytes = Field(default=bytes([0x01, 0x42]))
    ENCRYPTED_SECRET_KEY_EC: StrictBytes = Field(default=bytes([0x01, 0x43]))
    EXT_PUBLIC_KEY: StrictBytes = Field(default=bytes([0x04, 0x35, 0x87, 0xCF]))
    EXT_SECRET_KEY: StrictBytes = Field(default=bytes([0x04, 0x35, 0x83, 0x94]))
    PASSPHRASE_CODE: StrictBytes = Field(default=bytes([0x2C, 0xE9, 0xB3, 0xE1, 0xFF, 0x39, 0xE2]))
    CONFIRMATION_CODE: StrictBytes = Field(default=bytes([0x64, 0x3B, 0xF6, 0xA8, 0x9A]))
    STEALTH_ADDRESS: StrictBytes = Field(default=bytes([0x2B]))
    ASSET_ID: StrictBytes = Field(default=bytes([115]))
    COLORED_ADDRESS: StrictBytes = Field(default=bytes([0x13]))
    BECH32_HRP = 'tb'
    DEFAULT_PORT: Optional[int] = Field(default=26179)
    RPC_PORT: Optional[int] = Field(default=26175)
    API_PORT: Optional[int] = Field(default=38223)
    SIGNALR_PORT: Optional[int] = Field(default=39823)
