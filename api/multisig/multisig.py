from api import APIRequest, EndpointRegister, endpoint
from api.multisig.requestmodels import *
from api.multisig.responsemodels import *
from pybitcoin.types import Money


class Multisig(APIRequest, metaclass=EndpointRegister):
    route = '/api/multisig'

    def __init__(self, **kwargs):
        super(Multisig, self).__init__(**kwargs)

    @endpoint(f'{route}/build-transaction')
    def build_transaction(self, request_model: BuildTransactionRequest, **kwargs) -> BuildTransactionModel:
        """Builds a transaction.

        Args:
            request_model: BuildTransactionRequest model.
            **kwargs:

        Returns:
            BuildTransactionModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)
        data['fee'] = Money.from_satoshi_units(data['fee'])

        return BuildTransactionModel(**data)
