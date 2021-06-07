import pytest
from pytest_mock import MockerFixture
from api.federationwallet import FederationWallet


@pytest.mark.skip
def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if FederationWallet.route + '/' in endpoint:
            assert endpoint in FederationWallet.endpoints


@pytest.mark.skip
def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if FederationWallet.route + '/' in endpoint:
            assert endpoint in FederationWallet.endpoints


@pytest.mark.skip
def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if FederationWallet.route + '/' in endpoint:
            assert endpoint in FederationWallet.endpoints


@pytest.mark.skip
def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if FederationWallet.route + '/' in endpoint:
            assert endpoint in FederationWallet.endpoints

# @pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])


def test_general_info():
    # TODO
    pass


def test_balance():
    # TODO
    pass


def test_history():
    # TODO
    pass


def test_sync():
    # TODO
    pass


def test_enable_federation():
    # TODO
    pass


def test_remove_transactions():
    # TODO
    pass


