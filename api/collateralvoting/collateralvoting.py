from api import APIRequest, EndpointRegister, endpoint
from api.collateralvoting.requestmodels import *


class CollateralVoting(APIRequest, metaclass=EndpointRegister):
    route = '/api/collateralvoting'

    def __init__(self, **kwargs):
        super(CollateralVoting, self).__init__(**kwargs)

    @endpoint(f'{route}/schedulevote-kickfedmember')
    def schedulevote_kickfedmember(self, request_model: ScheduleVoteKickFedMemberRequest, **kwargs) -> None:
        """Schedule a vote to kick an existing federation member.

        Args:
            request_model: ScheduleVoteKickFedMemberRequest model
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        self.post(request_model, **kwargs)
