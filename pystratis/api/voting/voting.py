from typing import List, Union
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.voting.requestmodels import *
from pystratis.api.voting.responsemodels import *
from pystratis.core.types import hexstr, uint256


class Voting(APIRequest, metaclass=EndpointRegister):
    """Implements the voting api endpoints."""

    route = '/api/voting'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/polls/pending')
    def pending_polls(self,
                      vote_type: int,
                      pubkey_of_member_being_voted_on: Union[hexstr, str],
                      **kwargs) -> List[PollViewModel]:
        """Gets a list of pending polls.

        Args:
            vote_type (VoteKey, optional): The type of vote to query.
            pubkey_of_member_being_voted_on (PubKey, optional): The pubkey to query.
            **kwargs: Extra keyword arguments. 

        Returns:
            List[PollViewModel]: A list of pending polls.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(pubkey_of_member_being_voted_on, str):
            pubkey_of_member_being_voted_on = hexstr(pubkey_of_member_being_voted_on)
        request_model = PollsRequest(
            vote_type=vote_type,
            pubkey_of_member_being_voted_on=pubkey_of_member_being_voted_on
        )
        data = self.get(request_model, **kwargs)
        return [PollViewModel(**x) for x in data]

    @endpoint(f'{route}/polls/finished')
    def finished_polls(self,
                       vote_type: int,
                       pubkey_of_member_being_voted_on: Union[hexstr, str],
                       **kwargs) -> List[PollViewModel]:
        """Gets a list of finished polls.

        Args:
            vote_type (VoteKey, optional): The type of vote to query.
            pubkey_of_member_being_voted_on (PubKey, optional): The pubkey to query.
            **kwargs: Extra keyword arguments. 

        Returns:
            List[PollViewModel]: A list of finished polls.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(pubkey_of_member_being_voted_on, str):
            pubkey_of_member_being_voted_on = hexstr(pubkey_of_member_being_voted_on)
        request_model = PollsRequest(
            vote_type=vote_type,
            pubkey_of_member_being_voted_on=pubkey_of_member_being_voted_on
        )
        data = self.get(request_model, **kwargs)
        return [PollViewModel(**x) for x in data]

    @endpoint(f'{route}/polls/executed')
    def executed_polls(self,
                       vote_type: int,
                       pubkey_of_member_being_voted_on: Union[hexstr, str],
                       **kwargs) -> List[PollViewModel]:
        """Gets a list of executed polls.

        Args:
            vote_type (VoteKey, optional): The type of vote to query.
            pubkey_of_member_being_voted_on (PubKey, optional): The pubkey to query.
            **kwargs: Extra keyword arguments. 

        Returns:
            List[PollViewModel]: A list of executed polls.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(pubkey_of_member_being_voted_on, str):
            pubkey_of_member_being_voted_on = hexstr(pubkey_of_member_being_voted_on)
        request_model = PollsRequest(
            vote_type=vote_type,
            pubkey_of_member_being_voted_on=pubkey_of_member_being_voted_on
        )
        data = self.get(request_model, **kwargs)
        return [PollViewModel(**x) for x in data]

    @endpoint(f'{route}/whitelistedhashes')
    def whitelisted_hashes(self, **kwargs) -> List[WhitelistedHashesModel]:
        """Gets a list of whitelisted hashes.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            List[WhitelistedhashesModel]: A list of whitelisted hashes.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return [WhitelistedHashesModel(**x) for x in data]

    @endpoint(f'{route}/schedulevote-whitelisthash')
    def schedulevote_whitelisthash(self,
                                   hash_id: Union[uint256, str],
                                   **kwargs) -> None:
        """Vote to add a hash from whitelist.

        Args:
            hash_id (uint256, str): The hash to whitelist.
            **kwargs: Extra keyword arguments. 

        Returns:
            None

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(hash_id, str):
            hash_id = uint256(hash_id)
        request_model = ScheduleVoteWhitelistHashRequest(hash_id=hash_id)
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/schedulevote-removehash')
    def schedulevote_removehash(self,
                                hash_id: Union[uint256, str],
                                **kwargs) -> None:
        """Vote to remove a hash from whitelist.

        Args:
            hash_id (uint256, str): The hash to remove.
            **kwargs: Extra keyword arguments. 

        Returns:
            None

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(hash_id, str):
            hash_id = uint256(hash_id)
        request_model = ScheduleVoteRemoveHashRequest(hash_id=hash_id)
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/scheduledvotes')
    def scheduled_votes(self, **kwargs) -> List[VotingDataModel]:
        """Gets the scheduled voting data.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            List[VotingDataModel]: A list of voting data.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return [VotingDataModel(**x) for x in data]
