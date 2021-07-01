import pytest
from pytest_mock import MockerFixture
from api.mining import Mining
from api.mining.requestmodels import *
from api.mining.responsemodels import *
from pybitcoin.networks import StraxMain


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Mining.route + '/' in endpoint:
            assert endpoint in Mining.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Mining.route + '/' in endpoint:
            assert endpoint in Mining.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Mining.route + '/' in endpoint:
            assert endpoint in Mining.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Mining.route + '/' in endpoint:
            assert endpoint in Mining.endpoints


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_generate(mocker: MockerFixture, network, generate_uint256):
    data = {
        'blocks': [
            generate_uint256,
            generate_uint256
        ]
    }
    mocker.patch.object(Mining, 'post', return_value=data)
    mining = Mining(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = mining.generate(block_count=2)

    assert response == GenerateBlocksModel(**data)
    # noinspection PyUnresolvedReferences
    mining.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_stop_mining(mocker: MockerFixture, network):
    data = None
    mocker.patch.object(Mining, 'post', return_value=data)
    mining = Mining(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    mining.stop_mining()

    # noinspection PyUnresolvedReferences
    mining.post.assert_called_once()
