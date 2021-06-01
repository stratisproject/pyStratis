import pytest
from pytest_mock import MockerFixture
from api.collateralvoting import CollateralVoting
from api.collateralvoting.requestmodels import *
from pybitcoin import Address
from pybitcoin.types import Money
from pybitcoin.networks import StraxMain


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if CollateralVoting.route + '/' in endpoint:
            assert endpoint in CollateralVoting.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if CollateralVoting.route + '/' in endpoint:
            assert endpoint in CollateralVoting.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if CollateralVoting.route + '/' in endpoint:
            assert endpoint in CollateralVoting.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if CollateralVoting.route + '/' in endpoint:
            assert endpoint in CollateralVoting.endpoints


@pytest.mark.parametrize('network', [StraxMain()], ids=['Main'])
def test_join_federation(mocker: MockerFixture, network, fakeuri, create_p2pkh_address,
                         generate_compressed_pubkey):
    request = ScheduleVoteKickFedMemberRequest(
        pubkey_hex=generate_compressed_pubkey,
        collateral_amount_satoshis=Money(100000),
        collateral_mainchain_address=Address(address=create_p2pkh_address(network=network), network=network),
    )
    mocker.patch.object(CollateralVoting, 'post', return_value=None)
    collateralvoting = CollateralVoting(network=network, baseuri=fakeuri)
    collateralvoting.schedulevote_kickfedmember(request_model=request)

    # noinspection PyUnresolvedReferences
    collateralvoting.post.assert_called_once()
