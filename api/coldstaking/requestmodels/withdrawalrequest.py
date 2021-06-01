from pydantic import SecretStr, Field
from .offlinewithdrawalrequest import OfflineWithdrawalRequest


class WithdrawalRequest(OfflineWithdrawalRequest):
    """A WithdrawalRequest."""
    wallet_password: SecretStr = Field(alias='walletPassword')

