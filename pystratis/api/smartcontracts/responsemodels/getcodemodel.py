from typing import Optional
from pystratis.core import Model


class GetCodeModel(Model):
    """A GetCodeModel."""
    type: Optional[str]
    bytecode: Optional[str]
    csharp: Optional[str]
    message: Optional[str]
