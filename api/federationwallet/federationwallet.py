from typing import List, Union
from api import APIRequest, EndpointRegister, endpoint
from api.federationwallet.requestmodels import *
from api.federationwallet.responsemodels import *
from pybitcoin import RemovedTransactionModel, WalletBalanceModel, WalletGeneralInfoModel


class FederationWallet(APIRequest, metaclass=EndpointRegister):
    route = '/api/federationwallet'

    def __init__(self, **kwargs):
        super(FederationWallet, self).__init__(**kwargs)

    @endpoint(f'{route}/general-info')
    def general_info(self, **kwargs) -> WalletGeneralInfoModel:
        """Retrieves general information about the wallet.

        Args:
            **kwargs:

        Returns:
            WalletGeneralInfoModel

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return WalletGeneralInfoModel(**data)

    @endpoint(f'{route}/balance')
    def balance(self, **kwargs) -> WalletBalanceModel:
        """Retrieves wallet balances.

        Args:
            **kwargs:

        Returns:
            WalletBalanceModel

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return WalletBalanceModel(**data)

    @endpoint(f'{route}/history')
    def history(self, request_model: HistoryRequest, **kwargs) -> List[WithdrawalModel]:
        """Retrieves a withdrawal history for the wallet.

        Args:
            request_model: A history request model.
            **kwargs:

        Returns:
            List[WithdrawalModel]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return [WithdrawalModel(**x) for x in data]

    @endpoint(f'{route}/sync')
    def sync(self, request_model: SyncRequest, **kwargs) -> None:
        """Starts sending block to wallet for synchronisation. Demo/testing use only.

        Args:
            request_model: A syncrequest model.
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/enable-federation')
    def enable_federation(self, request_model: EnableFederationRequest, **kwargs) -> Union[None, str]:
        """Provide the federation wallet's credentials so that it can sign transactions.

        Args:
            request_model: EnableFederationRequest model.
            **kwargs:

        Returns:
            APIError
        """
        data = self.post(request_model, **kwargs)

        if data is not None:
            return data

    @endpoint(f'{route}/remove-transactions')
    def general_info(self, request_model: RemoveTransactionsRequest, **kwargs) -> List[RemovedTransactionModel]:
        """Remove all transactions from the wallet.

        Args:
            request_model: RemoveTransactionsRequest model.
            **kwargs:

        Returns:
            List[RemovedTransactionModel]

        Raises:
            APIError
        """
        data = self.delete(request_model, **kwargs)

        return [RemovedTransactionModel(**x) for x in data]
