from typing import Optional
from pybitcoin import Model


class GetCodeModel(Model):
    """A GetCodeModel."""
    type: Optional[str]
    bytecode: Optional[str]
    csharp: Optional[str]
    message: Optional[str]
