import pytest
from pytest_mock import MockerFixture
from pystratis.api.mempool import Mempool
from pystratis.core.networks import StraxMain, CirrusMain
from pystratis.core.types import uint256


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_raw_mempool(mocker: MockerFixture, network, generate_uint256):
    data = [
        generate_uint256,
        generate_uint256,
        generate_uint256
    ]
    mocker.patch.object(Mempool, 'get', return_value=data)
    mempool = Mempool(network=network, baseuri=mocker.MagicMock())

    response = mempool.get_raw_mempool()

    assert response == [uint256(x) for x in data]
    # noinspection PyUnresolvedReferences
    mempool.get.assert_called_once()
