from typing import List
from api import APIRequest, EndpointRegister, endpoint
from api.voting.requestmodels import *
from api.voting.responsemodels import *


class Voting(APIRequest, metaclass=EndpointRegister):
    route = '/api/voting'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/polls/pending')
    def pending_polls(self, request_model: PollsRequest, **kwargs) -> List[PollViewModel]:
        """Gets a list of pending polls.

        Args:
            request_model: PollsRequest model
            **kwargs:

        Returns:
            List[PollViewModel]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return [PollViewModel(**x) for x in data]

    @endpoint(f'{route}/polls/finished')
    def finished_polls(self, request_model: PollsRequest, **kwargs) -> List[PollViewModel]:
        """Gets a list of finished polls.

        Args:
            request_model: PollsRequest model
            **kwargs:

        Returns:
            List[PollViewModel]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return [PollViewModel(**x) for x in data]

    @endpoint(f'{route}/polls/executed')
    def executed_polls(self, request_model: PollsRequest, **kwargs) -> List[PollViewModel]:
        """Gets a list of executed polls.

        Args:
            request_model: A PollsRequest model
            **kwargs:

        Returns:
            List[PollViewModel]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return [PollViewModel(**x) for x in data]

    @endpoint(f'{route}/whitelistedhashes')
    def whitelisted_hashes(self, **kwargs) -> List[WhitelistedHashesModel]:
        """Gets a list of whitelisted hashes.

        Args:
            **kwargs:

        Returns:
            List[WhitelistedhashesModel]

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return [WhitelistedHashesModel(**x) for x in data]

    @endpoint(f'{route}/schedulevote-whitelisthash')
    def schedulevote_whitelisthash(self, request_model: ScheduleVoteWhitelistHashRequest, **kwargs) -> None:
        """Vote to add a hash from whitelist.

        Args:
            request_model: A ScheduleVoteWhitelistHashRequest model.
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/schedulevote-removehash')
    def schedulevote_removehash(self, request_model: ScheduleVoteRemoveHashRequest, **kwargs) -> None:
        """Vote to remove a hash from whitelist.

        Args:
            request_model: A ScheduleVoteRemoveHashRequest model.
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/scheduledvotes')
    def scheduled_votes(self, **kwargs) -> List[VotingDataModel]:
        """Gets the scheduled voting data.

        Args:
            **kwargs:

        Returns:
            List[VotingDataModel]

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return [VotingDataModel(**x) for x in data]
