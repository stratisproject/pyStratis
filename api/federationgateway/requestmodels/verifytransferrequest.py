from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import uint256


class VerifyTransferRequest(Model):
    """A request model for the federationgateway/transfer/verify endpoint.

    Args:
        deposit_id_transaction_id (uint256): The transaction id containing the deposit with the deposit id.
    """
    deposit_id_transaction_id: uint256 = Field(alias='depositIdTransactionId')
