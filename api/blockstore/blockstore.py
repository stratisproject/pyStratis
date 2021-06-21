from typing import Union, List
from api import APIRequest, EndpointRegister, endpoint
from api.blockstore.responsemodels import *
from api.blockstore.requestmodels import *
from pybitcoin.types import Address, hexstr, Money


class BlockStore(APIRequest, metaclass=EndpointRegister):
    """Implements the stratis blockstore api endpoints."""
    route = '/api/blockstore'

    def __init__(self, **kwargs):
        super(BlockStore, self).__init__(**kwargs)

    @endpoint(f'{route}/addressindexertip')
    def addressindexer_tip(self, **kwargs) -> AddressIndexerTipModel:
        """Retrieves the address indexer tip.

        Args:
            **kwargs:

        Returns:
            AddressIndexerTipModel

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return AddressIndexerTipModel(**data)

    @endpoint(f'{route}/block')
    def block(self, request_model: BlockRequest, **kwargs) -> Union[BlockModel, hexstr, str]:
        """Retrieves a block.

        Args:
            request_model: BlockRequest model
            **kwargs:

        Returns:
            Union[BlockModel, hexstr, str]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        if isinstance(data, str):
            try:
                return hexstr(data)
            except ValueError:
                return data

        if request_model.show_transaction_details:
            return BlockTransactionDetailsModel(**data)
        else:
            return BlockModel(**data)

    @endpoint(f'{route}/getblockcount')
    def get_block_count(self, **kwargs) -> int:
        """Gets the current block count.

        Args:
            **kwargs:

        Returns:
            int

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return data

    @endpoint(f'{route}/getaddressesbalances')
    def get_addresses_balances(self, request_model: GetAddressesBalancesRequest, **kwargs) -> GetAddressesBalancesModel:
        """Gets the current balances for specified address(es)

        Args:
            request_model: A GetAddressBalancesRequest model
            **kwargs:

        Returns:
            GetAddressesBalancesModel

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        for i in range(len(data['balances'])):
            data['balances'][i]['address'] = Address(
                address=data['balances'][i]['address'],
                network=self._network
            )
            data['balances'][i]['balance'] = Money.from_satoshi_units(data['balances'][i]['balance'])
        return GetAddressesBalancesModel(**data)

    @endpoint(f'{route}/getverboseaddressesbalances')
    def get_verbose_addresses_balances(self, request_model: GetVerboseAddressesBalancesRequest, **kwargs) -> GetVerboseAddressesBalancesModel:
        """Gets a verbose account of balances of the specified address(es).

        Args:
            request_model: A GetVerboseAddressesBalancesRequest model.
            **kwargs:

        Returns:
            GetVerboseAddressesBalancesModel

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        for i in range(len(data['balancesData'])):
            data['balancesData'][i]['address'] = Address(
                address=data['balancesData'][i]['address'],
                network=self._network
            )

        return GetVerboseAddressesBalancesModel(**data)

    @endpoint(f'{route}/getutxoset')
    def get_utxo_set(self, request_model: GetUTXOSetRequest, **kwargs) -> List[UTXOModel]:
        """Gets the UTXO set at the specified block height.

        Args:
            request_model: A GetUTXOSetRequest model.
            **kwargs:

        Returns:
            List[UTXOModel]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)
        for i in range(len(data)):
            data[i]['value'] = Money.from_satoshi_units(data[i]['value'])

        return [UTXOModel(**x) for x in data]

    @endpoint(f'{route}/getlastbalanceupdatetransaction')
    def get_last_balance_update_transaction(self, request_model: GetLastBalanceUpdateTransactionRequest, **kwargs) -> Union[GetLastBalanceUpdateTransactionModel, None]:
        """A

        Args:
            request_model: A GetLastBalanceUpdateTransactionRequest
            **kwargs:

        Returns:
            A GetLastBalanceUpdateTransactionModel if transaction exists, otherwise None.

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return None if data is None else GetLastBalanceUpdateTransactionModel(**data)
