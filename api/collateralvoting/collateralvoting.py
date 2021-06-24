from typing import Union
from pybitcoin import PubKey
from pybitcoin.types import hexstr, Address
from api import APIRequest, EndpointRegister, endpoint
from api.collateralvoting.requestmodels import *


class CollateralVoting(APIRequest, metaclass=EndpointRegister):
    route = '/api/collateralvoting'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/schedulevote-kickfedmember')
    def schedulevote_kickfedmember(self,
                                   pubkey_hex: Union[str, hexstr, PubKey],
                                   collateral_amount_satoshis: int,
                                   collateral_mainchain_address: Union[Address, str],
                                   **kwargs) -> None:
        """Schedule a vote to kick an existing federation member.

        Args:
            pubkey_hex (PubKey): The fedmember pubkey hex value.
            collateral_amount_satoshis (int): The collateral amount in satoshis.
            collateral_mainchain_address (Address | str): The mainchain address holding the collateral.
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        if isinstance(pubkey_hex, (str, hexstr)):
            pubkey_hex = PubKey(pubkey_hex)
        if isinstance(collateral_mainchain_address, str):
            collateral_mainchain_address = Address(address=collateral_mainchain_address, network=self._network)
        request_model = ScheduleVoteKickFedMemberRequest(
            pubkey_hex=pubkey_hex,
            collateral_amount_satoshis=collateral_amount_satoshis,
            collateral_mainchain_address=collateral_mainchain_address
        )
        self.post(request_model, **kwargs)
