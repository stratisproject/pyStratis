from typing import Union, List
from api import APIRequest, EndpointRegister, endpoint
from api.node.requestmodels import *
from api.node.responsemodels import *
from pybitcoin import ScriptPubKey
from pybitcoin.types import Address, hexstr, Money


class Node(APIRequest, metaclass=EndpointRegister):
    route = '/api/node'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/status')
    def status(self, **kwargs) -> StatusModel:
        """Gets the node status.

        Args:
            **kwargs:

        Returns:
            StatusModel

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return StatusModel(**data)

    @endpoint(f'{route}/getblockheader')
    def get_blockheader(self, request_model: GetBlockHeaderRequest, **kwargs) -> BlockHeaderModel:
        """Gets the specified block header.

        Args:
            request_model: GetBlockHeaderRequest model
            **kwargs:

        Returns:
            BlockHeaderModel

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return BlockHeaderModel(**data)

    @endpoint(f'{route}/getrawtransaction')
    def get_raw_transaction(self, request_model: GetRawTransactionRequest, **kwargs) -> Union[hexstr, TransactionModel]:
        """Gets a raw transaction from a transaction id.

        Args:
            request_model: GetRawTransactionRequest model
            **kwargs:

        Returns:
            Union[hexstr, TransactionModel]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)
        if data is None:
            raise RuntimeWarning('Transaction not found. Is -txindex=1 enabled?')
        if not request_model.verbose:
            return hexstr(data)
        return TransactionModel(**data)

    @endpoint(f'{route}/decoderawtransaction')
    def decode_raw_transaction(self, request_model: DecodeRawTransactionRequest, **kwargs) -> TransactionModel:
        """Decodes raw transaction hex into a transaction model.

        Args:
            request_model: DecodeRawTransactionRequest model
            **kwargs:

        Returns:
            TransactionModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return TransactionModel(**data)

    @endpoint(f'{route}/validateaddress')
    def validate_address(self, request_model: ValidateAddressRequest, **kwargs) -> ValidateAddressModel:
        """Validate an address

        Args:
            request_model: ValidateAddressRequest model
            **kwargs:

        Returns:
            ValidateAddressModel

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)
        data['address'] = Address(address=data['address'], network=self._network)

        return ValidateAddressModel(**data)

    @endpoint(f'{route}/gettxout')
    def get_txout(self, request_model: GetTxOutRequest, **kwargs) -> GetTxOutModel:
        """Gets a specified txout from a given transaction.

        Args:
            request_model: GetTxOutRequest model
            **kwargs:

        Returns:
            GetTxOutModel

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)
        if data is not None:
            if 'value' in data:
                data['value'] = Money.from_satoshi_units(data['value'])
            if 'scriptPubKey' in data:
                data['scriptPubKey'] = ScriptPubKey(**data['scriptPubKey'])
            return GetTxOutModel(**data)

    @endpoint(f'{route}/gettxoutproof')
    def get_txout_proof(self, request_model: GetTxOutProofRequest, **kwargs) -> hexstr:
        """The merkle proof that the specified transaction exist in a given block.

        Should have txindex enabled if not specifying blockhash.

        Args:
            request_model: GetTxOutProofRequest model
            **kwargs:

        Returns:
            hexstr

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return hexstr(data)

    @endpoint(f'{route}/shutdown')
    def shutdown(self, request_model: ShutdownRequest = ShutdownRequest(), **kwargs) -> None:
        """Triggers node shutdown.

        Args:
            request_model: ShutdownRequest model
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/stop')
    def stop(self, request_model: ShutdownRequest = ShutdownRequest(), **kwargs) -> None:
        """Triggers node shutdown.

        Args:
            request_model: The ShutdownRequest model.
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/loglevels')
    def log_levels(self, request_model: LogRulesRequest, **kwargs) -> None:
        """Changes log level for the specified loggers.

        Args:
            request_model: The LogRulesRequest model.
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        self.put(request_model, **kwargs)

    @endpoint(f'{route}/logrules')
    def log_rules(self, **kwargs) -> List[LogRulesModel]:
        """Returns the enabled log rules.

        Args:
            **kwargs:

        Returns:
            List[LogRulesModel]

        Raises:
            APIError

        """
        data = self.get(**kwargs)

        return [LogRulesModel(**x) for x in data]

    @endpoint(f'{route}/asyncloops')
    def async_loops(self, **kwargs) -> List[AsyncLoopsModel]:
        """Gets the currently running async loops.

        Args:
            **kwargs:

        Returns:
            List[AsyncLoopsModel]

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return [AsyncLoopsModel(**x) for x in data]
