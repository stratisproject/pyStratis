from pydantic import BaseModel


class ScriptSig(BaseModel):
    """A ScriptSig."""
    asm: str
    hex: str
