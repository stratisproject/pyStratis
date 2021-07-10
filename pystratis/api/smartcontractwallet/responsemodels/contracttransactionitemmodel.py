from pydantic import Field
from pystratis.api import Model
from pystratis.core import ContractTransactionItemType
from pystratis.core.types import Address, Money, uint256


class ContractTransactionItemModel(Model):
    """A pydantic model representing a contract transaction."""
    block_height: int = Field(alias='blockHeight')
    """The block height of block containing the transaction."""
    item_type: ContractTransactionItemType = Field(alias='type')
    """The contract transaction item type."""
    hash: uint256
    """The transaction hash."""
    to_address: Address = Field(alias='to')
    """The to address of the contact."""
    amount: Money
    """The transaction amount."""
    transaction_fee: Money = Field(alias='transactionFee')
    """The transaction fee."""
    gas_fee: Money = Field(alias='gasFee')
    """The transaction's gas fee."""
