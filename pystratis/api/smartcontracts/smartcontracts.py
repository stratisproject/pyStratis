import ast
from typing import List, Union
from binascii import unhexlify
from decimal import Decimal
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.smartcontracts.requestmodels import *
from pystratis.api.smartcontracts.responsemodels import *
from pystratis.core.types import Address, Money, uint32, uint64, uint128, uint256, int32, int64, hexstr
from pystratis.core import SmartContractParameter, Outpoint, Recipient


class SmartContracts(APIRequest, metaclass=EndpointRegister):
    """Implements the smartcontracts api endpoints."""

    route = '/api/smartcontracts'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/code')
    def code(self, address: Union[Address, str], **kwargs) -> GetCodeModel:
        """Gets the bytecode for a smart contract as a hexadecimal string.

        Args:
            address (Address, str): The smart contract address containing the contract bytecode.
            **kwargs: Extra keyword arguments. 

        Returns:
            GetCodeModel: The smart contract code.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(address, str):
            address = Address(address=address, network=self._network)
        request_model = CodeRequest(address=address)
        data = self.get(request_model, **kwargs)
        return GetCodeModel(**data)

    @endpoint(f'{route}/balance')
    def balance(self, address: Union[Address, str], **kwargs) -> Money:
        """Gets the balance of a smart contract in strax or sidechain coin.

        Args:
            address (Address, str): The smart contract address.
            **kwargs: Extra keyword arguments. 

        Returns:
            Money: The smart contract balance.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(address, str):
            address = Address(address=address, network=self._network)
        request_model = BalanceRequest(address=address)
        data = self.get(request_model, **kwargs)
        return Money(data)

    @endpoint(f'{route}/storage')
    def storage(self,
                contract_address: Union[Address, str],
                storage_key: str,
                data_type: int,
                **kwargs) -> Union[bool, bytes, str, uint32, uint64, int32, int64, Address, bytearray, uint128, uint256]:
        """Gets a single piece of smart contract data. Returns a serialized string, if exists.

        Args:
            contract_address (Address, str): The smart contract address being called.
            storage_key (str): The key in the key-value store.
            data_type: The data type. Allowed values: [1,12]
            **kwargs: Extra keyword arguments. 

        Returns:
            Union[bool, bytes, str, uint32, uint64, int32, int64, Address, bytearray, uint128, uint256]: The smart contract information retrieved from storage.

        Raises:
            APIError: Error thrown by node API. See message for details.
            RuntimeError
        """
        if isinstance(contract_address, str):
            contract_address = Address(address=contract_address, network=self._network)
        request_model = StorageRequest(contract_address=contract_address, storage_key=storage_key, data_type=data_type)
        data = self.get(request_model, **kwargs)
        if hasattr(data, 'Message'):
            raise RuntimeError(data['Message'])
        if request_model.data_type == 1:
            return bool(data)
        elif request_model.data_type == 2:
            return int(data).to_bytes(1, 'big')
        elif request_model.data_type == 3:
            return data
        elif request_model.data_type == 4:
            return data
        elif request_model.data_type == 5:
            return uint32(data)
        elif request_model.data_type == 6:
            return int32(data)
        elif request_model.data_type == 7:
            return uint64(data)
        elif request_model.data_type == 8:
            return int64(data)
        elif request_model.data_type == 9:
            return Address(address=data, network=self._network)
        elif request_model.data_type == 10:
            return bytearray(unhexlify(data))
        elif request_model.data_type == 11:
            return uint128(data)
        elif request_model.data_type == 12:
            return uint256(data)

    @endpoint(f'{route}/receipt')
    def receipt(self, tx_hash: Union[uint256, str], **kwargs) -> ReceiptModel:
        """Gets a smart contract transaction receipt.

        Args:
            tx_hash (uint256, str): The transaction hash of the smart contract receipt.
            **kwargs: Extra keyword arguments. 

        Returns:
            ReceiptModel: The smart contract transaction receipt.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(tx_hash, str):
            tx_hash = uint256(tx_hash)
        request_model = ReceiptRequest(tx_hash=tx_hash)
        data = self.get(request_model, **kwargs)
        if data['to'] is not None:
            data['to'] = Address(address=data['to'], network=self._network)
        data['from'] = Address(address=data['from'], network=self._network)
        data['newContractAddress'] = Address(address=data['newContractAddress'], network=self._network)
        for i in range(len(data['logs'])):
            data['logs'][i]['address'] = Address(address=data['logs'][i]['address'], network=self._network)
        return ReceiptModel(**data)

    @endpoint(f'{route}/receipt-search')
    def receipt_search(self,
                       contract_address: Union[Address, str],
                       topics: List[str] = None,
                       event_name: str = None,
                       from_block: int = 0,
                       to_block: int = None,
                       **kwargs) -> List[ReceiptModel]:
        """Searches a smart contract's receipts for those which match a specific event.

        Args:
            contract_address (Address, str): The address for the smart contract.
            event_name (str, optional): The event to search for.
            topics (List[str], optional): A list of topics to search for.
            from_block (int): Block to start search from.
            to_block (int): Block to search up to.
            **kwargs: Extra keyword arguments. 

        Returns:
            List[ReceiptModel]: A list of receipts.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(contract_address, str):
            contract_address = Address(address=contract_address, network=self._network)
        request_model = ReceiptSearchRequest(
            contract_address=contract_address,
            event_name=event_name,
            topics=topics,
            from_block=from_block,
            to_block=to_block
        )
        data = self.get(request_model, **kwargs)
        for i in range(len(data)):
            if data[i]['to'] is not None:
                data[i]['to'] = Address(address=data[i]['to'], network=self._network)
            data[i]['from'] = Address(address=data[i]['from'], network=self._network)
            if data[i]['newContractAddress'] is not None:
                data[i]['newContractAddress'] = Address(address=data[i]['newContractAddress'], network=self._network)
            for j in range(len(data[i]['logs'])):
                data[i]['logs'][j]['address'] = Address(address=data[i]['logs'][j]['address'], network=self._network)
        return [ReceiptModel(**x) for x in data]

    @endpoint(f'{route}/build-create')
    def build_create(self,
                     wallet_name: str,
                     fee_amount: Union[Money, int, float, Decimal],
                     password: str,
                     contract_code: Union[hexstr, str],
                     gas_price: int,
                     gas_limit: int,
                     sender: Union[Address, str],
                     amount: Union[Money, int, float, Decimal],
                     outpoints: List[Outpoint] = None,
                     account_name: str = 'account 0',
                     parameters: List[Union[str, SmartContractParameter]] = None,
                     **kwargs) -> BuildCreateContractTransactionModel:
        """Builds a transaction to create a smart contract.

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The wallet name. Default='account 0'
            outpoints (List[Outpoint], optional): A list of the outpoints used to construct the transactation.
            amount (Money, int, float, Decimal, optional): The amount being sent.
            fee_amount (Money, int, float, Decimal): The fee amount.
            password (SecretStr): The password.
            contract_code (hexstr, str): The smart contract code hexstring.
            gas_price (int): The amount of gas being used in satoshis.
            gas_limit (int): The maximum amount of gas that can be used in satoshis.
            sender (Address, str): The address of the sending address.
            parameters (List[Union[SmartContractParameter, str], optional): A list of parameters for the smart contract.
            **kwargs: Extra keyword arguments. 

        Returns:
            BuildCreateContractTransactionModel: A built create smart contract transaction.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(sender, str):
            sender = Address(address=sender, network=self._network)
        new_parameters = []
        if parameters is not None:
            for item in parameters:
                if isinstance(item, SmartContractParameter):
                    new_parameters.append(item)
                else:
                    assert isinstance(item, str)
                    value_type, value = item.split('#')
                    new_parameters.append(SmartContractParameter(value_type=value_type, value=value))
        request_model = BuildCreateContractTransactionRequest(
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
        data['fee'] = Money.from_satoshi_units(data['fee'])
        data['newContractAddress'] = Address(address=data['newContractAddress'], network=self._network)
        return BuildCreateContractTransactionModel(**data)

    @endpoint(f'{route}/build-call')
    def build_call(self,
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
                   parameters: List[Union[str, SmartContractParameter]] = None,
                   **kwargs) -> BuildContractTransactionModel:
        """Builds a transaction to call a smart contract method.

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The wallet name. Default='account 0'
            outpoints (List[Outpoint], optional): A list of the outpoints used to construct the transactation.
            contract_address (Address, str): The smart contract address being called.
            method_name (str): The method name being called.
            amount (Money, int, float, Decimal, optional): The amount being sent.
            fee_amount (Money, int, float, Decimal): The fee amount.
            password (SecretStr): The password.
            gas_price (int): The amount of gas being used in satoshis.
            gas_limit (int): The maximum amount of gas that can be used in satoshis.
            sender (Address, str): The address of the sending address.
            parameters (List[Union[SmartContractParameter, str]], optional): A list of parameters for the smart contract.
            **kwargs: Extra keyword arguments. 

        Returns:
            BuildContractTransactionModel: A built smart contract transaction.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(contract_address, str):
            contract_address = Address(address=contract_address, network=self._network)
        if isinstance(sender, str):
            sender = Address(address=sender, network=self._network)
        new_parameters = []
        if parameters is not None:
            for item in parameters:
                if isinstance(item, SmartContractParameter):
                    new_parameters.append(item)
                else:
                    assert isinstance(item, str)
                    value_type, value = item.split('#')
                    new_parameters.append(SmartContractParameter(value_type=value_type, value=value))
        request_model = BuildCallContractTransactionRequest(
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
        data['fee'] = Money.from_satoshi_units(data['fee'])
        return BuildContractTransactionModel(**data)

    @endpoint(f'{route}/build-transaction')
    def build_transaction(self,
                          sender: Union[Address, str],
                          password: str,
                          wallet_name: str,
                          recipients: List[Recipient],
                          op_return_data: str = None,
                          outpoints: List[Outpoint] = None,
                          op_return_amount: Union[Money, int, float, Decimal] = None,
                          fee_type: str = None,
                          allow_unconfirmed: bool = False,
                          shuffle_outputs: bool = False,
                          change_address: Union[Address, str] = None,
                          account_name: str = 'account 0',
                          segwit_change_address: bool = False,
                          fee_amount: Union[Money, int, float, Decimal] = None,
                          **kwargs) -> BuildContractTransactionModel:
        """Build a transaction to transfer funds on a smart contract network.

        Args:
            sender (Address): The sender address.
            fee_amount (Money, int, float, Decimal, optional): The fee amount.
            password (SecretStr): The password.
            segwit_change_address (bool, optional): If the change address is a segwit address. Default=False.
            wallet_name (str): The wallet name.
            account_name (str, optional): The account name. Default='account 0'.
            outpoints (List[Outpoint]): A list of the outpoints used to construct the transactation.
            recipients (List[Recipient]): A list of the recipients, including amounts, for the transaction.
            op_return_data (str, optional): OP_RETURN data to include with the transaction.
            op_return_amount (Money, int, float, Decimal, optional): Amount to burn in the OP_RETURN transaction.
            fee_type (str, optional): low, medium, or high.
            allow_unconfirmed (bool, optional): If True, allow unconfirmed transactions in the estimation. Default=False
            shuffle_outputs (bool, optional): If True, shuffles outputs. Default=False.
            change_address (Address, optional): Sends output sum less amount sent to recipients to this designated change address, if provided.
            **kwargs: Extra keyword arguments. 

        Returns:
            BuildContractTransactionModel: A built smart contract transaction.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(sender, str):
            sender = Address(address=sender, network=self._network)
        if change_address is not None and isinstance(change_address, str):
            change_address = Address(address=change_address, network=self._network)
        request_model = BuildTransactionRequest(
            sender=sender,
            fee_amount=fee_amount,
            password=password,
            segwit_change_address=segwit_change_address,
            wallet_name=wallet_name,
            account_name=account_name,
            outpoints=outpoints,
            recipients=recipients,
            op_return_data=op_return_data,
            op_return_amount=Money(op_return_amount) if op_return_amount is not None else None,
            fee_type=fee_type,
            allow_unconfirmed=allow_unconfirmed,
            shuffle_outputs=shuffle_outputs,
            change_address=change_address
        )
        data = self.post(request_model, **kwargs)
        data['fee'] = Money.from_satoshi_units(data['fee'])
        return BuildContractTransactionModel(**data)

    @endpoint(f'{route}/estimate-fee')
    def estimate_fee(self,
                     sender: Union[Address, str],
                     wallet_name: str,
                     recipients: List[Recipient],
                     fee_type: str,
                     outpoints: List[Outpoint] = None,
                     allow_unconfirmed: bool = False,
                     shuffle_outputs: bool = False,
                     op_return_data: str = None,
                     op_return_amount: Union[Money, int, float, Decimal] = None,
                     account_name: str = 'account 0',
                     change_address: Union[Address, str] = None,
                     **kwargs) -> Money:
        """Gets a fee estimate for a specific smart contract account-based transfer transaction.

        Args:
            sender (Address, str): The sender address.
            wallet_name (str): The wallet name.
            account_name (str, optional): The account name. Default='account 0'.
            outpoints (List[Outpoint], optional): A list of the outpoints used to construct the transactation.
            recipients (List[Recipient]): A list of the recipients, including amounts, for the transaction.
            op_return_data (str, optional): OP_RETURN data to include with the transaction.
            op_return_amount (Money, int, float, Decimal, optional): Amount to burn in the OP_RETURN transaction.
            fee_type (str, optional): low, medium, or high.
            allow_unconfirmed (bool, optional): If True, allow unconfirmed transactions in the estimation. Default=False
            shuffle_outputs (bool, optional): If True, shuffles outputs. Default=False.
            change_address (Address, str, optional): Sends output sum less amount sent to recipients to this designated change address, if provided.
            **kwargs: Extra keyword arguments. 

        Returns:
            Money: The fee estimate.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(sender, str):
            sender = Address(address=sender, network=self._network)
        if change_address is not None and isinstance(change_address, str):
            change_address = Address(address=change_address, network=self._network)
        request_model = EstimateFeeRequest(
            sender=sender,
            wallet_name=wallet_name,
            account_name=account_name,
            outpoints=outpoints,
            recipients=recipients,
            op_return_data=op_return_data,
            op_return_amount=Money(op_return_amount) if op_return_amount is not None else None,
            fee_type=fee_type,
            allow_unconfirmed=allow_unconfirmed,
            shuffle_outputs=shuffle_outputs,
            change_address=change_address
        )
        data = self.post(request_model, **kwargs)
        return Money.from_satoshi_units(data)

    @endpoint(f'{route}/build-and-send-create')
    def build_and_send_create(self,
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
                              parameters: List[Union[str, SmartContractParameter]] = None,
                              **kwargs) -> BuildCreateContractTransactionModel:
        """Builds a transaction to create a smart contract and then broadcasts.

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The wallet name. Default='account 0'
            outpoints (List[Outpoint], optional): A list of the outpoints used to construct the transactation.
            amount (Money, int, float, Decimal, optional): The amount being sent.
            fee_amount (Money, int, float, Decimal): The fee amount.
            password (SecretStr): The password.
            contract_code (hexstr, str): The smart contract code hexstring.
            gas_price (int): The amount of gas being used in satoshis.
            gas_limit (int): The maximum amount of gas that can be used in satoshis.
            sender (Address, str): The address of the sending address.
            parameters (List[Union[SmartContractParameter, str]], optional): A list of parameters for the smart contract.
            **kwargs: Extra keyword arguments. 

        Returns:
            BuildCreateContractTransactionModel: A built create smart contract transaction.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(sender, str):
            sender = Address(address=sender, network=self._network)
        new_parameters = []
        if parameters is not None:
            for item in parameters:
                if isinstance(item, SmartContractParameter):
                    new_parameters.append(item)
                else:
                    assert isinstance(item, str)
                    value_type, value = item.split('#')
                    new_parameters.append(SmartContractParameter(value_type=value_type, value=value))
        request_model = BuildAndSendCreateContractTransactionRequest(
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
        data['fee'] = Money.from_satoshi_units(data['fee'])
        data['newContractAddress'] = Address(address=data['newContractAddress'], network=self._network)
        return BuildCreateContractTransactionModel(**data)

    @endpoint(f'{route}/build-and-send-call')
    def build_and_send_call(self,
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
                            parameters: List[Union[str, SmartContractParameter]] = None,
                            **kwargs) -> BuildContractTransactionModel:
        """Builds a transaction to call a smart contract method and then broadcasts.

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The wallet name. Default='account 0'
            outpoints (List[Outpoint], optional): A list of the outpoints used to construct the transactation.
            contract_address (Address, str): The smart contract address being called.
            method_name (str): The method name being called.
            amount (Money, int, float, Decimal, optional): The amount being sent.
            fee_amount (Money, int, float, Decimal): The fee amount.
            password (SecretStr): The password.
            gas_price (int): The amount of gas being used in satoshis.
            gas_limit (int): The maximum amount of gas that can be used in satoshis.
            sender (Address, str): The address of the sending address.
            parameters (List[Union[SmartContractParameter, str]], optional): A list of parameters for the smart contract.
            **kwargs: Extra keyword arguments. 

        Returns:
            BuildContractTransactionModel: A built smart contract transaction.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(contract_address, str):
            contract_address = Address(address=contract_address, network=self._network)
        if isinstance(sender, str):
            sender = Address(address=sender, network=self._network)
        new_parameters = []
        if parameters is not None:
            for item in parameters:
                if isinstance(item, SmartContractParameter):
                    new_parameters.append(item)
                else:
                    assert isinstance(item, str)
                    value_type, value = item.split('#')
                    new_parameters.append(SmartContractParameter(value_type=value_type, value=value))
        request_model = BuildAndSendCallContractTransactionRequest(
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
        data['fee'] = Money.from_satoshi_units(data['fee'])
        return BuildContractTransactionModel(**data)

    @endpoint(f'{route}/local-call')
    def local_call(self,
                   contract_address: Union[Address, str],
                   method_name: str,
                   amount: Union[Money, int, float, Decimal],
                   gas_price: int,
                   gas_limit: int,
                   sender: Union[Address, str],
                   parameters: List[Union[str, SmartContractParameter]] = None,
                   **kwargs) -> LocalExecutionResultModel:
        """Makes a local call to a method on a smart contract that has been successfully deployed. The purpose is to query and test methods.

        Args:
            contract_address (Address, str): The smart contract address being called.
            method_name (str): The smart contract method being called.
            amount (Money, int, float, Decimal): The amount being sent.
            gas_price (int): The amount of gas being used in satoshis.
            gas_limit (int): The maximum amount of gas that can be used in satoshis.
            sender (Address, str): The address of the sending address.
            parameters (List[Union[SmartContractParameter, str]], optional): A list of parameters for the smart contract.
            **kwargs: Extra keyword arguments. 

        Returns:
            LocalExecutionResultModel: The results of a local contract execution.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(contract_address, str):
            contract_address = Address(address=contract_address, network=self._network)
        if isinstance(sender, str):
            sender = Address(address=sender, network=self._network)
        new_parameters = []
        if parameters is not None:
            for item in parameters:
                if isinstance(item, SmartContractParameter):
                    new_parameters.append(item)
                else:
                    assert isinstance(item, str)
                    value_type, value = item.split('#')
                    new_parameters.append(SmartContractParameter(value_type=value_type, value=value))
        request_model = LocalCallContractTransactionRequest(
            contract_address=contract_address,
            method_name=method_name,
            amount=Money(amount),
            gas_price=gas_price,
            gas_limit=gas_limit,
            sender=sender,
            parameters=new_parameters
        )
        data = self.post(request_model, **kwargs)
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

    @endpoint(f'{route}/address-balances')
    def address_balances(self, wallet_name: str, **kwargs) -> List[AddressBalanceModel]:
        """Gets all addresses owned by a wallet which have a balance associated with them.

        Args:
            wallet_name (str): The wallet name.
            **kwargs: Extra keyword arguments. 

        Returns:
            List[AddressBalanceModel]: A list of addresses with balance information.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = BalancesRequest(wallet_name=wallet_name)
        data = self.get(request_model, **kwargs)
        for i in range(len(data)):
            data[i]['address'] = Address(address=data[i]['address'], network=self._network)
            data[i]['sum'] = Money.from_satoshi_units(data[i]['sum'])
        return [AddressBalanceModel(**x) for x in data]
