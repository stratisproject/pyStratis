import pytest
from pytest_mock import MockerFixture
from pystratis.api.mining import Mining
from pystratis.api.mining.responsemodels import *
from pystratis.core.networks import StraxMain


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_generate(mocker: MockerFixture, network, generate_uint256):
    data = {
        'blocks': [
            generate_uint256,
            generate_uint256
        ]
    }
    mocker.patch.object(Mining, 'post', return_value=data)
    mining = Mining(network=network, baseuri=mocker.MagicMock())

    response = mining.generate(block_count=2)

    assert response == GenerateBlocksModel(**data)
    # noinspection PyUnresolvedReferences
    mining.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_stop_mining(mocker: MockerFixture, network):
    data = None
    mocker.patch.object(Mining, 'post', return_value=data)
    mining = Mining(network=network, baseuri=mocker.MagicMock())

    mining.stop_mining()

    # noinspection PyUnresolvedReferences
    mining.post.assert_called_once()
