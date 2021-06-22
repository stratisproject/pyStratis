from typing import List, Optional
from pydantic import Field
from pybitcoin import Model


class ValidateTransactionResultModel(Model):
    """A ValidateTransactionResultModel."""
    is_valid: Optional[bool] = Field(alias='isValid')
    errors: Optional[List[str]] = Field(alias='errors')
