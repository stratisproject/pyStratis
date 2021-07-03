import pytest
from pytest_mock import MockerFixture
from pystratis.api.mempool import Mempool
from pystratis.core.networks import StraxMain, CirrusMain
from pystratis.core.types import uint256


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths']]
    for endpoint in paths:
        if Mempool.route + '/' in endpoint:
            assert endpoint in Mempool.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths']]
    for endpoint in paths:
        if Mempool.route + '/' in endpoint:
            assert endpoint in Mempool.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths']]
    for endpoint in paths:
        if Mempool.route + '/' in endpoint:
            assert endpoint in Mempool.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths']]
    for endpoint in paths:
        if Mempool.route + '/' in endpoint:
            assert endpoint in Mempool.endpoints


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_raw_mempool(mocker: MockerFixture, network, generate_uint256):
    data = [
        generate_uint256,
        generate_uint256,
        generate_uint256
    ]
    mocker.patch.object(Mempool, 'get', return_value=data)
    mempool = Mempool(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = mempool.get_raw_mempool()

    assert response == [uint256(x) for x in data]
    # noinspection PyUnresolvedReferences
    mempool.get.assert_called_once()
