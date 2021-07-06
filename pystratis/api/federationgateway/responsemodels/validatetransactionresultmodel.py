from typing import List, Optional
from pydantic import Field
from pystratis.api import Model


class ValidateTransactionResultModel(Model):
    """A pydantic model for a validate transaction result."""
    is_valid: bool = Field(alias='isValid')
    """If true, transaction is valid."""
    errors: Optional[List[str]] = Field(alias='errors')
    """Transaction validation errors."""
