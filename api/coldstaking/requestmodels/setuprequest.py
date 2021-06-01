from pydantic import Field, SecretStr
from .setupofflinerequest import SetupOfflineRequest


class SetupRequest(SetupOfflineRequest):
    """A SetupRequest."""
    wallet_password: SecretStr = Field(alias='walletPassword')
