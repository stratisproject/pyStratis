from typing import Union, List
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.blockstore.requestmodels import *
from pystratis.api.blockstore.responsemodels import *
from pystratis.core import TransactionModel
from pystratis.core.types import Address, hexstr, Money, uint256


class BlockStore(APIRequest, metaclass=EndpointRegister):
    """Implements the stratis blockstore api endpoints."""
    route = '/api/blockstore'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/addressindexertip')
    def addressindexer_tip(self,
                           **kwargs) -> AddressIndexerTipModel:
        """Retrieves the address indexer tip.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            AddressIndexerTipModel

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return AddressIndexerTipModel(**data)

    @endpoint(f'{route}/block')
    def block(self,
              block_hash: Union[uint256, str],
              show_transaction_details: bool = True,
              output_json: bool = True,
              **kwargs) -> Union[BlockModel, BlockTransactionDetailsModel, hexstr, str]:
        """Retrieves the block which matches the supplied block hash.

        Args:
            block_hash (uint256 | str): The hash of the required block.
            show_transaction_details (bool, optional): A flag that indicates whether to return each block
                transaction complete with details or simply return transaction hashes. Default=True.
            output_json (bool): Output json or hex block. Default=True.
            **kwargs: Extra keyword arguments. 

        Returns:
            Union[BlockModel, BlockTransactionDetailsModel, hexstr, str]

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

    @endpoint(f'{route}/getblockcount')
    def get_block_count(self, **kwargs) -> int:
        """Gets the current block count.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            int

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return data

    @endpoint(f'{route}/getaddressesbalances')
    def get_addresses_balances(self,
                               addresses: Union[List[Union[Address, str]], Address, str],
                               min_confirmations: int = 0,
                               **kwargs) -> GetAddressesBalancesModel:
        """Provides balance of the given addresses confirmed with at least min_confirmations confirmations.

        Args:
            addresses (List(Address | str) | Address | str): A list of addresses or single address to query.
            min_confirmations (int, optional): Only blocks below consensus tip less this parameter will be considered. Default=0.
            **kwargs: Extra keyword arguments. 

        Returns:
            GetAddressesBalancesModel

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(addresses, list):
            for i in range(len(addresses)):
                if isinstance(addresses[i], str):
                    addresses[i] = Address(address=addresses[i], network=self._network)
        if isinstance(addresses, str):
            addresses = Address(address=addresses, network=self._network)
        request_model = GetAddressesBalancesRequest(addresses=addresses, min_confirmations=min_confirmations)
        data = self.get(request_model, **kwargs)
        for i in range(len(data['balances'])):
            data['balances'][i]['address'] = Address(address=data['balances'][i]['address'], network=self._network)
            data['balances'][i]['balance'] = Money.from_satoshi_units(data['balances'][i]['balance'])
        return GetAddressesBalancesModel(**data)

    @endpoint(f'{route}/getverboseaddressesbalances')
    def get_verbose_addresses_balances(self,
                                       addresses: Union[List[Union[Address, str]], Address, str],
                                       **kwargs) -> GetVerboseAddressesBalancesModel:
        """Provides verbose balance data of the given addresses.

        Args:
            addresses (List(Address | str) | Address | str): A list of addresses or single address to query.
            **kwargs: Extra keyword arguments. 

        Returns:
            GetVerboseAddressesBalancesModel

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(addresses, list):
            for i in range(len(addresses)):
                if isinstance(addresses[i], str):
                    addresses[i] = Address(address=addresses[i], network=self._network)
        if isinstance(addresses, str):
            addresses = Address(address=addresses, network=self._network)
        request_model = GetVerboseAddressesBalancesRequest(addresses=addresses)
        data = self.get(request_model, **kwargs)
        for i in range(len(data['balancesData'])):
            data['balancesData'][i]['address'] = Address(address=data['balancesData'][i]['address'], network=self._network)
        return GetVerboseAddressesBalancesModel(**data)

    @endpoint(f'{route}/getutxoset')
    def get_utxo_set(self,
                     at_block_height: int,
                     **kwargs) -> List[UTXOModel]:
        """Gets the UTXO set at the specified block height.

        Args:
            at_block_height (int): The specified block height.
            **kwargs: Extra keyword arguments. 

        Returns:
            List[UTXOModel]

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = GetUTXOSetRequest(at_block_height=at_block_height)
        data = self.get(request_model, **kwargs)
        for i in range(len(data)):
            data[i]['value'] = Money.from_satoshi_units(data[i]['value'])
        return [UTXOModel(**x) for x in data]

    @endpoint(f'{route}/getlastbalanceupdatetransaction')
    def get_last_balance_update_transaction(self,
                                            address: Union[Address, str],
                                            **kwargs) -> Union[GetLastBalanceUpdateTransactionModel, None]:
        """A

        Args:
            address (Address): An address to query.
            **kwargs: Extra keyword arguments. 

        Returns:
            A GetLastBalanceUpdateTransactionModel if transaction exists, otherwise None.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(address, str):
            address = Address(address=address, network=self._network)
        request_model = GetLastBalanceUpdateTransactionRequest(address=address)
        data = self.get(request_model, **kwargs)
        return None if data is None else GetLastBalanceUpdateTransactionModel(**data)
