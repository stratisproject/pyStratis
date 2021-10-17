from typing import List, Union
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.interop.responsemodels import *
from pystratis.api.interop.requestmodels import *
from pystratis.core.types import Address, Money, uint256, hexstr
from pystratis.core.networks import Ethereum
from pystratis.core import PubKey


class Interop(APIRequest, metaclass=EndpointRegister):
    """Implements the interop api endpoints."""

    route = '/api/interop'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/status/burns')
    def status_burns(self, **kwargs) -> List[ConversionRequestModel]:
        """Gets the current interop status of burns.

        Args:
            **kwargs: Extra keyword arguments.

        Returns:
            List[ConversionRequestModel]: A list of burn conversion requests.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        for i in range(len(data['burnRequests'])):
            data['burnRequests'][i]['amount'] = Money(data['burnRequests'][i]['amount'])
            data['burnRequests'][i]['destinationAddress'] = Address(
                address=data['burnRequests'][i]['destinationAddress'],
                network=self._network
            )
        return [ConversionRequestModel(**x) for x in data['burnRequests']]

    @endpoint(f'{route}/status/mints')
    def status_mints(self, **kwargs) -> List[ConversionRequestModel]:
        """Gets the current interop status of mints.

        Args:
            **kwargs: Extra keyword arguments.

        Returns:
            List[ConversionRequestModel]: A list of mint conversion requests.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        for i in range(len(data['mintRequests'])):
            data['mintRequests'][i]['amount'] = Money(data['mintRequests'][i]['amount'])
            data['mintRequests'][i]['destinationAddress'] = Address(
                address=data['mintRequests'][i]['destinationAddress'],
                network=Ethereum()
            )
        return [ConversionRequestModel(**x) for x in data['mintRequests']]

    @endpoint(f'{route}/status/votes')
    def status_votes(self, **kwargs) -> dict:
        """Gets the current interop status of votes.

        Args:
            **kwargs: Extra keyword arguments.

        Returns:
            dict: A dictionary of votes with {request_id: [pubkeys_that_voted]}

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        received_votes = {}
        if data['receivedVotes'] is not None:
            for key in data['receivedVotes']:
                values = [PubKey(x) for x in data['receivedVotes'][key]]
                received_votes[uint256(key)] = values
        return received_votes

    @endpoint(f'{route}/owners')
    def owners(self, destination_chain: int, **kwargs) -> List[str]:
        """Retrieves the list of current owners for the multisig wallet contract.

        Args:
            destination_chain (int): The destination chain.
            **kwargs: Extra keyword arguments.

        Returns:
            List[str]: A list of owners of the multisig contract.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = OwnersRequest(destination_chain=destination_chain)
        data = self.get(request_model, **kwargs)
        return data

    @endpoint(f'{route}/addowner')
    def add_owner(self,
                  destination_chain: int,
                  new_owner_address: Union[str, Address],
                  gas_price: int,
                  **kwargs) -> uint256:
        """Creates and broadcasts an addOwner contract call on the multisig wallet contract. This can only be done by one of the current owners of the contract, and needs to be confirmed by a sufficient number of the other owners.

        Args:
            destination_chain (int): The destination chain.
            new_owner_address (str, Address): The address to add to multisig ownership.
            gas_price (int): The gas price.
            **kwargs: Extra keyword arguments.

        Returns:
            uint256: The transactionId of the multisig wallet contract transaction, which is then used to confirm the transaction.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(new_owner_address, str):
            new_owner_address = Address(address=new_owner_address, network=self._network)
        request_model = AddOwnerRequest(
            destination_chain=destination_chain,
            new_owner_address=new_owner_address,
            gas_price=gas_price
        )
        data = self.get(request_model, **kwargs)
        return uint256(data)

    @endpoint(f'{route}/removeowner')
    def remove_owner(self,
                     destination_chain: int,
                     existing_owner_address: Union[str, Address],
                     gas_price: int,
                     **kwargs) -> uint256:
        """Creates and broadcasts a removeOwner contract call on the multisig wallet contract. This can only be done by one of the current owners of the contract, and needs to be confirmed by a sufficient number of the other owners.

        Args:
            destination_chain (int): The destination chain.
            existing_owner_address (str, Address): The address to add to multisig ownership.
            gas_price (int): The gas price.
            **kwargs: Extra keyword arguments.

        Returns:
            uint256: The transactionId of the multisig wallet contract transaction, which is then used to confirm the transaction.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(existing_owner_address, str):
            existing_owner_address = Address(address=existing_owner_address, network=self._network)
        request_model = RemoveOwnerRequest(
            destination_chain=destination_chain,
            existing_owner_address=existing_owner_address,
            gas_price=gas_price
        )
        data = self.get(request_model, **kwargs)
        return uint256(data)

    @endpoint(f'{route}/confirmtransaction')
    def confirm_transaction(self,
                            destination_chain: int,
                            transaction_id: int,
                            gas_price: int,
                            **kwargs) -> uint256:
        """Explicitly confirms a given multisig wallet contract transactionId by submitting a contract call transaction to the network.

        This can only be called once per multisig owner. Additional calls by the same owner account will simply fail and waste gas.

        Args:
            destination_chain (int): The destination chain.
            transaction_id (int): The multisig wallet transactionId (int, not transaction hash).
            gas_price (int): The gas price.
            **kwargs: Extra keyword arguments.

        Returns:
            uint256: The on-chain transaction hash of the contract call transaction.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = ConfirmTransactionRequest(
            destination_chain=destination_chain,
            transaction_id=transaction_id,
            gas_price=gas_price
        )
        data = self.get(request_model, **kwargs)
        return uint256(data)

    @endpoint(f'{route}/changerequirement')
    def change_requirement(self,
                           destination_chain: int,
                           requirement: int,
                           gas_price: int,
                           **kwargs) -> uint256:
        """Creates and broadcasts a 'changeRequirement()' contract call on the multisig wallet contract. This can only be done by one of the current owners of the contract, and needs to be confirmed by a sufficient number of the other owners.

        This should only be done once all owner modifications are complete to save gas and orchestrating confirmations.

        Args:
            destination_chain (int): The destination chain.
            requirement (int): The new threshold for confirmations on the multisig wallet contract. Can usually be numOwners / 2 rounded up.
            gas_price (int): The gas price.
            **kwargs: Extra keyword arguments.

        Returns:
            uint256: The multisig wallet transactionId of the changerequirement call.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = ChangeRequirementRequest(
            destination_chain=destination_chain,
            requirement=requirement,
            gas_price=gas_price
        )
        data = self.get(request_model, **kwargs)
        return uint256(data)

    @endpoint(f'{route}/multisigtransaction')
    def multisig_transaction(self,
                             destination_chain: int,
                             transaction_id: int,
                             raw: bool,
                             **kwargs) -> Union[hexstr, TransactionResponseModel]:
        """Retrieves a multisig wallet transaction.

        Args:
            destination_chain (int): The destination chain.
            transaction_id (int): The multisig wallet transactionId (int, not transaction hash).
            raw (bool): Indicates whether to partially decode the transaction or leave it in raw hex format.
            **kwargs: Extra keyword arguments.

        Returns:
            Union[hexstr, TransactionResponseModel]: The multisig wallet transaction data.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = MultisigTransactionRequest(
            destination_chain=destination_chain,
            transaction_id=transaction_id,
            raw=raw
        )
        data = self.get(request_model, **kwargs)
        if raw:
            return hexstr(data)
        else:
            return TransactionResponseModel(**data)

    @endpoint(f'{route}/multisigconfirmations')
    def multisig_confirmations(self,
                               destination_chain: int,
                               transaction_id: int,
                               **kwargs) -> List[str]:
        """Returns the list of contract owners that confirmed a particular multisig transaction.

        Args:
            destination_chain (int): The destination chain.
            transaction_id (int): The multisig wallet transactionId (int, not transaction hash).
            **kwargs: Extra keyword arguments.

        Returns:
            List[str]: A list of owner addresses that confirmed the transaction.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = MultisigConfirmationsRequest(
            destination_chain=destination_chain,
            transaction_id=transaction_id
        )
        data = self.get(request_model, **kwargs)
        return data

    @endpoint(f'{route}/balance')
    def balance(self,
                destination_chain: int,
                account: str,
                **kwargs) -> Money:
        """Retrieves the wSTRAX balance of a given account.

        Args:
            destination_chain (int): The chain the wSTRAX ERC20 contract is deployed to.
            account (str): The account to retrieve the balance for.
            **kwargs: Extra keyword arguments.

        Returns:
            Money: The wSTRAX account balance.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = BalanceRequest(
            destination_chain=destination_chain,
            account=account
        )
        data = self.get(request_model, **kwargs)
        return Money(data)

    @endpoint(f'{route}/requests/delete')
    def requests_delete(self, **kwargs) -> Money:
        """Deletes conversion requests.

        Args:
            **kwargs: Extra keyword arguments.

        Returns:
            str: A message about the status of the request.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.delete(**kwargs)
        return data

    @endpoint(f'{route}/requests/setoriginator')
    def requests_setoriginator(self, request_id: int, **kwargs) -> str:
        """Endpoint that allows the multisig operator to set itself as the originator (submittor) for a given request id.

        Args:
            request_id (int): The requestId in question.
            **kwargs: Extra keyword arguments.

        Returns:
            str: A message about the status of the request.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = SetOriginatorRequest(request_id=request_id)
        data = self.post(request_model, **kwargs)
        return data

    @endpoint(f'{route}/requests/setnotoriginator')
    def requests_setnotoriginator(self, request_id: int, **kwargs) -> str:
        """Endpoint that allows the multisig operator to reset the request as NotOriginator.

        Args:
            request_id (int): The requestId in question.
            **kwargs: Extra keyword arguments.

        Returns:
            str: A message about the status of the request.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = SetOriginatorRequest(request_id=request_id)
        data = self.post(request_model, **kwargs)
        return data

    @endpoint(f'{route}/requests/reprocessburn')
    def requests_reprocess_burn(self,
                                request_id: int,
                                height: int,
                                **kwargs) -> str:
        """Endpoint that allows the multisig operator to reprocess a burn.

        Args:
            request_id (int): The requestId to reprocess burn.
            height (int): The height at which to reprocess the burn.
            **kwargs: Extra keyword arguments.

        Returns:
            str: A message about the status of the request.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = ReprocessBurnRequest(request_id=request_id, height=height)
        data = self.post(request_model, **kwargs)
        return data

    @endpoint(f'{route}/requests/pushvote')
    def requests_pushvote(self,
                          request_id: int,
                          vote_id: int,
                          **kwargs) -> str:
        """Endpoint that allows the multisig operator to manually add a vote if they are originator of the request.

        Args:
            request_id (int): The request id.
            vote_id (int): The vote id.
            **kwargs: Extra keyword arguments.

        Returns:
            str: A message about the status of the request.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = PushVoteRequest(request_id=request_id, vote_id=vote_id)
        data = self.post(request_model, **kwargs)
        return data
