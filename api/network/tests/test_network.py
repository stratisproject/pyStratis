import pytest
from pytest_mock import MockerFixture
from api.network import Network


@pytest.mark.skip
def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Network.route + '/' in endpoint:
            assert endpoint in Network.endpoints


@pytest.mark.skip
def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Network.route + '/' in endpoint:
            assert endpoint in Network.endpoints


@pytest.mark.skip
def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Network.route + '/' in endpoint:
            assert endpoint in Network.endpoints


@pytest.mark.skip
def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Network.route + '/' in endpoint:
            assert endpoint in Network.endpoints

# @pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
