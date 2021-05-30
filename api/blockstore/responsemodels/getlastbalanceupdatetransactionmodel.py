from pydantic import Field, conint
from pybitcoin import Model, TransactionModel


class GetLastBalanceUpdateTransactionModel(Model):
    """A GetLastBalanceUpdateTransactionModel."""
    transaction: TransactionModel
    block_height: conint(ge=0) = Field(alias='blockHeight')
