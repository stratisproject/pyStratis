from typing import Optional
from pystratis.api import Model


class GetCodeModel(Model):
    """A pydantic model for the smart contact code request."""
    type: str
    """The code type."""
    bytecode: str
    """The contract bytecode."""
    csharp: str
    """The csharp code."""
    message: Optional[str]
    """A message from response."""
