import pytest
import json
from api.collateralvoting.requestmodels import *
from pybitcoin.networks import StraxMain, CirrusMain
from pybitcoin import PubKey
from pybitcoin.types import Address, Money


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_schedulevotekickfedmemberrequest(network, generate_compressed_pubkey, generate_p2pkh_address):
    data = {
        'pubKeyHex': generate_compressed_pubkey,
        'collateralAmountSatoshis': '100000.00000000',
        'collateralMainchainAddress': generate_p2pkh_address(network=network)
    }
    request_model = ScheduleVoteKickFedMemberRequest(
        pubkey_hex=PubKey(data['pubKeyHex']),
        collateral_amount_satoshis=Money(100000_0000_0000),
        collateral_mainchain_address=Address(address=data['collateralMainchainAddress'], network=network),

    )
    assert json.dumps(data) == request_model.json()
