from pydantic import Field, SecretStr
from .setupofflinerequest import SetupOfflineRequest


# noinspection PyUnresolvedReferences
class SetupRequest(SetupOfflineRequest):
    """A request model for the coldstaking/setup-cold-staking and coldstaking/estimate-cold-staking-setup-tx-fee endpoints.

    Args:
        cold_wallet_address (Address): The cold wallet address.
        hot_wallet_address (Address): The hot wallet address.
        wallet_name (str): The wallet name.
        wallet_account (str): The wallet account.
        amount (Money): The amount to send to the old wallet.
        fees (Money): The transaction fee.
        subtract_fee_from_amount (bool, optional): If fee should be subtracted from amount. Default=True.
        split_count (conint(ge=1), optional): Number of transactions to split over. Default=1.
        segwit_change_address (bool, optional): If change address is a segwit address. Default=False.
        wallet_password (SecretStr): The wallet password.
    """
    wallet_password: SecretStr = Field(alias='walletPassword')
