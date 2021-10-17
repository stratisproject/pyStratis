import ast
from typing import List, Union
from decimal import Decimal
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.core.types import Address, Money
from pystratis.api.dynamic_contract.responsemodels import *


class DynamicContract(APIRequest, metaclass=EndpointRegister):
    """Implements the connectionmanager api endpoints."""

    route = '/api/contract'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/{{address}}/property/{{property}}')
    def property(self,
                 address: Address,
                 property: str,
                 wallet_name: str,
                 wallet_password: str,
                 sender: Address,
                 gas_price: int = 100,
                 gas_limit: int = 250000,
                 amount: Union[Money, int, float, Decimal] = Money(0),
                 fee_amount: Union[Money, int, float, Decimal] = Money(0.01),
                 **kwargs) -> LocalExecutionResultModel:
        """Query the value of a property on the contract using a local call.

        Args:
            address (Address): The smart contract address.
            property (str): The property to query.
            wallet_name (str): The wallet name.
            wallet_password (str): The wallet password.
            sender (Address): The sending address.
            gas_price (int, optional): The gas price. Default=100
            gas_limit (int, optional): The gas limit. Default=250000
            amount (Money, int, float, Decimal, optional): Amount to send. Default=Money(0)
            fee_amount (Money, int, float, Decimal, optional): Fee amount. Default=Money(0.01)
            **kwargs: Extra keyword arguments.

        Returns:
            LocalExecutionResultModel: The results of a local contract execution.
        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        kwargs['endpoint'] = kwargs['endpoint'].replace('{address}', f'{address}')
        kwargs['endpoint'] = kwargs['endpoint'].replace('{property}', f'{property}')
        headers = {
            'GasPrice': str(gas_price),
            'GasLimit': str(gas_limit),
            'Amount': Money(amount).to_coin_unit(),
            'FeeAmount': Money(fee_amount).to_coin_unit(),
            'WalletName': wallet_name,
            'WalletPassword': wallet_password,
            'Sender': str(sender)
        }
        kwargs['headers'] = headers
        data = self.get(**kwargs)
        for i in range(len(data['internalTransfers'])):
            data['internalTransfers'][i]['from'] = Address(address=data['internalTransfers'][i]['from'], network=self._network)
            data['internalTransfers'][i]['to'] = Address(address=data['internalTransfers'][i]['to'], network=self._network)
        for i in range(len(data['logs'])):
            data['logs'][i]['address'] = Address(address=data['logs'][i]['address'], network=self._network)
        if data['errorMessage'] is not None:
            data['errorMessage'] = ast.literal_eval(data['errorMessage'])
            data['errorMessage'] = data['errorMessage']['value']
        if data['gasConsumed'] is not None:
            data['gasConsumed'] = data['gasConsumed']['value']
        if data['return'] is not None:
            data['return'] = data['return']
        return LocalExecutionResultModel(**data)

    @endpoint(f'{route}/{{address}}/method/{{method}}')
    def method(self,
               address: Address,
               method: str,
               data: dict,
               wallet_name: str,
               wallet_password: str,
               sender: Address,
               gas_price: int = 100,
               gas_limit: int = 250000,
               amount: Union[Money, int, float, Decimal] = Money(0),
               fee_amount: Union[Money, int, float, Decimal] = Money(0.01),
               **kwargs) -> BuildContractTransactionModel:
        """Call a method on the contract by broadcasting a call transaction to the network.

        Args:
            address (Address): The smart contract address.
            method (str): The method to call.
            data (dict): The data for the request body.
            wallet_name (str): The wallet name.
            wallet_password (str): The wallet password.
            sender (Address): The sending address.
            gas_price (int, optional): The gas price. Default=100
            gas_limit (int, optional): The gas limit. Default=250000
            amount (Money, int, float, Decimal, optional): Amount to send. Default=Money(0)
            fee_amount (Money, int, float, Decimal, optional): Fee amount. Default=Money(0.01)
            **kwargs: Extra keyword arguments.

        Returns:
            BuildContractTransactionModel: A built smart contract transaction.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        kwargs['endpoint'] = kwargs['endpoint'].replace('{address}', f'{address}')
        kwargs['endpoint'] = kwargs['endpoint'].replace('{method}', f'{method}')
        headers = {
            'GasPrice': str(gas_price),
            'GasLimit': str(gas_limit),
            'Amount': Money(amount).to_coin_unit(),
            'FeeAmount': Money(fee_amount).to_coin_unit(),
            'WalletName': wallet_name,
            'WalletPassword': wallet_password,
            'Sender': str(sender)
        }
        kwargs['headers'] = headers
        data = self.post(request_model=data, **kwargs)
        data['fee'] = Money.from_satoshi_units(data['fee'])
        return BuildContractTransactionModel(**data)
