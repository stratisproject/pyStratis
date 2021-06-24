from typing import List
from api import APIRequest, EndpointRegister, endpoint
from api.multisig.requestmodels import *
from api.multisig.responsemodels import *
from pybitcoin import Recipient, MultisigSecret
from pybitcoin.types import Money


class Multisig(APIRequest, metaclass=EndpointRegister):
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
            **kwargs:

        Returns:
            BuildTransactionModel

        Raises:
            APIError
        """
        request_model = BuildTransactionRequest(recipients=recipients, secrets=secrets)
        data = self.post(request_model, **kwargs)
        data['fee'] = Money.from_satoshi_units(data['fee'])

        return BuildTransactionModel(**data)
