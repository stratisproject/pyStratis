from typing import List
from pybitcoin import Model, MultisigSecret, Recipient


class BuildTransactionRequest(Model):
    """A request model for the multisig/build-transaction endpoint.

    Args:
        recipients (List[Recipient]): A list of recipient objects.
        secrets (List[MultisigSecret]): A list of corresponding multisig secrets.
    """
    recipients: List[Recipient]
    secrets: List[MultisigSecret]
