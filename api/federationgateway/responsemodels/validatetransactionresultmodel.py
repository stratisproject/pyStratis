from typing import List
from pydantic import Field
from pybitcoin import Model


class ValidateTransactionResultModel(Model):
    """A ValidateTransactionResultModel."""
    is_valid: bool = Field(alias='IsValid')
    errors: List[str] = Field(alias='Errors')
