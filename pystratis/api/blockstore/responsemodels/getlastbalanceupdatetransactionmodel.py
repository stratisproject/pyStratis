from pydantic import Field
from pystratis.api import Model
from pystratis.api.global_responsemodels import TransactionModel


class GetLastBalanceUpdateTransactionModel(Model):
    """A pydantic model containing information about there last transaction where a balance changed for an address."""
    transaction: TransactionModel
    """The transaction model containing the last balance update of the given address."""
    block_height: int = Field(alias='blockHeight')
    """The block height for the last transaction for the given address."""
