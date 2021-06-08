import pytest
from pytest_mock import MockerFixture
from api.collateral import Collateral
from api.collateral.requestmodels import *
from api.collateral.responsemodels import *
from pybitcoin.networks import StraxMain
from pybitcoin.types import Address


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Collateral.route + '/' in endpoint:
            assert endpoint in Collateral.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Collateral.route + '/' in endpoint:
            assert endpoint in Collateral.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Collateral.route + '/' in endpoint:
            assert endpoint in Collateral.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Collateral.route + '/' in endpoint:
            assert endpoint in Collateral.endpoints


@pytest.mark.parametrize('strax_network', [StraxMain()], ids=['Main'])
def test_join_federation(mocker: MockerFixture, strax_network, fakeuri, generate_p2pkh_address,
                         generate_compressed_pubkey):
    request = JoinFederationRequest(
        collateral_address=Address(address=generate_p2pkh_address(network=strax_network), network=strax_network),
        collateral_wallet_name='Test_InterfluxStrax_Wallet',
        collateral_wallet_password='cirrus_password',
        wallet_name='Test_InterfluxCirrus_Wallet',
        wallet_account='account 0',
        wallet_password='cirrus_assword',
    )
    data = {'MinerPublicKey': generate_compressed_pubkey}
    mocker.patch.object(Collateral, 'post', return_value=data)
    collateral = Collateral(network=strax_network, baseuri=fakeuri)
    response = collateral.join_federation(request_model=request)

    assert response == JoinFederationResponseModel(**data)
    # noinspection PyUnresolvedReferences
    collateral.post.assert_called_once()
