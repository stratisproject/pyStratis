from typing import Union, List
from decimal import Decimal
from api import APIRequest, EndpointRegister, endpoint
from api.smartcontractwallet.requestmodels import *
from api.smartcontractwallet.responsemodels import *
from pybitcoin.types import Address, Money, uint256, hexstr
from pybitcoin import Outpoint, SmartContractParameter


class SmartContractWallet(APIRequest, metaclass=EndpointRegister):
    route = '/api/smartcontractwallet'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/account-addresses')
    def account_addresses(self,
                          wallet_name: str,
                          **kwargs) -> List[Address]:
        """Gets a smart contract account address.

        Args:
            wallet_name (str): The wallet name.
            **kwargs:

        Returns:
            List[Address]

        Raises:
            APIError
        """
        request_model = AccountAddressesRequest(wallet_name=wallet_name)
        data = self.get(request_model, **kwargs)
        return [Address(address=x, network=self._network) for x in data]

    @endpoint(f'{route}/address-balance')
    def address_balance(self,
                        address: Union[Address, str],
                        **kwargs) -> Money:
        """Gets the balance at a specific wallet address in STRAX (or the sidechain coin).

        Args:
            address (Address | str): The smart contract address being queried.
            **kwargs:

        Returns:
            Money

        Raises:
            APIError
        """
        if isinstance(address, str):
            address = Address(address=address, network=self._network)
        request_model = AddressBalanceRequest(address=address)
        data = self.get(request_model, **kwargs)
        return Money.from_satoshi_units(data)

    @endpoint(f'{route}/history')
    def history(self,
                wallet_name: str,
                address: Union[Address, str],
                skip: int = 0,
                take: int = None,
                **kwargs) -> List[ContractTransactionItemModel]:
        """Gets the history of a specific wallet address.

        Args:
            wallet_name (str): The wallet name.
            address (Address | str): The address to query the history.
            skip (int, optional): Skip this many items. Default=0.
            take (int, optional): Take this many items.
            **kwargs:

        Returns:
            List[ContractTransactionItemModel]

        Raises:
            APIError
        """
        if isinstance(address, str):
            address = Address(address=address, network=self._network)
        request_model = HistoryRequest(
            wallet_name=wallet_name,
            address=address,
            skip=skip,
            take=take
        )
        data = self.get(request_model, **kwargs)
        for i in range(len(data)):
            data[i]['to'] = Address(address=data[i]['to'], network=self._network)
        return [ContractTransactionItemModel(**x) for x in data]

    @endpoint(f'{route}/create')
    def create(self,
               wallet_name: str,
               fee_amount: Union[Money, int, float, Decimal],
               password: str,
               contract_code: Union[hexstr, str],
               gas_price: int,
               gas_limit: int,
               sender: Union[Address, str],
               amount: Union[Money, int, float, Decimal] = None,
               outpoints: List[Outpoint] = None,
               account_name: str = 'account 0',
               parameters: List[str] = None,
               **kwargs) -> uint256:
        """Builds a transaction to create a smart contract and then broadcasts the transaction to the network.

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The wallet name. Default='account 0'
            outpoints (List[Outpoint], optional): A list of the outpoints used to construct the transactation.
            amount (Money | int | float | Decimal, optional): The amount being sent.
            fee_amount (Money | int | float | Decimal): The fee amount.
            password (SecretStr): The password.
            contract_code (hexstr | str): The smart contract code hexstring.
            gas_price (int): The amount of gas being used in satoshis.
            gas_limit (int): The maximum amount of gas that can be used in satoshis.
            sender (Address | str): The address of the sending address.
            parameters (List[Union[SmartContractParameter, str], optional): A list of parameters for the smart contract.
            **kwargs:

        Returns:
            uint256

        Raises:
            APIError
        """
        if isinstance(sender, str):
            sender = Address(address=sender, network=self._network)
        new_parameters = []
        for item in parameters:
            if isinstance(item, SmartContractParameter):
                new_parameters.append(item)
            else:
                assert isinstance(item, str)
                value_type, value = item.split('#')
                new_parameters.append(SmartContractParameter(value_type=value_type, value=value))
        request_model = CreateContractTransactionRequest(
            wallet_name=wallet_name,
            account_name=account_name,
            outpoints=outpoints,
            amount=Money(amount) if amount is not None else None,
            fee_amount=Money(fee_amount),
            password=password,
            contract_code=hexstr(contract_code),
            gas_price=gas_price,
            gas_limit=gas_limit,
            sender=sender,
            parameters=new_parameters
        )
        data = self.post(request_model, **kwargs)
        return uint256(data)

    @endpoint(f'{route}/call')
    def call(self,
             wallet_name: str,
             fee_amount: Union[Money, int, float, Decimal],
             password: str,
             contract_address: Union[Address, str],
             method_name: str,
             gas_price: int,
             gas_limit: int,
             sender: Union[Address, str],
             amount: Union[Money, int, float, Decimal] = None,
             outpoints: List[Outpoint] = None,
             account_name: str = 'account 0',
             parameters: List[str] = None,
             **kwargs) -> BuildContractTransactionModel:
        """Builds a transaction to call a smart contract method and then broadcasts the transaction to the network.

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The wallet name. Default='account 0'
            outpoints (List[Outpoint], optional): A list of the outpoints used to construct the transactation.
            contract_address (Address | str): The smart contract address being called.
            method_name (str): The method name being called.
            amount (Money | int | float | Decimal, optional): The amount being sent.
            fee_amount (Money | int | float | Decimal): The fee amount.
            password (SecretStr): The password.
            gas_price (int): The amount of gas being used in satoshis.
            gas_limit (int): The maximum amount of gas that can be used in satoshis.
            sender (Address | str): The address of the sending address.
            parameters (List[Union[SmartContractParameter, str]], optional): A list of parameters for the smart contract.
            **kwargs:

        Returns:
            BuildContractTransactionModel

        Raises:
            APIError
        """
        if isinstance(contract_address, str):
            contract_address = Address(address=contract_address, network=self._network)
        if isinstance(sender, str):
            sender = Address(address=sender, network=self._network)
        new_parameters = []
        for item in parameters:
            if isinstance(item, SmartContractParameter):
                new_parameters.append(item)
            else:
                assert isinstance(item, str)
                value_type, value = item.split('#')
                new_parameters.append(SmartContractParameter(value_type=value_type, value=value))
        request_model = CallContractTransactionRequest(
            wallet_name=wallet_name,
            account_name=account_name,
            outpoints=outpoints,
            contract_address=contract_address,
            method_name=method_name,
            amount=Money(amount) if amount is not None else None,
            fee_amount=Money(fee_amount),
            password=password,
            gas_price=gas_price,
            gas_limit=gas_limit,
            sender=sender,
            parameters=new_parameters
        )
        data = self.post(request_model, **kwargs)
        return BuildContractTransactionModel(**data)

    @endpoint(f'{route}/send-transaction')
    def send_transaction(self,
                         transaction_hex: Union[hexstr, str],
                         **kwargs) -> WalletSendTransactionModel:
        """Broadcasts a transaction, which either creates a smart contract or calls a method on a smart contract.

        Args:
            transaction_hex (hexstr, str): The transaction hex string.
            **kwargs:

        Returns:
            WalletSendTransactionModel

        Raises:
            APIError
        """
        if isinstance(transaction_hex, str):
            transaction_hex = hexstr(transaction_hex)
        request_model = SendTransactionRequest(hex=transaction_hex)
        data = self.post(request_model, **kwargs)
        for i in range(len(data['outputs'])):
            if 'address' in data['outputs'][i]:
                try:
                    data['outputs'][i]['address'] = int(data['outputs'][i]['address'])
                except ValueError:
                    data['outputs'][i]['address'] = Address(address=data['outputs'][i]['address'], network=self._network)
            data['outputs'][i] = TransactionOutputModel(**data['outputs'][i])
        return WalletSendTransactionModel(**data)
