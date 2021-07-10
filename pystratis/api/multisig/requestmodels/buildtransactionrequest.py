from typing import List
from pystratis.api import Model
from pystratis.core import MultisigSecret, Recipient


# noinspection PyUnresolvedReferences
class BuildTransactionRequest(Model):
    """A request model for the multisig/build-transaction endpoint.

    Args:
        recipients (List[Recipient]): A list of recipient objects.
        secrets (List[MultisigSecret]): A list of corresponding multisig secrets.
    """
    recipients: List[Recipient]
    secrets: List[MultisigSecret]
