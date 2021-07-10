from typing import Optional
from pydantic import StrictBytes, Field
from .basenetwork import BaseNetwork


# noinspection PyUnresolvedReferences
class StraxMain(BaseNetwork):
    """Describes the StraxMain network.

    Args:
        DEFAULT_PORT (int, optional): The network communication port. Default=17105.
        RPC_PORT (int, optional): The rpc port, if active. Default=17104.
        API_PORT (int, optional): The API port. Default=17103.
        SIGNALR_PORT (int, optional): The SignalR port. Default=17102.
    """
    name: str = Field(default='StraxMain')
    PUBKEY_ADDRESS: StrictBytes = Field(default=bytes([75]))
    SCRIPT_ADDRESS: StrictBytes = Field(default=bytes([140]))
    SECRET_KEY: StrictBytes = Field(default=bytes([75+128]))
    ENCRYPTED_SECRET_KEY_NO_EC: StrictBytes = Field(default=bytes([0x01, 0x42]))
    ENCRYPTED_SECRET_KEY_EC: StrictBytes = Field(default=bytes([0x01, 0x43]))
    EXT_PUBLIC_KEY: StrictBytes = Field(default=bytes([0x04, 0x88, 0xB2, 0x1E]))
    EXT_SECRET_KEY: StrictBytes = Field(default=bytes([0x04, 0x88, 0xAD, 0xE4]))
    PASSPHRASE_CODE: StrictBytes = Field(default=bytes([0x2C, 0xE9, 0xB3, 0xE1, 0xFF, 0x39, 0xE2]))
    CONFIRMATION_CODE: StrictBytes = Field(default=bytes([0x64, 0x3B, 0xF6, 0xA8, 0x9A]))
    STEALTH_ADDRESS: StrictBytes = Field(default=bytes([0x2A]))
    ASSET_ID: StrictBytes = Field(default=bytes([23]))
    COLORED_ADDRESS: StrictBytes = Field(default=bytes([0x13]))
    BECH32_HRP = 'strax'
    DEFAULT_PORT: Optional[int] = Field(default=17105)
    RPC_PORT: Optional[int] = Field(default=17104)
    API_PORT: Optional[int] = Field(default=17103)
    SIGNALR_PORT: Optional[int] = Field(default=17102)


# noinspection PyUnresolvedReferences
class StraxTest(BaseNetwork):
    """Describes the StraxTest network.

    Args:
        DEFAULT_PORT (int, optional): The network communication port. Default=27105.
        RPC_PORT (int, optional): The rpc port, if active. Default=27104.
        API_PORT (int, optional): The API port. Default=27103.
        SIGNALR_PORT (int, optional): The SignalR port. Default=27102.
    """
    name: str = Field(default='StraxTest')
    PUBKEY_ADDRESS: StrictBytes = Field(default=bytes([120]))
    SCRIPT_ADDRESS: StrictBytes = Field(default=bytes([127]))
    SECRET_KEY: StrictBytes = Field(default=bytes([120 + 128]))
    ENCRYPTED_SECRET_KEY_NO_EC: StrictBytes = Field(default=bytes([0x01, 0x42]))
    ENCRYPTED_SECRET_KEY_EC: StrictBytes = Field(default=bytes([0x01, 0x43]))
    EXT_PUBLIC_KEY: StrictBytes = Field(default=bytes([0x04, 0x88, 0xB2, 0x1E]))
    EXT_SECRET_KEY: StrictBytes = Field(default=bytes([0x04, 0x88, 0xAD, 0xE4]))
    PASSPHRASE_CODE: StrictBytes = Field(default=bytes([0x2C, 0xE9, 0xB3, 0xE1, 0xFF, 0x39, 0xE2]))
    CONFIRMATION_CODE: StrictBytes = Field(default=bytes([0x64, 0x3B, 0xF6, 0xA8, 0x9A]))
    STEALTH_ADDRESS: StrictBytes = Field(default=bytes([0x2A]))
    ASSET_ID: StrictBytes = Field(default=bytes([23]))
    COLORED_ADDRESS: StrictBytes = Field(default=bytes([0x13]))
    BECH32_HRP = 'tstrax'
    DEFAULT_PORT: Optional[int] = Field(default=27105)
    RPC_PORT: Optional[int] = Field(default=27104)
    API_PORT: Optional[int] = Field(default=27103)
    SIGNALR_PORT: Optional[int] = Field(default=27102)


# noinspection PyUnresolvedReferences
class StraxRegTest(BaseNetwork):
    """Describes the StraxRegTest network.

    Args:
        DEFAULT_PORT (int, optional): The network communication port. Default=37105.
        RPC_PORT (int, optional): The rpc port, if active. Default=37104.
        API_PORT (int, optional): The API port. Default=37103.
        SIGNALR_PORT (int, optional): The SignalR port. Default=37102.
    """
    name: str = Field(default='StraxRegTest')
    PUBKEY_ADDRESS: StrictBytes = Field(default=bytes([120]))
    SCRIPT_ADDRESS: StrictBytes = Field(default=bytes([127]))
    SECRET_KEY: StrictBytes = Field(default=bytes([120 + 128]))
    ENCRYPTED_SECRET_KEY_NO_EC: StrictBytes = Field(default=bytes([0x01, 0x42]))
    ENCRYPTED_SECRET_KEY_EC: StrictBytes = Field(default=bytes([0x01, 0x43]))
    EXT_PUBLIC_KEY: StrictBytes = Field(default=bytes([0x04, 0x88, 0xB2, 0x1E]))
    EXT_SECRET_KEY: StrictBytes = Field(default=bytes([0x04, 0x88, 0xAD, 0xE4]))
    PASSPHRASE_CODE: StrictBytes = Field(default=bytes([0x2C, 0xE9, 0xB3, 0xE1, 0xFF, 0x39, 0xE2]))
    CONFIRMATION_CODE: StrictBytes = Field(default=bytes([0x64, 0x3B, 0xF6, 0xA8, 0x9A]))
    STEALTH_ADDRESS: StrictBytes = Field(default=bytes([0x2A]))
    ASSET_ID: StrictBytes = Field(default=bytes([23]))
    COLORED_ADDRESS: StrictBytes = Field(default=bytes([0x13]))
    BECH32_HRP = 'tstrax'
    DEFAULT_PORT: Optional[int] = Field(default=37105)
    RPC_PORT: Optional[int] = Field(default=37104)
    API_PORT: Optional[int] = Field(default=37103)
    SIGNALR_PORT: Optional[int] = Field(default=37102)
