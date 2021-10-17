from typing import List, Union
from decimal import Decimal
import ast
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.unity3d.requestmodels import *
from pystratis.api.unity3d.responsemodels import *
from pystratis.core.types import Address, Money, uint256, hexstr
from pystratis.core import SmartContractParameter


class Unity3D(APIRequest, metaclass=EndpointRegister):
    """Implements the unity3dapi endpoints."""

    route = '/unity3d'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/getutxosforaddress')
    def get_utxos_for_address(self, address: Union[str, Address], **kwargs) -> GetUTXOModel:
        """Gets UTXOs for specified address.

        Args:
            address (str, Address): The address.
            **kwargs: Extra keyword arguments.

        Returns:
            GetUTXOModel: UTXOs for the specified address.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(address, str):
            address = Address(address=address, network=self._network)
        request_model = AddressRequest(address=address)
        data = self.get(request_model, **kwargs)
        if data['balanceSat'] is not None:
            data['balanceSat'] = Money.from_satoshi_units(data['balanceSat'])
        if data['utxOs'] is not None:
            for i in range(len(data['utxOs'])):
                data['utxOs'][i]['satoshis'] = Money.from_satoshi_units(data['utxOs'][i]['satoshis'])
            data['utxOs'] = [UTXOModel(**x) for x in data['utxOs']]
        return GetUTXOModel(**data)

    @endpoint(f'{route}/getaddressbalance')
    def get_address_balance(self, address: Union[str, Address], **kwargs) -> Money:
        """Provides balance of the given address confirmed with at least 1 confirmation.

        Args:
            address (str, Address): The address.
            **kwargs: Extra keyword arguments.

        Returns:
            Money: The amount in the address.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(address, str):
            address = Address(address=address, network=self._network)
        request_model = AddressRequest(address=address)
        data = self.get(request_model, **kwargs)
        return Money.from_satoshi_units(data)

    @endpoint(f'/api/{route}/getblockheader')
    def get_blockheader(self,
                        block_hash: Union[str, uint256],
                        is_json_format: bool = True,
                        **kwargs) -> BlockHeaderModel:
        """Gets the specified block header.

        Args:
            block_hash (str, uint256): The specified block hash.
            is_json_format (bool, optional): If block header should be returned as json. Default=True.
            **kwargs: Extra keyword arguments.

        Returns:
            BlockHeaderModel: The block headers.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(block_hash, str):
            block_hash = uint256(block_hash)
        request_model = GetBlockHeaderRequest(block_hash=block_hash, is_json_format=is_json_format)
        data = self.get(request_model, **kwargs)

        return BlockHeaderModel(**data)

    @endpoint(f'/api/{route}/getrawtransaction')
    def get_raw_transaction(self,
                            trxid: Union[uint256, str],
                            verbose: bool = False,
                            **kwargs) -> Union[hexstr, TransactionModel]:
        """Gets a raw transaction from a transaction id.

        Requires txindex=1 in node configuration.

        Args:
            trxid (uint256, str): The transaction hash.
            verbose (bool, optional): If output should include verbose transaction data. Default=False.
            **kwargs: Extra keyword arguments.

        Returns:
            Union[hexstr, TransactionModel]: A raw transaction.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(trxid, str):
            trxid = uint256(trxid)
        request_model = GetRawTransactionRequest(trxid=trxid, verbose=verbose)
        data = self.get(request_model, **kwargs)
        if data is None:
            raise RuntimeWarning('Transaction not found. Is -txindex=1 enabled?')
        if not request_model.verbose:
            return hexstr(data)
        return TransactionModel(**data)

    @endpoint(f'/api/{route}/send-transaction')
    def send_transaction(self,
                         transaction_hex: Union[str, hexstr],
                         **kwargs) -> WalletSendTransactionModel:
        """Sends a transaction that has already been built.

        Args:
            transaction_hex (hexstr, str): The hexified transaction.
            **kwargs: Extra keyword arguments.

        Returns:
            WalletSendTransactionModel: Information about a sent transaction.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(transaction_hex, str):
            transaction_hex = hexstr(transaction_hex)
        request_model = SendTransactionRequest(transaction_hex=transaction_hex)
        data = self.post(request_model, **kwargs)
        for i in range(len(data['outputs'])):
            if 'address' in data['outputs'][i]:
                data['outputs'][i]['address'] = Address(address=data['outputs'][i]['address'], network=self._network)
                data['outputs'][i]['amount'] = Money.from_satoshi_units(data['outputs'][i]['amount'])
            data['outputs'][i] = TransactionOutputModel(**data['outputs'][i])
        return WalletSendTransactionModel(**data)

    @endpoint(f'/api/{route}/validateaddress')
    def validate_address(self, address: str, **kwargs) -> ValidateAddressModel:
        """Validate an address

        Args:
            address (str): The address to validate.
            **kwargs: Extra keyword arguments.

        Returns:
            ValidateAddressModel: Information on the validity of the provided address, and if valid, if it is a witness or script address.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = ValidateAddressRequest(address=address)
        data = self.get(request_model, **kwargs)
        data['address'] = Address(address=data['address'], network=self._network)
        return ValidateAddressModel(**data)

    @endpoint(f'/api/{route}/block')
    def block(self,
              block_hash: Union[uint256, str],
              show_transaction_details: bool = True,
              output_json: bool = True,
              **kwargs) -> Union[BlockModel, BlockTransactionDetailsModel, hexstr, str]:
        """Retrieves the block which matches the supplied block hash.

        Args:
            block_hash (uint256, str): The hash of the required block.
            show_transaction_details (bool, optional): A flag that indicates whether to return each block
                transaction complete with details or simply return transaction hashes. Default=True.
            output_json (bool): Output json or hex block. Default=True.
            **kwargs: Extra keyword arguments.

        Returns:
            (BlockModel, BlockTransactionDetailsModel, hexstr, str): The representation of the block.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(block_hash, str):
            block_hash = uint256(block_hash)
        request_model = BlockRequest(block_hash=block_hash, show_transaction_details=show_transaction_details, output_json=output_json)
        data = self.get(request_model, **kwargs)
        if isinstance(data, str):
            try:
                return hexstr(data)
            except ValueError:
                return data
        if request_model.show_transaction_details:
            data['transactions'] = [TransactionModel(**x) for x in data['transactions']]
            return BlockTransactionDetailsModel(**data)
        else:
            return BlockModel(**data)

    @endpoint(f'/api/{route}/tip')
    def addressindexer_tip(self, **kwargs) -> AddressIndexerTipModel:
        """Retrieves the address indexer tip.

        Args:
            **kwargs: Extra keyword arguments.

        Returns:
            AddressIndexerTipModel: The address indexer tip hash and height.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return AddressIndexerTipModel(**data)

    @endpoint(f'/api/{route}/reciept')
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

    @endpoint(f'/api/{route}/local-call')
    def local_call(self,
                   contract_address: Union[Address, str],
                   method_name: str,
                   amount: Union[Money, int, float, Decimal],
                   gas_price: int,
                   gas_limit: int,
                   sender: Union[Address, str],
                   block_height: int = None,
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
            block_height (int, optional): The height at which to query the contract's state. If unset, will default to the current chain tip.
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
            block_height=block_height,
            parameters=new_parameters
        )
        data = self.post(request_model, **kwargs)
        for i in range(len(data['internalTransfers'])):
            data['internalTransfers'][i]['from'] = Address(address=data['internalTransfers'][i]['from'], network=self._network)
            data['internalTransfers'][i]['to'] = Address(address=data['internalTransfers'][i]['to'], network=self._network)
        for i in range(len(data['logs'])):
            if isinstance(data['logs'][i]['address'], str):
                data['logs'][i]['address'] = Address(address=data['logs'][i]['address'], network=self._network)
            else:
                data['logs'][i]['address'] = None
        if data['errorMessage'] is not None:
            data['errorMessage'] = ast.literal_eval(data['errorMessage'])
            data['errorMessage'] = data['errorMessage']['value']
        if data['gasConsumed'] is not None:
            data['gasConsumed'] = data['gasConsumed']['value']
        if data['return'] is not None:
            data['return'] = data['return']
        return LocalExecutionResultModel(**data)
