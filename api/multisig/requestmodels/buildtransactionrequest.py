from typing import List
from pybitcoin import Model, MultisigSecret, Recipient


class BuildTransactionRequest(Model):
    """A BuildTransactionRequest."""
    recipients: List[Recipient]
    secrets: List[MultisigSecret]
