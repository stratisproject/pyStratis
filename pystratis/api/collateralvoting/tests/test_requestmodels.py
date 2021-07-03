import pytest
import json
from pystratis.api.collateralvoting.requestmodels import *
from pystratis.core.networks import StraxMain, CirrusMain
from pystratis.core import PubKey
from pystratis.core.types import Address


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_schedulevotekickfedmemberrequest(network, generate_compressed_pubkey, generate_p2pkh_address):
    data = {
        'pubKeyHex': generate_compressed_pubkey,
        'collateralAmountSatoshis': 100000_0000_0000,
        'collateralMainchainAddress': generate_p2pkh_address(network=network)
    }
    request_model = ScheduleVoteKickFedMemberRequest(
        pubkey_hex=PubKey(data['pubKeyHex']),
        collateral_amount_satoshis=100000_0000_0000,
        collateral_mainchain_address=Address(address=data['collateralMainchainAddress'], network=network),

    )
    assert json.dumps(data) == request_model.json()
