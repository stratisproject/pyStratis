import pytest
from api.collateralvoting.requestmodels import *
from pybitcoin.types import Address, Money
from pybitcoin.networks import CirrusRegTest


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_join_federation(interflux_cirrusminer_node, get_federation_compressed_pubkey, generate_p2pkh_address):
    request_model = ScheduleVoteKickFedMemberRequest(
        pubkey_hex=get_federation_compressed_pubkey(index=0),
        collateral_amount_satoshis=Money(10),
        collateral_mainchain_address=Address(address=generate_p2pkh_address(network=CirrusRegTest()), network=CirrusRegTest()),
    )
    interflux_cirrusminer_node.collateralvoting.schedulevote_kickfedmember(request_model=request_model)
