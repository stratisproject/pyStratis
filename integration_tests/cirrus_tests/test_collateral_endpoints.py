import pytest
from nodes import CirrusNode
from api.collateral.requestmodels import *
from api.collateral.responsemodels import *
from pybitcoin.types import Address
from pybitcoin.networks import StraxRegTest


@pytest.mark.skip(reason='Does not work in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_join_federation(cirrus_node: CirrusNode, generate_p2pkh_address, wait_n_blocks_and_sync):
    # This method is present in the cirrus node but needs to be tested in interflux federation because it requires querying counter chain.
    wait_n_blocks_and_sync(2)
    request_model = JoinFederationRequest(
        collateral_address=Address(address=generate_p2pkh_address(network=StraxRegTest()), network=StraxRegTest()),
        collateral_wallet_name='Test',
        collateral_wallet_password='password',
        wallet_name='Test',
        wallet_account='account 0',
        wallet_password='password',
    )
    response = cirrus_node.collateral.join_federation(request_model)
    if response is not None:
        assert isinstance(response, JoinFederationResponseModel)
