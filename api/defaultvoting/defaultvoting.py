from typing import List
from api import APIRequest, EndpointRegister, endpoint
from api.defaultvoting.requestmodels import *
from pybitcoin import PollViewModel


class DefaultVoting(APIRequest, metaclass=EndpointRegister):
    route = '/api/defaultvoting'

    def __init__(self, **kwargs):
        super(DefaultVoting, self).__init__(**kwargs)

    @endpoint(f'{route}/polls/executed')
    def executed_polls(self, request_model: ExecutedPollsRequest, **kwargs) -> List[PollViewModel]:
        """Gets a list of executed polls.

        Args:
            request_model: A ExecutedPollsRequest model
            **kwargs:

        Returns:
            List[PollViewModel]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return [PollViewModel(**x) for x in data]

    @endpoint(f'{route}/polls/finished')
    def finished_polls(self, request_model: FinishedPollsRequest, **kwargs) -> List[PollViewModel]:
        """Gets a list of finished polls.

        Args:
            request_model: A FinishedPollsRequest model.
            **kwargs:

        Returns:
            List[PollViewModel]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return [PollViewModel(**x) for x in data]

    @endpoint(f'{route}/polls/pending')
    def pending_polls(self, request_model: PendingPollsRequest, **kwargs) -> List[PollViewModel]:
        """Gets a list of finished polls.

        Args:
            request_model: A PendingPollsRequest model.
            **kwargs:

        Returns:
            List[PollViewModel]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return [PollViewModel(**x) for x in data]

    @endpoint(f'{route}/polls/schedulevote-whitelisthash')
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
        self.get(request_model, **kwargs)

    @endpoint(f'{route}/polls/schedulevote-removehash')
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
        self.get(request_model, **kwargs)
