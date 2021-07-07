from typing import List, Union
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.federationgateway.responsemodels import *
from pystratis.api.federationgateway.requestmodels import *
from pystratis.core import DestinationChain
from pystratis.core.types import Address, Money, uint256
from pystratis.core.networks import StraxMain, StraxTest, StraxRegTest, CirrusMain, CirrusTest, CirrusRegTest, Ethereum


class FederationGateway(APIRequest, metaclass=EndpointRegister):
    """Implements the federationgateway api endpoints."""

    route = '/api/federationgateway'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/deposits')
    def deposits(self, block_height: int, **kwargs) -> List[MaturedBlockDepositsModel]:
        """Retrieves block deposits

        Args:
            block_height (int): The block height at which to obtain deposits.
            **kwargs: Extra keyword arguments. 

        Returns:
            List[MaturedBlockDepositsModel]: A list of matured block deposits.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = DepositsRequest(block_height=block_height)
        data = self.get(request_model, **kwargs)

        serializable_result = SerializableResult(**data)

        matured_block_deposit_models = []
        for item in serializable_result.value:
            data = {'deposits': [], 'blockInfo': item['blockInfo']}
            for deposit in item['deposits']:
                deposit['amount'] = Money.from_satoshi_units(deposit['amount'])
                if 'targetChain' in deposit:
                    if deposit['targetChain'] == DestinationChain.ETH.value:
                        deposit['targetAddress'] = Address(address=deposit['targetAddress'], network=Ethereum())
                    else:
                        chain_name = DestinationChain(deposit['targetChain']).name
                        raise RuntimeWarning(f'Validation for {chain_name} not implemented.')
                else:
                    if self._network == StraxMain():
                        deposit['targetAddress'] = Address(address=deposit['targetAddress'], network=CirrusMain())
                    if self._network == CirrusMain():
                        deposit['targetAddress'] = Address(address=deposit['targetAddress'], network=StraxMain())
                    if self._network == StraxTest():
                        deposit['targetAddress'] = Address(address=deposit['targetAddress'], network=CirrusTest())
                    if self._network == CirrusTest():
                        deposit['targetAddress'] = Address(address=deposit['targetAddress'], network=StraxTest())
                    if self._network == StraxRegTest() or self._network == CirrusRegTest():
                        deposit['targetAddress'] = Address(address=deposit['targetAddress'], network=StraxRegTest())
                    if self._network == StraxRegTest() or self._network == CirrusRegTest():
                        deposit['targetAddress'] = Address(address=deposit['targetAddress'], network=StraxRegTest())
                data['deposits'].append(deposit)
            matured_block_deposit_models.append(MaturedBlockDepositsModel(**data))
        return matured_block_deposit_models

    @endpoint(f'{route}/transfer/pending')
    def pending_transfer(self,
                         deposit_id: Union[str, uint256],
                         transaction_id: Union[str, uint256],
                         **kwargs) -> List[CrossChainTransferModel]:
        """Gets pending transfers.

        Args:
            deposit_id (uint256, str): The deposit id hash.
            transaction_id (uint256, str): The transaction id hash.
            **kwargs: Extra keyword arguments. 

        Returns:
            List[CrossChainTransferModel]: A list of cross chain transfers.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(deposit_id, str):
            deposit_id = uint256(deposit_id)
        if isinstance(transaction_id, str):
            transaction_id = uint256(transaction_id)
        request_model = PendingTransferRequest(deposit_id=deposit_id, transaction_id=transaction_id)
        data = self.get(request_model, **kwargs)
        return [CrossChainTransferModel(**x) for x in data]

    @endpoint(f'{route}/transfer/fullysigned')
    def fullysigned_transfer(self,
                             deposit_id: Union[str, uint256],
                             transaction_id: Union[str, uint256],
                             **kwargs) -> List[CrossChainTransferModel]:
        """Get fully signed transfers.

        Args:
            deposit_id (uint256, str): The deposit id hash.
            transaction_id (uint256, str): The transaction id hash.
            **kwargs: Extra keyword arguments. 

        Returns:
            List[CrossChainTransferModel]: A list of cross chain transfers.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(deposit_id, str):
            deposit_id = uint256(deposit_id)
        if isinstance(transaction_id, str):
            transaction_id = uint256(transaction_id)
        request_model = FullySignedTransferRequest(deposit_id=deposit_id, transaction_id=transaction_id)
        data = self.get(request_model, **kwargs)

        return [CrossChainTransferModel(**x) for x in data]

    @endpoint(f'{route}/member/info')
    def member_info(self, **kwargs) -> FederationMemberInfoModel:
        """Gets info on the state of a multisig member.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            FederationMemberInfoModel: Information on the current multisig member.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)

        return FederationMemberInfoModel(**data)

    @endpoint(f'{route}/info')
    def info(self, **kwargs) -> FederationGatewayInfoModel:
        """Gets info on the state of the federation.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            FederationGatewayInfoModel: Information on the federation gateway.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        data['multisigAddress'] = Address(address=data['multisigAddress'], network=self._network)
        return FederationGatewayInfoModel(**data)

    @endpoint(f'{route}/member/ip/add')
    def ip_add(self, ipaddr: str, **kwargs) -> str:
        """Add a federation member's IP address to the federation IP list

        Args:
            ipaddr (str): The endpoint.
            **kwargs: Extra keyword arguments. 

        Returns:
            str: Response to ip add request.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = MemberIPAddRequest(ipaddr=ipaddr)
        data = self.put(request_model, **kwargs)
        return data

    @endpoint(f'{route}/member/ip/remove')
    def ip_remove(self, ipaddr: str, **kwargs) -> str:
        """Remove a federation member's IP address to the federation IP list

        Args:
            ipaddr (str): The endpoint.
            **kwargs: Extra keyword arguments. 

        Returns:
            str: response to ip remove request.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = MemberIPRemoveRequest(ipaddr=ipaddr)
        data = self.put(request_model, **kwargs)
        return data

    @endpoint(f'{route}/member/ip/replace')
    def ip_replace(self, ipaddrtouse: str, ipaddr: str, **kwargs) -> str:
        """Replace a federation member's IP from the federation IP list with another.

        Args:
            ipaddrtouse (str): The new endpoint.
            ipaddr (str): The endpoint being replaced.
            **kwargs: Extra keyword arguments. 

        Returns:
            str: Response to ip replace request.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = MemberIPReplaceRequest(ipaddrtouse=ipaddrtouse, ipaddr=ipaddr)
        data = self.put(request_model, **kwargs)
        return data

    @endpoint(f'{route}/transfer/verify')
    def verify_transfer(self,
                        deposit_id_transaction_id: Union[str, uint256],
                        **kwargs) -> Union[str, ValidateTransactionResultModel]:
        """Validate a transfer transaction.

        Args:
            deposit_id_transaction_id (uint256, str): The transaction id containing the deposit with the deposit id.
            **kwargs: Extra keyword arguments. 

        Returns:
            Union[str, ValidateTransactionResultModel]: A model describing the validity of the transfer.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(deposit_id_transaction_id, str):
            deposit_id_transaction_id = uint256(deposit_id_transaction_id)
        request_model = VerifyTransferRequest(deposit_id_transaction_id=deposit_id_transaction_id)
        data = self.get(request_model, **kwargs)
        if isinstance(data, str):
            return data
        return ValidateTransactionResultModel(**data)
