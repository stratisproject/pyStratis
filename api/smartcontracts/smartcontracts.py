import ast
from typing import List
from api import APIRequest, EndpointRegister, endpoint
from api.smartcontracts.requestmodels import *
from api.smartcontracts.responsemodels import *
from pybitcoin import BuildContractTransactionModel
from pybitcoin.types import Address, Money, hexstr


class SmartContracts(APIRequest, metaclass=EndpointRegister):
    route = '/api/smartcontracts'

    def __init__(self, **kwargs):
        super(SmartContracts, self).__init__(**kwargs)

    @endpoint(f'{route}/code')
    def code(self, request_model: CodeRequest, **kwargs) -> GetCodeModel:
        """Gets the bytecode for a smart contract as a hexadecimal string.

        Args:
            request_model: CodeRequest model
            **kwargs:

        Returns:
            GetCodeModel

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return GetCodeModel(**data)

    @endpoint(f'{route}/balance')
    def balance(self, request_model: BalanceRequest, **kwargs) -> Money:
        """Gets the balance of a smart contract in strax or sidechain coin.

        Args:
            request_model: BalanceRequest model
            **kwargs:

        Returns:
            Money

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return Money(data)

    @endpoint(f'{route}/storage')
    def storage(self, request_model: StorageRequest, **kwargs) -> hexstr:
        """Gets a single piece of smart contract data. Returns a serialized string, if exists.

        Args:
            request_model:
            **kwargs:

        Returns:
            hexstr

        Raises:
            APIError
            RuntimeError
        """
        data = self.get(request_model, **kwargs)

        if hasattr(data, 'Message'):
            raise RuntimeError(data['Message'])
        return data

    @endpoint(f'{route}/receipt')
    def receipt(self, request_model: ReceiptRequest, **kwargs) -> ReceiptModel:
        """Gets a smart contract transaction receipt

        Args:
            request_model: ReceiptRequest model
            **kwargs:

        Returns:
            ReceiptModel

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)
        data['To'] = Address(address=data['To'], network=self._network)
        data['From'] = Address(address=data['From'], network=self._network)
        data['NewContractAddress'] = Address(address=data['NewContractAddress'], network=self._network)
        for i in range(len(data['Logs'])):
            data['Logs'][i]['Address'] = Address(address=data['Logs'][i]['Address'], network=self._network)

        return ReceiptModel(**data)

    @endpoint(f'{route}/receipt-search')
    def receipt_search(self, request_model: ReceiptSearchRequest, **kwargs) -> List[ReceiptModel]:
        """Searches a smart contract's receipts for those which match a specific event.

        Args:
            request_model: ReceiptSearchRequest model
            **kwargs:

        Returns:
            List[ReceiptModel]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)
        for i in range(len(data)):
            data[i]['To'] = Address(address=data[i]['To'], network=self._network)
            data[i]['From'] = Address(address=data[i]['From'], network=self._network)
            data[i]['NewContractAddress'] = Address(address=data[i]['NewContractAddress'], network=self._network)
            for j in range(len(data[i]['Logs'])):
                data[i]['Logs'][j]['Address'] = Address(address=data[i]['Logs'][j]['Address'], network=self._network)

        return [ReceiptModel(**x) for x in data]

    @endpoint(f'{route}/build-create')
    def build_create(self, request_model: BuildCreateContractTransactionRequest, **kwargs) -> BuildContractTransactionModel:
        """Builds a transaction to create a smart contract.

        Args:
            request_model: BuildCreateContractTransactionRequest model
            **kwargs:

        Returns:
            BuildContractTransactionModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return BuildContractTransactionModel(**data)

    @endpoint(f'{route}/build-call')
    def build_call(self, request_model: BuildCallContractTransactionRequest, **kwargs) -> BuildContractTransactionModel:
        """Builds a transaction to call a smart contract method.

        Args:
            request_model: BuildCallContractTransactionRequest model
            **kwargs:

        Returns:
            BuildContractTransactionModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return BuildContractTransactionModel(**data)

    @endpoint(f'{route}/build-transaction')
    def build_transaction(self, request_model: BuildTransactionRequest, **kwargs) -> BuildContractTransactionModel:
        """Buld a transaction to transfer funds on a smart contract network.

        Args:
            request_model: BuildTransactionRequest model
            **kwargs:

        Returns:
            BuildContractTransactionModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return BuildContractTransactionModel(**data)

    @endpoint(f'{route}/estimate-fee')
    def estimate_fee(self, request_model: EstimateFeeRequest, **kwargs) -> Money:
        """Gets a fee estimate for a specific smart contract account-based transfer transaction.

        Args:
            request_model: EstimateFeeRequest model
            **kwargs:

        Returns:
            Money

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return Money(data)

    @endpoint(f'{route}/build-and-send-create')
    def build_and_send_create(self, request_model: BuildAndSendCreateContractTransactionRequest, **kwargs) -> BuildContractTransactionModel:
        """Builds a transaction to create a smart contract and then broadcasts.

        Args:
            request_model: BuildAndSendCreateContractTransactionRequest model
            **kwargs:

        Returns:
            BuildContractTransactionModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return BuildContractTransactionModel(**data)

    @endpoint(f'{route}/build-and-send-call')
    def build_and_send_call(self, request_model: BuildAndSendCallContractTransactionRequest, **kwargs) -> BuildContractTransactionModel:
        """Biuilds a transaction to call a smart contract method and then broadcasts.

        Args:
            request_model: BuildAndSendCallContractTransactionRequest model
            **kwargs:

        Returns:
            BuildContractTransactionModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return BuildContractTransactionModel(**data)

    @endpoint(f'{route}/local-call')
    def local_call(self, request_model: LocalCallContractTransactionRequest, **kwargs) -> LocalExecutionResultModel:
        """Makes a local call to a method on a smart contract that has been successfully deployed. The purpose is to query and test methods.

        Args:
            request_model: LocalCallContractTransactionRequest model
            **kwargs:

        Returns:
            LocalExecutionResultModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)
        for i in range(len(data['InternalTransfers'])):
            data['InternalTransfers'][i]['From'] = Address(address=data['InternalTransfers'][i]['From'], network=self._network)
            data['InternalTransfers'][i]['To'] = Address(address=data['InternalTransfers'][i]['To'], network=self._network)
        for i in range(len(data['Logs'])):
            data['Logs'][i]['Address'] = Address(address=data['Logs'][i]['Address'], network=self._network)
        data['Return'] = ast.literal_eval(data['Return'])

        return LocalExecutionResultModel(**data)

    @endpoint(f'{route}/address-balances')
    def address_balances(self, request_model: BalancesRequest, **kwargs) -> List[AddressBalanceModel]:
        """Gets all addresses owned by a wallet which have a balance associated with them.

        Args:
            request_model: BalancesRequest model
            **kwargs:

        Returns:
            List[AddressBalanceModel]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)
        for i in range(len(data)):
            data[i]['Address'] = Address(address=data[i]['Address'], network=self._network)

        return [AddressBalanceModel(**x) for x in data]
