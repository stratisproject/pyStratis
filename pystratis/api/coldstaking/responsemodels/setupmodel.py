from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import hexstr


class SetupModel(Model):
    """A pydantic model for a cold staking wallet setup transaction."""
    transaction_hex: hexstr = Field(alias='transactionHex')
    """The hex serialized cold staking wallet setup transaction."""
