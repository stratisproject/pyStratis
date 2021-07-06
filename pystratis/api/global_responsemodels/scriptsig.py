from pystratis.api import Model


class ScriptSig(Model):
    """Represents ScriptSig.
    
    A ScriptSig is a part of transaction's input, and is the first half of a script.

    Note:
        Learn more about `transaction structure`__.

    .. __: https://en.bitcoin.it/wiki/Transaction#Input
    """
    asm: str
    """The assembly representation of the script."""
    hex: str
    """The hex representation of the script."""
