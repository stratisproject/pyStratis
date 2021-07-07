from typing import List
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.multisig.requestmodels import *
from pystratis.api.multisig.responsemodels import *
from pystratis.core import Recipient, MultisigSecret
from pystratis.core.types import Money


class Multisig(APIRequest, metaclass=EndpointRegister):
    """Implements the multisig api endpoints."""

    route = '/api/multisig'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/build-transaction')
    def build_transaction(self,
                          recipients: List[Recipient],
                          secrets: List[MultisigSecret],
                          **kwargs) -> BuildTransactionModel:
        """Builds a transaction.

        Args:
            recipients (List[Recipient]): A list of recipient objects.
            secrets (List[MultisigSecret]): A list of corresponding multisig secrets.
            **kwargs: Extra keyword arguments. 

        Returns:
            BuildTransactionModel: A built multisig transaction.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = BuildTransactionRequest(recipients=recipients, secrets=secrets)
        data = self.post(request_model, **kwargs)
        data['fee'] = Money.from_satoshi_units(data['fee'])

        return BuildTransactionModel(**data)
