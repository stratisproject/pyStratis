from typing import List
from api import APIRequest, EndpointRegister, endpoint
from api.smartcontractwallet.requestmodels import *
from api.smartcontractwallet.responsemodels import *
from pybitcoin.types import Address, Money, uint256


class SmartContractWallet(APIRequest, metaclass=EndpointRegister):
    route = '/api/smartcontractwallet'

    def __init__(self, **kwargs):
        super(SmartContractWallet, self).__init__(**kwargs)

    @endpoint(f'{route}/account-addresses')
    def account_addresses(self, request_model: AccountAddressesRequest, **kwargs) -> List[Address]:
        """Gets a smart contract account address.

        Args:
            request_model: AccountAddressesRequest model
            **kwargs:

        Returns:
            List[Address]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return [Address(address=x, network=self._network) for x in data]

    @endpoint(f'{route}/address-balance')
    def address_balance(self, request_model: AddressBalanceRequest, **kwargs) -> Money:
        """Gets the balance at a specific wallet address in STRAX (or the sidechain coin).

        Args:
            request_model: AddressBalanceRequest model
            **kwargs:

        Returns:
            Money

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return Money.from_satoshi_units(data)

    @endpoint(f'{route}/history')
    def history(self, request_model: HistoryRequest, **kwargs) -> List[ContractTransactionItemModel]:
        """Gets the history of a specific wallet address.

        Args:
            request_model: HistoryRequest model
            **kwargs:

        Returns:
            List[ContractTransactionItemModel]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)
        for i in range(len(data)):
            data[i]['to'] = Address(address=data[i]['to'], network=self._network)

        return [ContractTransactionItemModel(**x) for x in data]

    @endpoint(f'{route}/create')
    def create(self, request_model: CreateContractTransactionRequest, **kwargs) -> uint256:
        """Builds a transaction to create a smart contract and then broadcasts the transaction to the network.

        Args:
            request_model: CreateContractTransactionRequest model
            **kwargs:

        Returns:
            uint256

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return uint256(data)

    @endpoint(f'{route}/call')
    def call(self, request_model: CallContractTransactionRequest, **kwargs) -> BuildContractTransactionModel:
        """Builds a transaction to call a smart contract method and then broadcasts the transaction to the network.

        Args:
            request_model: CallContractTransactionRequest model
            **kwargs:

        Returns:
            BuildContractTransactionModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return BuildContractTransactionModel(**data)

    @endpoint(f'{route}/send-transaction')
    def send_transaction(self, request_model: SendTransactionRequest, **kwargs) -> WalletSendTransactionModel:
        """Broadcasts a transaction, which either creates a smart contract or calls a method on a smart contract.

        Args:
            request_model: SendTransactionRequest model
            **kwargs:

        Returns:
            WalletSendTransactionModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)
        for i in range(len(data['outputs'])):
            if 'address' in data['outputs'][i]:
                try:
                    data['outputs'][i]['address'] = int(data['outputs'][i]['address'])
                except ValueError:
                    data['outputs'][i]['address'] = Address(address=data['outputs'][i]['address'], network=self._network)
            data['outputs'][i] = TransactionOutputModel(**data['outputs'][i])

        return WalletSendTransactionModel(**data)
